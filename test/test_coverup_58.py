# file: pyinstrument/renderers/html.py:131-151
# asked: {"lines": [140, 141, 142, 143, 144, 146, 147, 149, 150, 151], "branches": [[140, 141], [140, 146]]}
# gained: {"lines": [140, 141, 142, 143, 144, 146, 147, 149, 150, 151], "branches": [[140, 141], [140, 146]]}

import os
import tempfile
import webbrowser

import pytest

from pyinstrument.renderers.html import HTMLRenderer
from pyinstrument.session import Session


def test_open_in_browser_with_tempfile(monkeypatch):
    class MockSession(Session):
        def __init__(self):
            pass

    def mock_render(self, session):
        return "<html><body>Test</body></html>"

    def mock_open(url):
        pass

    monkeypatch.setattr(HTMLRenderer, "render", mock_render)
    monkeypatch.setattr(webbrowser, "open", mock_open)

    renderer = HTMLRenderer()
    session = MockSession()
    output_filename = renderer.open_in_browser(session)
    assert output_filename.endswith(".html")
    os.remove(output_filename)


def test_open_in_browser_with_specified_filename(monkeypatch, tmp_path):
    class MockSession(Session):
        def __init__(self):
            pass

    def mock_render(self, session):
        return "<html><body>Test</body></html>"

    def mock_open(url):
        pass

    monkeypatch.setattr(HTMLRenderer, "render", mock_render)
    monkeypatch.setattr(webbrowser, "open", mock_open)

    renderer = HTMLRenderer()
    session = MockSession()
    output_filename = tmp_path / "test.html"
    result_filename = renderer.open_in_browser(session, output_filename=str(output_filename))
    assert result_filename == str(output_filename)
    assert output_filename.exists()
    output_filename.unlink()
