"""
Unit tests for handler.py

The S3 Files mount is simulated using pytest's tmp_path fixture,
so no real AWS infrastructure is needed to run these tests.

Run:
    pip install pytest pandas
    pytest src/tests/ -v
"""

import os
import sys

import pytest

# Make src/ importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

SALES_CSV = """\
region,revenue,units
North,1000,10
South,2000,20
North,500,5
East,750,8
South,300,3
"""


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def patch_mount(tmp_path, monkeypatch):
    """Point MOUNT_PATH at a temp directory and reset the module constant."""
    import handler
    mount_dir = tmp_path / "s3data"
    mount_dir.mkdir()
    monkeypatch.setenv("MOUNT_PATH", str(mount_dir))
    handler.MOUNT_PATH = str(mount_dir)
    return mount_dir


@pytest.fixture()
def mount(tmp_path):
    return tmp_path / "s3data"


@pytest.fixture()
def sales_file(mount):
    """Write a standard sales CSV into the mock mount's input/ directory."""
    csv_path = mount / "input" / "sales.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.write_text(SALES_CSV)
    return mount


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

class TestHappyPath:

    def test_returns_200(self, sales_file):
        import handler
        handler.MOUNT_PATH = str(sales_file)
        result = handler.lambda_handler({"file": "input/sales.csv"}, {})
        assert result["statusCode"] == 200

    def test_row_count_is_correct(self, sales_file):
        import handler
        handler.MOUNT_PATH = str(sales_file)
        result = handler.lambda_handler({"file": "input/sales.csv"}, {})
        assert result["body"]["rows"] == 5

    def test_columns_are_returned(self, sales_file):
        import handler
        handler.MOUNT_PATH = str(sales_file)
        result = handler.lambda_handler({"file": "input/sales.csv"}, {})
        assert result["body"]["columns"] == ["region", "revenue", "units"]

    def test_preview_contains_up_to_5_rows(self, sales_file):
        import handler
        handler.MOUNT_PATH = str(sales_file)
        result = handler.lambda_handler({"file": "input/sales.csv"}, {})
        assert len(result["body"]["preview"]) == 5

    def test_preview_capped_at_5_for_large_file(self, mount):
        """Files with more than 5 rows should still return only 5 in preview."""
        import handler
        handler.MOUNT_PATH = str(mount)
        csv_path = mount / "input" / "big.csv"
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        rows = "id,value\n" + "\n".join(f"{i},{i*10}" for i in range(20))
        csv_path.write_text(rows)
        result = handler.lambda_handler({"file": "input/big.csv"}, {})
        assert len(result["body"]["preview"]) == 5

    def test_file_path_in_response(self, sales_file):
        import handler
        handler.MOUNT_PATH = str(sales_file)
        result = handler.lambda_handler({"file": "input/sales.csv"}, {})
        assert "input/sales.csv" in result["body"]["file"]


# ---------------------------------------------------------------------------
# Input validation
# ---------------------------------------------------------------------------

class TestInputValidation:

    def test_missing_file_field_returns_400(self, mount):
        import handler
        handler.MOUNT_PATH = str(mount)
        result = handler.lambda_handler({}, {})
        assert result["statusCode"] == 400
        assert "file" in result["body"]["error"].lower()

    def test_empty_event_returns_400(self, mount):
        import handler
        handler.MOUNT_PATH = str(mount)
        result = handler.lambda_handler({}, {})
        assert result["statusCode"] == 400

    def test_file_not_found_returns_404(self, mount):
        import handler
        handler.MOUNT_PATH = str(mount)
        result = handler.lambda_handler({"file": "input/missing.csv"}, {})
        assert result["statusCode"] == 404

    def test_404_error_message_contains_path(self, mount):
        import handler
        handler.MOUNT_PATH = str(mount)
        result = handler.lambda_handler({"file": "input/missing.csv"}, {})
        assert "missing.csv" in result["body"]["error"]
