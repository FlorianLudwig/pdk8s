import pathlib

import pdk8s.k8s
import pdk8s.cli


TEST_CHARTS = pathlib.Path(__file__).parent / pathlib.Path("test_charts")


def test_load_chart_from_file():
    # test basic loading of python files
    empty = pdk8s.cli.load_chart_from_file(TEST_CHARTS / pathlib.Path("empty.py"))

    assert empty["name"] == "empty_chart"
    assert empty["chart"] == []

    # Simple chart
    ## makes sure that importing pdk8s works
    simple = pdk8s.cli.load_chart_from_file(TEST_CHARTS / pathlib.Path("simple.py"))
    assert simple["name"] == "simple_chart"
    assert isinstance(simple["chart"][0], pdk8s.k8s.Service)
    