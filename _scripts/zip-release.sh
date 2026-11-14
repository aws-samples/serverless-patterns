#!/usr/bin/env bash
# Builds pattern zips and publishes them to the shard releases (zips-1 .. zips-N, see
# zip-shard.mjs) and to v1.0.0. Used by .github/workflows/create_update_release.yaml.
# Run from the repo root.
#
#   zip-release.sh push <file of changed pattern folders>
#   zip-release.sh backfill [mapping.csv]   build every pattern (or only the CSV rows,
#                                           under their new names) and upload what's missing
#   zip-release.sh cleanup [mapping.csv]    delete shard assets with no pattern or the wrong
#                                           shard; in v1.0.0, everything but legacy-zips.json
#                                           (only once dualWriteV1 is false)
#
# Env: DRY_RUN=true reads GitHub as usual but prints each create, upload and delete instead
# of doing it. MAX_UPLOADS caps backfill uploads and cleanup deletes (default 450: each
# upload is about 2 API calls, against GITHUB_TOKEN's 1,000 requests an hour and GitHub's
# ~500 content-creating requests an hour). Re-run to resume.
set -euo pipefail

REPO=${GITHUB_REPOSITORY:-aws-samples/serverless-patterns}
DRY_RUN=${DRY_RUN:-false}
MAX_UPLOADS=${MAX_UPLOADS:-450}
PAUSE=${PAUSE:-3}
OUT=${OUT:-temp_archives}
V1=$(node _scripts/zip-plan.mjs --config v1Tag)
DUAL=$(node _scripts/zip-plan.mjs --config dualWriteV1)
mkdir -p "$OUT"
writes=0
known_releases=" "

case "$MAX_UPLOADS" in '' | *[!0-9]*) echo "MAX_UPLOADS must be a number" >&2; exit 1 ;; esac

write() { # a GitHub write, or just print it in a dry run
  if [ "$DRY_RUN" = true ]; then echo "DRY RUN: $*"; else "$@"; fi
}

all_folders() { # every folder holding an example-pattern.json
  find . -name example-pattern.json -not -path './.git/*' -not -path './.github/*' \
    -not -path './_*' -not -path '*/node_modules/*' |
    sed 's|/example-pattern\.json$||; s|^\./||' | sort -u
}

build_zip() { # <folder> <zip name>: $OUT/<zip name>.zip holding the folder under <zip name>/
  local stage="$OUT/stage/$2"
  rm -rf "$OUT/stage" "$OUT/$2.zip"
  mkdir -p "$stage"
  cp -a "$1/." "$stage/"
  (cd "$OUT/stage" && zip -rq "../$2.zip" "$2")
  rm -rf "$OUT/stage"
}

list_assets() { # asset names of a release; nothing if the release doesn't exist
  local id
  id=$(gh api "repos/$REPO/releases/tags/$1" --jq .id 2>/dev/null) || return 0
  gh api --paginate "repos/$REPO/releases/$id/assets?per_page=100" --jq '.[].name'
}

keep_v1_latest() { # the AWS Toolkit downloads from releases/latest, which must stay v1.0.0
  local latest
  latest=$(gh api "repos/$REPO/releases/latest" --jq .tag_name)
  if [ "$latest" != "$V1" ]; then
    echo "::warning::Latest release is $latest, not $V1. Marking $V1 as latest again."
    write gh release edit "$V1" -R "$REPO" --latest
  fi
}

ensure_shard() { # create the shard release on first use, never as "latest"
  case "$known_releases" in *" $1 "*) return 0 ;; esac
  if ! gh release view "$1" -R "$REPO" >/dev/null 2>&1; then
    echo "Creating release $1"
    # If a parallel run made it first, create fails and the view succeeds.
    write gh release create "$1" -R "$REPO" --latest=false --title "Pattern zips ($1)" \
      --notes "Pattern zips for Serverless Land download links, shard $1. See _scripts/zip-shard.mjs. The latest release ($V1) keeps the AWS Toolkit's zips." ||
      gh release view "$1" -R "$REPO" >/dev/null
    keep_v1_latest
  fi
  known_releases="$known_releases$1 "
}

upload() { # <tag> <file>
  write gh release upload "$1" "$2" -R "$REPO" --clobber
  writes=$((writes + 1))
  echo "Uploaded $(basename "$2") to $1"
  [ "$DRY_RUN" = true ] || sleep "$PAUSE"
}

delete_asset() { # <tag> <asset name>
  write gh release delete-asset "$1" "$2" -R "$REPO" -y
  writes=$((writes + 1))
  [ "$DRY_RUN" = true ] || sleep "$PAUSE"
}

load_exclude() { # Serverless Land's "don't build" list for v1.0.0. Stop if it can't be read.
  curl -fsSL https://serverlessland.com/pattern-zip-exclude.json | jq -r '.exclude[]' >"$OUT/zip-exclude.txt"
  echo "v1.0.0 exclude list: $(wc -l <"$OUT/zip-exclude.txt" | tr -d ' ') patterns"
}

cmd_push() {
  [ -s "$1" ] || { echo "No changed patterns"; return 0; }
  if [ "$DUAL" = true ]; then load_exclude; fi
  node _scripts/zip-plan.mjs <"$1" >"$OUT/plan.tsv"
  local folder zip tag legacy name in_v1
  while IFS=$'\t' read -r folder zip tag legacy <&3; do
    build_zip "$folder" "$zip"
    ensure_shard "$tag"
    upload "$tag" "$OUT/$zip.zip"
    in_v1=
    if [ "$DUAL" = true ]; then
      if grep -qxF "$zip" "$OUT/zip-exclude.txt"; then
        echo "Not uploading $zip to $V1 (excluded)"
      else
        upload "$V1" "$OUT/$zip.zip"
        in_v1=$zip
      fi
    fi
    for name in ${legacy//,/ }; do
      if [ "$name" = - ] || [ "$name" = "$in_v1" ]; then continue; fi
      build_zip "$folder" "$name"
      upload "$V1" "$OUT/$name.zip"
    done
  done 3<"$OUT/plan.tsv"
}

cmd_backfill() {
  if [ -n "${1:-}" ]; then
    node _scripts/zip-plan.mjs --mapping "$1" >"$OUT/plan.tsv"
  else
    all_folders | node _scripts/zip-plan.mjs >"$OUT/plan.tsv"
  fi
  echo "$(wc -l <"$OUT/plan.tsv" | tr -d ' ') patterns to check"
  local folder zip tag legacy name tags skipped=0 left=0

  # The Toolkit's legacy names in v1.0.0 first: few, and some are missing today.
  list_assets "$V1" >"$OUT/have-$V1.txt"
  while IFS=$'\t' read -r folder zip tag legacy <&3; do
    for name in ${legacy//,/ }; do
      if [ "$name" = - ] || grep -qxF "$name.zip" "$OUT/have-$V1.txt"; then continue; fi
      if [ "$writes" -ge "$MAX_UPLOADS" ]; then left=$((left + 1)); continue; fi
      build_zip "$folder" "$name"
      upload "$V1" "$OUT/$name.zip"
    done
  done 3<"$OUT/plan.tsv"

  # One asset listing per shard, then upload only what's missing.
  tags=$(cut -f3 "$OUT/plan.tsv" | sort -u)
  for tag in $tags; do list_assets "$tag" >"$OUT/have-$tag.txt"; done
  while IFS=$'\t' read -r folder zip tag legacy <&3; do
    if grep -qxF "$zip.zip" "$OUT/have-$tag.txt"; then skipped=$((skipped + 1)); continue; fi
    if [ "$writes" -ge "$MAX_UPLOADS" ]; then left=$((left + 1)); continue; fi
    build_zip "$folder" "$zip"
    ensure_shard "$tag"
    upload "$tag" "$OUT/$zip.zip"
  done 3<"$OUT/plan.tsv"

  echo "Backfill: $writes uploaded, $skipped already there, $left left."
  if [ "$left" -gt 0 ]; then echo "::warning::Stopped at max_uploads=$MAX_UPLOADS with $left zips left. Run the backfill again to resume."; fi
}

cmd_cleanup() {
  local tag asset count
  all_folders | node _scripts/zip-plan.mjs | cut -f2,3 >"$OUT/expected.tsv"
  if [ -n "${1:-}" ]; then node _scripts/zip-plan.mjs --mapping "$1" | cut -f2,3 >>"$OUT/expected.tsv"; fi
  : >"$OUT/delete.tsv"

  gh release list -R "$REPO" --limit 500 --json tagName --jq '.[].tagName' | grep -E '^zips-[0-9]+$' >"$OUT/shards.txt" || true
  while read -r tag <&3; do
    list_assets "$tag" | while IFS= read -r asset; do
      grep -qxF "${asset%.zip}"$'\t'"$tag" "$OUT/expected.tsv" || printf '%s\t%s\n' "$tag" "$asset"
    done >>"$OUT/delete.tsv"
  done 3<"$OUT/shards.txt"

  if [ "$DUAL" = true ]; then
    echo "dualWriteV1 is true: leaving $V1 as it is."
  else
    jq -r '.zips | keys[] | . + ".zip"' _scripts/legacy-zips.json >"$OUT/legacy.txt"
    list_assets "$V1" | while IFS= read -r asset; do
      grep -qxF "$asset" "$OUT/legacy.txt" || printf '%s\t%s\n' "$V1" "$asset"
    done >>"$OUT/delete.tsv"
  fi

  count=$(wc -l <"$OUT/delete.tsv" | tr -d ' ')
  echo "Assets to delete: $count"
  cut -f1 "$OUT/delete.tsv" | sort | uniq -c
  tr '\t' ' ' <"$OUT/delete.tsv"
  if [ "$DRY_RUN" = true ]; then echo "Dry run: nothing deleted."; return 0; fi

  while IFS=$'\t' read -r tag asset <&3; do
    if [ "$writes" -ge "$MAX_UPLOADS" ]; then
      echo "::warning::Stopped at max_uploads=$MAX_UPLOADS. Run the cleanup again to resume."
      break
    fi
    delete_asset "$tag" "$asset"
    echo "Deleted $asset from $tag"
  done 3<"$OUT/delete.tsv"
}

case "${1:-}" in
  push) cmd_push "${2:?changed folders file}" ;;
  backfill) cmd_backfill "${2:-}" ;;
  cleanup) cmd_cleanup "${2:-}" ;;
  *) echo "usage: $0 push <folders-file> | backfill [mapping.csv] | cleanup [mapping.csv]" >&2; exit 1 ;;
esac
