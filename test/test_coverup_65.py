# file: pyinstrument/profiler.py:297-337
# asked: {"lines": [319, 320, 321, 322, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 336], "branches": [[319, 320], [319, 321], [321, 322], [321, 324]]}
# gained: {"lines": [319, 320, 321, 322, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 336], "branches": [[319, 320], [321, 322]]}

from io import StringIO

import pytest

from pyinstrument.profiler import Profiler
from pyinstrument.renderers.console import FlatTimeMode
from pyinstrument.typing import LiteralStr
from pyinstrument.util import file_supports_color, file_supports_unicode


def test_print_with_unicode_and_color_none():
    profiler = Profiler()
    file = StringIO()
    profiler.output_text = lambda **kwargs: "mocked output"

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("pyinstrument.util.file_supports_unicode", lambda x: True)
        mp.setattr("pyinstrument.util.file_supports_color", lambda x: True)

        profiler.print(file=file, unicode=None, color=None)
        captured = file.getvalue()
        assert captured == "mocked output\n"


def test_print_with_unicode_false_and_color_none():
    profiler = Profiler()
    file = StringIO()
    profiler.output_text = lambda **kwargs: "mocked output"

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("pyinstrument.util.file_supports_unicode", lambda x: False)
        mp.setattr("pyinstrument.util.file_supports_color", lambda x: True)

        profiler.print(file=file, unicode=None, color=None)
        captured = file.getvalue()
        assert captured == "mocked output\n"


def test_print_with_unicode_none_and_color_false():
    profiler = Profiler()
    file = StringIO()
    profiler.output_text = lambda **kwargs: "mocked output"

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("pyinstrument.util.file_supports_unicode", lambda x: True)
        mp.setattr("pyinstrument.util.file_supports_color", lambda x: False)

        profiler.print(file=file, unicode=None, color=None)
        captured = file.getvalue()
        assert captured == "mocked output\n"


def test_print_with_unicode_false_and_color_false():
    profiler = Profiler()
    file = StringIO()
    profiler.output_text = lambda **kwargs: "mocked output"

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("pyinstrument.util.file_supports_unicode", lambda x: False)
        mp.setattr("pyinstrument.util.file_supports_color", lambda x: False)

        profiler.print(file=file, unicode=None, color=None)
        captured = file.getvalue()
        assert captured == "mocked output\n"
