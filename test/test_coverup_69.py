# file: pyinstrument/renderers/speedscope.py:144-207
# asked: {"lines": [164, 165, 169, 170, 171, 175, 176, 177, 181, 182, 198, 199, 201, 204, 205, 207], "branches": [[164, 165], [164, 169], [170, 171], [170, 175], [181, 182], [181, 198], [199, 201], [199, 204]]}
# gained: {"lines": [164, 165, 169, 170, 171, 175, 176, 177, 181, 182, 198, 199, 201, 204, 205, 207], "branches": [[164, 165], [164, 169], [170, 171], [170, 175], [181, 182], [181, 198], [199, 201], [199, 204]]}

from unittest.mock import Mock

import pytest

from pyinstrument.frame import Frame
from pyinstrument.renderers.speedscope import (
    SpeedscopeEvent,
    SpeedscopeEventType,
    SpeedscopeFrame,
    SpeedscopeRenderer,
)


def test_render_frame_none():
    renderer = SpeedscopeRenderer()
    result = renderer.render_frame(None)
    assert result == []


def test_render_frame_new_frame():
    renderer = SpeedscopeRenderer()
    frame = Mock(spec=Frame)
    frame.function = "test_function"
    frame.file_path = "test_file.py"
    frame.line_no = 10
    frame.children = []
    frame.absorbed_time = 1.0
    frame.is_synthetic_leaf = False
    frame.time = 0.0

    result = renderer.render_frame(frame)
    assert len(result) == 2
    assert isinstance(result[0], SpeedscopeEvent)
    assert result[0].type == SpeedscopeEventType.OPEN
    assert isinstance(result[1], SpeedscopeEvent)
    assert result[1].type == SpeedscopeEventType.CLOSE


def test_render_frame_existing_frame():
    renderer = SpeedscopeRenderer()
    frame = Mock(spec=Frame)
    frame.function = "test_function"
    frame.file_path = "test_file.py"
    frame.line_no = 10
    frame.children = []
    frame.absorbed_time = 1.0
    frame.is_synthetic_leaf = False
    frame.time = 0.0

    sframe = SpeedscopeFrame(frame.function, frame.file_path, frame.line_no)
    renderer._frame_to_index[sframe] = 0

    result = renderer.render_frame(frame)
    assert len(result) == 2
    assert isinstance(result[0], SpeedscopeEvent)
    assert result[0].type == SpeedscopeEventType.OPEN
    assert isinstance(result[1], SpeedscopeEvent)
    assert result[1].type == SpeedscopeEventType.CLOSE


def test_render_frame_with_children():
    renderer = SpeedscopeRenderer()
    frame = Mock(spec=Frame)
    frame.function = "test_function"
    frame.file_path = "test_file.py"
    frame.line_no = 10
    frame.children = [Mock(spec=Frame), Mock(spec=Frame)]
    frame.absorbed_time = 1.0
    frame.is_synthetic_leaf = False
    frame.time = 0.0

    for child in frame.children:
        child.function = "child_function"
        child.file_path = "child_file.py"
        child.line_no = 20
        child.children = []
        child.absorbed_time = 0.5
        child.is_synthetic_leaf = False
        child.time = 0.0

    result = renderer.render_frame(frame)
    assert len(result) == 6
    assert isinstance(result[0], SpeedscopeEvent)
    assert result[0].type == SpeedscopeEventType.OPEN
    assert isinstance(result[5], SpeedscopeEvent)
    assert result[5].type == SpeedscopeEventType.CLOSE


def test_render_frame_synthetic_leaf():
    renderer = SpeedscopeRenderer()
    frame = Mock(spec=Frame)
    frame.function = "test_function"
    frame.file_path = "test_file.py"
    frame.line_no = 10
    frame.children = []
    frame.absorbed_time = 1.0
    frame.is_synthetic_leaf = True
    frame.time = 2.0

    result = renderer.render_frame(frame)
    assert len(result) == 2
    assert isinstance(result[0], SpeedscopeEvent)
    assert result[0].type == SpeedscopeEventType.OPEN
    assert isinstance(result[1], SpeedscopeEvent)
    assert result[1].type == SpeedscopeEventType.CLOSE
