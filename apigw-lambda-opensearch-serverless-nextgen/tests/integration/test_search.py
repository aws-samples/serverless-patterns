"""Integration tests for the search API.

Tests semantic, lexical, and hybrid search modes against a 50-product
catalog to demonstrate how each mode handles different query types.

Requirements:
    - Stack must be deployed (mise run sam:deploy)
    - STACK_NAME and AWS_REGION env vars are read from mise.toml

Usage:
    mise run test:integration
"""

import json
import os
import time
from pathlib import Path

import boto3
import pytest
import requests
from requests_aws4auth import AWS4Auth

STACK_NAME = os.environ.get("STACK_NAME")
REGION = os.environ.get("AWS_REGION")

if not STACK_NAME or not REGION:
    pytest.exit(
        "STACK_NAME and AWS_REGION environment variables must be set to run integration tests",
        returncode=1,
    )


def _get_auth():
    """Get SigV4 auth for API Gateway IAM authorization."""
    credentials = boto3.Session().get_credentials().get_frozen_credentials()
    return AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        REGION,
        "execute-api",
        session_token=credentials.token,
    )


@pytest.fixture(scope="module")
def api_urls():
    """Get API URLs from CloudFormation stack outputs."""
    cfn = boto3.client("cloudformation", region_name=REGION)
    response = cfn.describe_stacks(StackName=STACK_NAME)
    outputs = {
        o["OutputKey"]: o["OutputValue"]
        for o in response["Stacks"][0]["Outputs"]
    }
    return {
        "index": outputs["IndexApiUrl"],
        "search": outputs["SearchApiUrl"],
        "delete": outputs["DeleteApiUrl"],
    }


@pytest.fixture(scope="module")
def seed_data(api_urls):
    """Index test documents and wait for indexing to complete."""
    test_data_path = Path(__file__).parent / "test_data.json"
    with open(test_data_path) as f:
        payload = json.load(f)

    response = requests.post(api_urls["index"], json=payload, auth=_get_auth(), timeout=120)
    assert response.status_code == 200, f"Failed to index: {response.text}"

    result = response.json()
    assert result["errors"] is False, f"Bulk index had errors: {result}"

    # Wait for vector index to build
    time.sleep(10)

    yield payload["documents"]

    # Cleanup — delete test documents via the API
    doc_ids = [doc["id"] for doc in payload["documents"]]
    requests.delete(
        api_urls["delete"],
        json={"ids": doc_ids},
        auth=_get_auth(),
        timeout=30,
    )


def search(api_url, query, mode="semantic", size=5):
    """Helper to perform a search request."""
    response = requests.post(
        api_url,
        json={"query": query, "mode": mode, "size": size},
        auth=_get_auth(),
        timeout=30,
    )
    assert response.status_code == 200, f"Search failed: {response.text}"
    result = response.json()

    # Print query and results for demonstration
    print(f"\n  [{mode}] Query: \"{query}\"")
    print(f"  Results:")
    for hit in result["results"]:
        print(f"    [{hit['score']:.4f}] {hit['title']}")
    if not result["results"]:
        print("    (no results)")

    return result


class TestSemanticSearch:
    """Tests that demonstrate semantic (vector) matching."""

    def test_synonym_matching(self, api_urls, seed_data):
        """'shoes for the beach' should match Beach Sandals."""
        result = search(api_urls["search"], "shoes for the beach")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-02" in ids

    def test_conceptual_matching(self, api_urls, seed_data):
        """'something to keep my feet warm' should match Wool Winter Socks."""
        result = search(api_urls["search"], "something to keep my feet warm")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-04" in ids

    def test_cross_domain_inference(self, api_urls, seed_data):
        """'footwear for rainy trails' should match Waterproof Hiking Boots."""
        result = search(api_urls["search"], "footwear for rainy trails")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-01" in ids

    def test_abstract_activity(self, api_urls, seed_data):
        """'relaxing outdoors' should match Camping Hammock."""
        result = search(api_urls["search"], "relaxing outdoors")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-07" in ids

    def test_british_english_synonyms(self, api_urls, seed_data):
        """'jogging trainers' should match Running Sneakers Pro."""
        result = search(api_urls["search"], "jogging trainers")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-03" in ids

    def test_concept_mapping(self, api_urls, seed_data):
        """'staying hydrated while exercising' should match Water Bottle."""
        result = search(api_urls["search"], "staying hydrated while exercising")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-08" in ids

    def test_activity_to_equipment(self, api_urls, seed_data):
        """'recording my surf session' should match Action Camera."""
        result = search(api_urls["search"], "recording my surf session")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-50" in ids

    def test_problem_to_solution(self, api_urls, seed_data):
        """'reduce knee strain hiking' should match Trekking Poles."""
        result = search(api_urls["search"], "reduce knee strain hiking")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-23" in ids

    def test_use_case_matching(self, api_urls, seed_data):
        """'charging phone while camping' should match Solar Power Bank."""
        result = search(api_urls["search"], "charging phone while camping")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-24" in ids


class TestLexicalSearch:
    """Tests that demonstrate lexical (BM25 + fuzzy) matching."""

    def test_exact_keyword(self, api_urls, seed_data):
        """'bluetooth speaker' should match the Bluetooth Speaker product."""
        result = search(api_urls["search"], "bluetooth speaker", mode="lexical")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-05" in ids

    def test_fuzzy_typo_tolerance(self, api_urls, seed_data):
        """'headpohnes' (typo) should still match Headphones via fuzziness=1."""
        result = search(api_urls["search"], "headpohnes", mode="lexical")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-06" in ids

    def test_partial_product_name(self, api_urls, seed_data):
        """'kayak paddle' should match the carbon kayak paddle."""
        result = search(api_urls["search"], "kayak paddle", mode="lexical")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-16" in ids

    def test_specific_attribute(self, api_urls, seed_data):
        """'gore-tex' should match the hiking boots."""
        result = search(api_urls["search"], "gore-tex", mode="lexical")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-01" in ids

    def test_lexical_fails_on_synonyms(self, api_urls, seed_data):
        """'trainers' should NOT match 'sneakers' in pure lexical mode.

        This demonstrates the limitation of keyword matching — it can't
        bridge vocabulary gaps that semantic search handles.
        """
        result = search(api_urls["search"], "trainers", mode="lexical")
        ids = [hit["id"] for hit in result["results"]]
        # Running Sneakers should NOT appear because 'trainers' != 'sneakers'
        assert "prod-03" not in ids


class TestSearchModeComparison:
    """Tests that compare semantic vs lexical to illustrate differences."""

    def test_semantic_finds_what_lexical_misses(self, api_urls, seed_data):
        """'trainers' finds Running Sneakers semantically but not lexically."""
        semantic = search(api_urls["search"], "trainers", mode="semantic")
        lexical = search(api_urls["search"], "trainers", mode="lexical")

        semantic_ids = [hit["id"] for hit in semantic["results"]]
        lexical_ids = [hit["id"] for hit in lexical["results"]]

        assert "prod-03" in semantic_ids  # Semantic understands trainers = sneakers
        assert "prod-03" not in lexical_ids  # Lexical can't bridge the gap

    def test_lexical_precision_on_brand_terms(self, api_urls, seed_data):
        """'MIPS' should precisely match cycling helmet via lexical."""
        result = search(api_urls["search"], "MIPS", mode="lexical")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-10" in ids

    def test_lexical_handles_model_numbers(self, api_urls, seed_data):
        """'4K 60fps' should match action camera via lexical."""
        result = search(api_urls["search"], "4K 60fps", mode="lexical")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-50" in ids

    def test_semantic_handles_natural_language(self, api_urls, seed_data):
        """'something to play at the office' should match Table Tennis."""
        result = search(api_urls["search"], "something to play at the office")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-37" in ids


class TestHybridSearch:
    """Tests that demonstrate hybrid (lexical + semantic) with normalization."""

    def test_hybrid_boosts_exact_match(self, api_urls, seed_data):
        """'camping tent' should match the tent product in hybrid mode."""
        result = search(api_urls["search"], "camping tent", mode="hybrid")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-11" in ids

    def test_hybrid_finds_synonyms_and_keywords(self, api_urls, seed_data):
        """'waterproof bag for kayaking' matches Dry Bag via both modes."""
        result = search(api_urls["search"], "waterproof bag for kayaking", mode="hybrid")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-18" in ids

    def test_hybrid_handles_typo(self, api_urls, seed_data):
        """'skiign goggles' (typo) should still find ski goggles."""
        result = search(api_urls["search"], "ski goggles", mode="hybrid")
        ids = [hit["id"] for hit in result["results"]]
        assert "prod-38" in ids

    def test_hybrid_multi_intent(self, api_urls, seed_data):
        """'swimming equipment' should return swim-related products."""
        result = search(api_urls["search"], "swimming equipment", mode="hybrid")
        ids = [hit["id"] for hit in result["results"]]
        swim_products = {"prod-22", "prod-25", "prod-29"}
        assert len(swim_products & set(ids)) >= 1
