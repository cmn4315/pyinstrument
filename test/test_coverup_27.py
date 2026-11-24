# file: pyinstrument/profiler.py:401-409
# asked: {"lines": [401, 405, 407, 408, 409], "branches": []}
# gained: {"lines": [401, 405, 407, 408, 409], "branches": []}

from unittest.mock import Mock, patch

import pytest

from pyinstrument import renderers
from pyinstrument.profiler import Profiler


@pytest.fixture
def profiler():
    return Profiler()


@patch("pyinstrument.profiler.Profiler._get_last_session_or_fail")
def test_open_in_browser_defaults(mock_get_last_session_or_fail, profiler):
    mock_get_last_session_or_fail.return_value = "mocked_session"
    renderer_mock = Mock()
    renderer_mock.open_in_browser = Mock(return_value=None)
    with patch.object(renderers, "HTMLRenderer", return_value=renderer_mock) as mock_renderer:
        profiler.open_in_browser()
        mock_get_last_session_or_fail.assert_called_once()
        mock_renderer.assert_called_once_with(timeline=False, resample_interval=None)
        renderer_mock.open_in_browser.assert_called_once_with("mocked_session")


@patch("pyinstrument.profiler.Profiler._get_last_session_or_fail")
def test_open_in_browser_with_timeline(mock_get_last_session_or_fail, profiler):
    mock_get_last_session_or_fail.return_value = "mocked_session"
    renderer_mock = Mock()
    renderer_mock.open_in_browser = Mock(return_value=None)
    with patch.object(renderers, "HTMLRenderer", return_value=renderer_mock) as mock_renderer:
        profiler.open_in_browser(timeline=True)
        mock_get_last_session_or_fail.assert_called_once()
        mock_renderer.assert_called_once_with(timeline=True, resample_interval=None)
        renderer_mock.open_in_browser.assert_called_once_with("mocked_session")


@patch("pyinstrument.profiler.Profiler._get_last_session_or_fail")
def test_open_in_browser_with_resample_interval(mock_get_last_session_or_fail, profiler):
    mock_get_last_session_or_fail.return_value = "mocked_session"
    renderer_mock = Mock()
    renderer_mock.open_in_browser = Mock(return_value=None)
    with patch.object(renderers, "HTMLRenderer", return_value=renderer_mock) as mock_renderer:
        profiler.open_in_browser(resample_interval=0.5)
        mock_get_last_session_or_fail.assert_called_once()
        mock_renderer.assert_called_once_with(timeline=False, resample_interval=0.5)
        renderer_mock.open_in_browser.assert_called_once_with("mocked_session")
