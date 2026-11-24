# file: pyinstrument/stack_sampler.py:150-181
# asked: {"lines": [152, 153, 161, 165], "branches": [[151, 152], [160, 161], [164, 165], [172, 175]]}
# gained: {"lines": [152, 153, 161, 165], "branches": [[151, 152], [160, 161], [164, 165]]}

from unittest.mock import Mock, patch

import pytest

from pyinstrument.low_level.stat_profile import setstatprofile, walltime_coarse_resolution
from pyinstrument.low_level.types import TimerType
from pyinstrument.stack_sampler import StackSampler


def test_start_sampling_with_timing_thread_and_timer_func():
    sampler = StackSampler()
    sampler.timer_func = Mock()
    with pytest.raises(
        ValueError,
        match="Profiler requested to use the timing thread but this stack sampler is already using a custom timer function.",
    ):
        sampler._start_sampling(interval=1.0, use_timing_thread=True)


def test_start_sampling_with_timing_thread():
    sampler = StackSampler()
    with patch("pyinstrument.stack_sampler.setstatprofile") as mock_setstatprofile:
        sampler._start_sampling(interval=1.0, use_timing_thread=True)
        assert mock_setstatprofile.called
        _, kwargs = mock_setstatprofile.call_args
        assert kwargs["timer_type"] == "walltime_thread"


def test_start_sampling_with_coarse_resolution():
    sampler = StackSampler()
    with patch("pyinstrument.stack_sampler.walltime_coarse_resolution", return_value=0.5):
        with patch("pyinstrument.stack_sampler.setstatprofile") as mock_setstatprofile:
            sampler._start_sampling(interval=1.0, use_timing_thread=False)
            _, kwargs = mock_setstatprofile.call_args
            assert kwargs["timer_type"] == "walltime_coarse"


def test_start_sampling_with_last_profile_time_near_zero():
    sampler = StackSampler()
    sampler.last_profile_time = -0.000005
    with patch("pyinstrument.stack_sampler.setstatprofile") as mock_setstatprofile:
        with patch.object(sampler, "_timer", return_value=1.0):
            sampler._start_sampling(interval=1.0, use_timing_thread=False)
            assert sampler.last_profile_time == 1.0
