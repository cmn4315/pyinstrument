# file: pyinstrument/profiler.py:381-399
# asked: {"lines": [381, 391, 392, 393, 394, 395, 398], "branches": []}
# gained: {"lines": [381, 391, 392, 393, 394, 395, 398], "branches": []}

from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from pyinstrument import renderers
from pyinstrument.profiler import Profiler


@pytest.fixture
def profiler():
    profiler = Profiler()
    profiler._Profiler__last_session = None
    profiler._Profiler__is_running = False
    return profiler


def test_write_html_with_default_parameters(profiler, tmp_path):
    html_output = "<html><body>Profile Output</body></html>"
    file_path = tmp_path / "output.html"

    with patch.object(profiler, "output", return_value=html_output) as mock_output, patch.object(
        Path, "write_text", new_callable=mock_open()
    ) as mock_write_text:
        profiler.write_html(file_path)
        mock_output.assert_called_once()
        mock_write_text.assert_called_once_with(html_output, encoding="utf-8")


def test_write_html_with_custom_parameters(profiler, tmp_path):
    html_output = "<html><body>Custom Profile Output</body></html>"
    file_path = tmp_path / "output.html"
    timeline = True
    show_all = True
    resample_interval = 0.5

    with patch.object(profiler, "output", return_value=html_output) as mock_output, patch.object(
        Path, "write_text", new_callable=mock_open()
    ) as mock_write_text:
        profiler.write_html(
            file_path, timeline=timeline, show_all=show_all, resample_interval=resample_interval
        )
        mock_output.assert_called_once()
        mock_write_text.assert_called_once_with(html_output, encoding="utf-8")
