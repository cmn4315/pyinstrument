# file: pyinstrument/stack_sampler.py:337-353
# asked: {"lines": [337, 338, 339, 353], "branches": []}
# gained: {"lines": [337, 338, 339, 353], "branches": []}

import pytest

from pyinstrument.stack_sampler import AsyncState


def test_async_state_in_context():
    state = AsyncState(state="in_context", info=None)
    assert state.state == "in_context"
    assert state.info is None


def test_async_state_out_of_context_awaited():
    state = AsyncState(state="out_of_context_awaited", info=["stack", "trace"])
    assert state.state == "out_of_context_awaited"
    assert state.info == ["stack", "trace"]


def test_async_state_out_of_context_unknown():
    state = AsyncState(state="out_of_context_unknown", info=["stack", "trace"])
    assert state.state == "out_of_context_unknown"
    assert state.info == ["stack", "trace"]
