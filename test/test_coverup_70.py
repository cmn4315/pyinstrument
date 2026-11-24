# file: pyinstrument/__main__.py:533-549
# asked: {"lines": [536, 537, 538, 539, 540, 543, 544, 545, 547, 548], "branches": []}
# gained: {"lines": [536, 537, 538, 539, 540, 543, 544, 545, 547, 548], "branches": []}

from typing import TextIO, Type

import pytest
from _pytest.monkeypatch import MonkeyPatch

from pyinstrument import renderers
from pyinstrument.__main__ import OptionsParseError, create_renderer
from pyinstrument.util import file_supports_color, file_supports_unicode


class MockTextIO(TextIO):
    def __init__(self, unicode_support: bool, color_support: bool):
        self.unicode_support = unicode_support
        self.color_support = color_support

    def write(self, s: str) -> int:
        return len(s)

    def flush(self) -> None:
        pass

    def close(self) -> None:
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_create_renderer_success(monkeypatch: MonkeyPatch):
    class MockRenderer(renderers.Renderer):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    class MockOptions:
        def __init__(self):
            self.renderer_options = {}

    def mock_compute_render_options(options, renderer_class, unicode_support, color_support):
        return options.renderer_options

    monkeypatch.setattr("pyinstrument.__main__.compute_render_options", mock_compute_render_options)
    output_file = MockTextIO(unicode_support=True, color_support=True)
    options = MockOptions()
    renderer = create_renderer(MockRenderer, options, output_file)
    assert isinstance(renderer, MockRenderer)


def test_create_renderer_type_error(monkeypatch: MonkeyPatch):
    class MockRenderer(renderers.Renderer):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            raise TypeError("Bad renderer option")

    class MockOptions:
        def __init__(self):
            self.renderer_options = {}

    def mock_compute_render_options(options, renderer_class, unicode_support, color_support):
        return options.renderer_options

    monkeypatch.setattr("pyinstrument.__main__.compute_render_options", mock_compute_render_options)
    output_file = MockTextIO(unicode_support=True, color_support=True)
    options = MockOptions()
    with pytest.raises(
        OptionsParseError,
        match="Failed to create MockRenderer. Check your renderer options.\\n  Bad renderer option\\n",
    ):
        create_renderer(MockRenderer, options, output_file)


def test_create_renderer_misconfiguration_error(monkeypatch: MonkeyPatch):
    class MockRenderer(renderers.Renderer):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            raise renderers.Renderer.MisconfigurationError("Misconfiguration")

    class MockOptions:
        def __init__(self):
            self.renderer_options = {}

    def mock_compute_render_options(options, renderer_class, unicode_support, color_support):
        return options.renderer_options

    monkeypatch.setattr("pyinstrument.__main__.compute_render_options", mock_compute_render_options)
    output_file = MockTextIO(unicode_support=True, color_support=True)
    options = MockOptions()
    with pytest.raises(
        OptionsParseError,
        match="Failed to create MockRenderer. Check your renderer options.\\n  Misconfiguration\\n",
    ):
        create_renderer(MockRenderer, options, output_file)
