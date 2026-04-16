import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app


def test_layout_exists():
    assert app.layout is not None


def test_header_present():
    header = app.layout.children[0]
    assert "Soul Foods Pink Morsel Sales Visualiser" in header.children


def test_components_present():
    # Check that radio + graph exist in layout
    components = str(app.layout)

    assert "region-filter" in components
    assert "sales-chart" in components