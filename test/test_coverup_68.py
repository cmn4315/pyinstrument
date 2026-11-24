# file: pyinstrument/stack_sampler.py:129-148
# asked: {"lines": [], "branches": [[145, 0]]}
# gained: {"lines": [], "branches": [[145, 0]]}

import pytest

from pyinstrument.stack_sampler import StackSampler


def test_update_with_different_interval(monkeypatch):
    class MockSubscriber:
        def __init__(self, desired_interval, use_timing_thread=None):
            self.desired_interval = desired_interval
            self.use_timing_thread = use_timing_thread

    sampler = StackSampler()
    sampler.current_sampling_interval = 10
    sampler.subscribers = [MockSubscriber(5)]

    def mock_start_sampling(self, interval, use_timing_thread):
        assert interval == 5
        assert use_timing_thread is False

    monkeypatch.setattr(StackSampler, "_start_sampling", mock_start_sampling)

    sampler._update()


def test_update_with_same_interval(monkeypatch):
    class MockSubscriber:
        def __init__(self, desired_interval, use_timing_thread=None):
            self.desired_interval = desired_interval
            self.use_timing_thread = use_timing_thread

    sampler = StackSampler()
    sampler.current_sampling_interval = 5
    sampler.subscribers = [MockSubscriber(5)]

    def mock_start_sampling(self, interval, use_timing_thread):
        pytest.fail("_start_sampling should not be called")

    monkeypatch.setattr(StackSampler, "_start_sampling", mock_start_sampling)

    sampler._update()
