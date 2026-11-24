# file: pyinstrument/profiler.py:258-295
# asked: {"lines": [264, 265, 266, 270, 271, 272, 274, 275, 276, 277, 278, 282, 283, 284, 286, 287, 288, 289, 290, 295], "branches": [[264, 265], [264, 269], [269, 274], [269, 281], [281, 286], [281, 295]]}
# gained: {"lines": [264, 265, 266, 270, 271, 272, 274, 275, 276, 277, 278, 282, 283, 284, 286, 287, 288, 289, 290, 295], "branches": [[264, 265], [264, 269], [269, 274], [269, 281], [281, 286], [281, 295]]}

from unittest.mock import MagicMock

import pytest

from pyinstrument.frame import AWAIT_FRAME_IDENTIFIER, OUT_OF_CONTEXT_FRAME_IDENTIFIER
from pyinstrument.profiler import Profiler
from pyinstrument.stack_sampler import AsyncState


def test_sampler_saw_call_stack_no_active_session():
    profiler = Profiler()
    profiler._active_session = None
    with pytest.raises(
        RuntimeError,
        match="Received a call stack without an active session. Please file an issue on pyinstrument Github describing how you made this happen!",
    ):
        profiler._sampler_saw_call_stack([], 0.1, None)


def test_sampler_saw_call_stack_async_out_of_context_awaited():
    profiler = Profiler()
    profiler._active_session = MagicMock()
    profiler._active_session.frame_records = []
    profiler._async_mode = "enabled"
    async_state = AsyncState("out_of_context_awaited", ["awaiting_coroutine"])
    profiler._sampler_saw_call_stack(["func1"], 0.1, async_state)
    assert profiler._active_session.frame_records[-1][0] == ["awaiting_coroutine"] + [
        AWAIT_FRAME_IDENTIFIER
    ]


def test_sampler_saw_call_stack_async_out_of_context_unknown():
    profiler = Profiler()
    profiler._active_session = MagicMock()
    profiler._active_session.frame_records = []
    profiler._async_mode = "strict"
    async_state = AsyncState("out_of_context_unknown", ["context_exit"])
    profiler._sampler_saw_call_stack(["func1"], 0.1, async_state)
    assert profiler._active_session.frame_records[-1][0] == ["context_exit"] + [
        OUT_OF_CONTEXT_FRAME_IDENTIFIER
    ]


def test_sampler_saw_call_stack_regular_sync_code():
    profiler = Profiler()
    profiler._active_session = MagicMock()
    profiler._active_session.frame_records = []
    profiler._sampler_saw_call_stack(["func1"], 0.1, None)
    assert profiler._active_session.frame_records[-1][0] == ["func1"]
