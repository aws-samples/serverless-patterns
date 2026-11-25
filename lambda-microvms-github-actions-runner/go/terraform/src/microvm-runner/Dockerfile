# Lambda builds this on top of the managed AL2023 MicroVM base image
# (--base-image-arn); FROM only selects the container for the app layers.
# The runner is pre-extracted so it is baked into the snapshot.
# arm64: must match CpuConfigurations (ARM_64) in main.tf and ARCH in build.sh.
FROM arm64v8/debian:13-slim

# Bump RUNNER_SHA256 with RUNNER_VERSION (checksum from the release notes at
# https://github.com/actions/runner/releases), or `sha256sum -c` fails the build.
ARG RUNNER_VERSION=2.337.0
ARG RUNNER_ARCH=arm64
ARG RUNNER_SHA256=9b1dc70626422526e3c94767cf024896beb15da5342a3f4819bf2feac13e0393
# Upstream minor only, so Debian security rebuilds still match. Must be the
# minor shipped by the Debian suite in FROM.
ARG BUILDAH_VERSION=1.39

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates git curl tar gzip \
    && rm -rf /var/lib/apt/lists/*

# --- GitHub Actions runner ---
# Runs as root: buildah's chroot isolation needs it. Acceptable because each
# MicroVM is single-use and terminates after one job.
WORKDIR /opt/actions-runner
RUN curl -fsSL -o runner.tar.gz \
      "https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-${RUNNER_ARCH}-${RUNNER_VERSION}.tar.gz" \
    && echo "${RUNNER_SHA256}  runner.tar.gz" | sha256sum -c - \
    && tar xzf runner.tar.gz \
    && rm runner.tar.gz \
    && ./bin/installdependencies.sh \
    && rm -rf /var/lib/apt/lists/*

# --- buildah ---
# dockerd can't run in the MicroVM (no mount/PID namespaces, no cgroup v2), so
# CI jobs use buildah with chroot isolation and the vfs driver.
# netavark: buildah refuses to build without a network backend.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        "buildah=${BUILDAH_VERSION}.*" \
        netavark \
    && rm -rf /var/lib/apt/lists/* \
    && buildah --version \
    && buildah --version | grep -qF "buildah version ${BUILDAH_VERSION}."

# Defaults so CI jobs can run plain `buildah bud`. Short image names resolve
# to Docker Hub, as with docker.
RUN mkdir -p /etc/containers/registries.conf.d \
    && printf '%s\n' \
        '[storage]' \
        'driver = "vfs"' \
        'runroot = "/run/containers/storage"' \
        'graphroot = "/var/lib/containers/storage"' \
        > /etc/containers/storage.conf \
    && printf '%s\n' \
        'unqualified-search-registries = ["docker.io"]' \
        > /etc/containers/registries.conf.d/50-microvm-runner.conf
ENV BUILDAH_ISOLATION=chroot

# --- Supervisor: answers the hooks, runs the job, self-terminates ---
COPY supervisor /usr/local/bin/supervisor

# The runner refuses to run as root without this flag.
ENV RUNNER_DIR=/opt/actions-runner
ENV RUNNER_ALLOW_RUNASROOT=1

# Lifecycle hooks port; must match Hooks.Port in main.tf.
EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/supervisor"]
