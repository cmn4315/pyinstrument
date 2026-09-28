# some tests for the renderer classes

from __future__ import annotations

import json
import os
import sys
import time
from unittest.mock import patch

import pytest

from pyinstrument import profiler, renderers, session
from pyinstrument.profiler import Profiler
from pyinstrument.renderers.base import Renderer
from pyinstrument.renderers.console import ConsoleRenderer
from pyinstrument.renderers.html import HTMLRenderer
from pyinstrument.renderers.session import SessionRenderer
from pyinstrument.session import Session

from .fake_time_util import fake_time

# utils

frame_renderer_classes: list[type[renderers.FrameRenderer]] = [
    renderers.ConsoleRenderer,
    renderers.JSONRenderer,
    renderers.PstatsRenderer,
    renderers.SpeedscopeRenderer,
]

parametrize_frame_renderer_class = pytest.mark.parametrize(
    "frame_renderer_class", frame_renderer_classes, ids=lambda c: c.__name__
)

# fixtures


def a():
    b()
    c()


def b():
    d()


def c():
    d()


def d():
    e()


def e():
    time.sleep(1)


@pytest.fixture(scope="module")
def profiler_session():
    with fake_time():
        profiler = Profiler()
        profiler.start()

        a()

        profiler.stop()
        return profiler.last_session


# tests


@parametrize_frame_renderer_class
def test_empty_profile(frame_renderer_class: type[renderers.FrameRenderer]):
    with Profiler() as profiler:
        pass
    profiler.output(renderer=frame_renderer_class())


@parametrize_frame_renderer_class
def test_timeline_doesnt_crash(
    profiler_session, frame_renderer_class: type[renderers.FrameRenderer]
):
    renderer = frame_renderer_class(timeline=True)
    renderer.render(profiler_session)


@parametrize_frame_renderer_class
def test_show_all_doesnt_crash(
    profiler_session, frame_renderer_class: type[renderers.FrameRenderer]
):
    renderer = frame_renderer_class(show_all=True)
    renderer.render(profiler_session)


@pytest.mark.parametrize("flat_time", ["self", "total"])
def test_console_renderer_flat_doesnt_crash(profiler_session, flat_time):
    renderer = renderers.ConsoleRenderer(flat=True, flat_time=flat_time)
    renderer.render(profiler_session)


def test_html_renderer_resampling(capsys):
    # create a session with more than 100,000 samples
    frame_records = []
    # first 100,000 frames have almost no time in them
    frame_records += [("<module>\x00somemodule/__init__.py\x0012", 1e-9)] * 100_000
    # last frame has some time in it
    frame_records += [("a\x00b\x001", 1)]

    session = Session(
        duration=1.0001,
        start_time=0,
        frame_records=frame_records,
        sample_count=len(frame_records),
        min_interval=1e-9,
        max_interval=1e-9,
        start_call_stack=["<module>\x00somemodule/__init__.py\x0012"],
        target_description="test",
        cpu_time=1.0001,
        sys_path=sys.path,
        sys_prefixes=[],
    )

    renderer = renderers.HTMLRenderer()
    with patch("pyinstrument.session.Session._resample_frame_records") as mock_resample:
        renderer.render(session)

    captured = capsys.readouterr()
    assert "Resampled to" in captured.err
    assert mock_resample.called


# Caleb Naeger - Added for SWEN 777
def test_session_renderer_renders_json(profiler_session):
    session_renderer = SessionRenderer()
    rendered = session_renderer.render(profiler_session)
    rendered = json.loads(rendered)
    assert rendered is not None
    assert "sample_count" in rendered
    assert rendered["sample_count"] == 2
    assert "start_call_stack" in rendered


def test_console_renderer_flat_xor_timeline():
    with pytest.raises(Renderer.MisconfigurationError, match="timeline and flat options together"):
        renderer = ConsoleRenderer(timeline=True, flat=True)


def test_console_renderer_percent_of_total_time(profiler_session):
    renderer = ConsoleRenderer(time="percent_of_total")
    result = renderer.render(profiler_session)
    # check that result shows the top level stack frame with 100% of the total time, and that there's a frame with 50%
    # of the time
    assert "100.0%" in result
    assert "50.0%" in result


def test_html_renderer_options_deprecated():
    with pytest.warns(DeprecationWarning, match="the show_all option is deprecated"):
        renderer = HTMLRenderer(show_all=True)
    with pytest.warns(DeprecationWarning, match="timeline is deprecated"):
        renderer = HTMLRenderer(timeline=True)


def test_html_renderer_open_in_browser(profiler_session):
    with patch("webbrowser.open") as mock_open:
        renderer = HTMLRenderer()
        renderer.open_in_browser(profiler_session, "tmp.html")

        # Assert webbrowser.open called with the correct URL
        mock_open.assert_called_once_with("file:tmp.html")
        # cleanup tmp.html
        os.remove("tmp.html")

        # reset the mock, so we can do the other branch
        mock_open.reset_mock()

        # cover the other branch -- no output file specified
        file = renderer.open_in_browser(profiler_session)
        mock_open.assert_called_once_with(f"file://{file}")
        os.remove(file)
