# file: pyinstrument/__main__.py:552-587
# asked: {"lines": [553, 555, 556, 558, 559, 561, 562, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 577, 578, 579, 581, 582, 586], "branches": [[555, 556], [555, 558], [558, 559], [558, 561], [561, 562], [561, 564], [564, 565], [564, 566], [566, 567], [566, 568], [568, 569], [568, 570], [570, 571], [570, 572], [572, 573], [572, 574], [574, 575], [574, 577]]}
# gained: {"lines": [553, 555, 558, 561, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 577, 578, 579, 581, 582, 586], "branches": [[555, 558], [558, 561], [561, 564], [564, 565], [564, 566], [566, 567], [566, 568], [568, 569], [568, 570], [570, 571], [570, 572], [572, 573], [572, 574], [574, 575], [574, 577]]}

import pytest

from pyinstrument import renderers
from pyinstrument.__main__ import CommandLineOptions, OptionsParseError, get_renderer_class


def test_get_renderer_class_text():
    class MockOptions:
        renderer = "text"
        output_html = False
        outfile = None

    assert get_renderer_class(MockOptions()) == renderers.ConsoleRenderer


def test_get_renderer_class_html():
    class MockOptions:
        renderer = "html"
        output_html = False
        outfile = None

    assert get_renderer_class(MockOptions()) == renderers.HTMLRenderer


def test_get_renderer_class_json():
    class MockOptions:
        renderer = "json"
        output_html = False
        outfile = None

    assert get_renderer_class(MockOptions()) == renderers.JSONRenderer


def test_get_renderer_class_speedscope():
    class MockOptions:
        renderer = "speedscope"
        output_html = False
        outfile = None

    assert get_renderer_class(MockOptions()) == renderers.SpeedscopeRenderer


def test_get_renderer_class_pyisession():
    class MockOptions:
        renderer = "pyisession"
        output_html = False
        outfile = None

    assert get_renderer_class(MockOptions()) == renderers.SessionRenderer


def test_get_renderer_class_pstats():
    class MockOptions:
        renderer = "pstats"
        output_html = False
        outfile = None

    assert get_renderer_class(MockOptions()) == renderers.PstatsRenderer


def test_get_renderer_class_import_path():
    class MockOptions:
        renderer = "pyinstrument.renderers.ConsoleRenderer"
        output_html = False
        outfile = None

    assert get_renderer_class(MockOptions()) == renderers.ConsoleRenderer


def test_get_renderer_class_invalid_import_path():
    class MockOptions:
        renderer = "invalid.import.path"
        output_html = False
        outfile = None

    with pytest.raises(OptionsParseError):
        get_renderer_class(MockOptions())
