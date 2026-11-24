# file: pyinstrument/low_level/pyi_timing_thread_python.py:21-24
# asked: {"lines": [23], "branches": [[22, 23]]}
# gained: {"lines": [23], "branches": [[22, 23]]}

from unittest.mock import patch

from pyinstrument.low_level.pyi_timing_thread_python import get_interval


def test_get_interval_with_subscribers():
    class Subscriber:
        def __init__(self, interval):
            self.interval = interval

    subscribers = [Subscriber(10), Subscriber(20), Subscriber(5)]
    with patch("pyinstrument.low_level.pyi_timing_thread_python.subscribers", subscribers):
        result = get_interval(30)
        assert result == 5, "The minimum interval among subscribers should be returned"


def test_get_interval_without_subscribers():
    with patch("pyinstrument.low_level.pyi_timing_thread_python.subscribers", []):
        result = get_interval(30)
        assert result == 30, "The max_interval should be returned when there are no subscribers"
