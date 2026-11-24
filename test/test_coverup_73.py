# file: pyinstrument/frame.py:315-332
# asked: {"lines": [319, 320, 323, 325, 326, 327, 330, 331, 332], "branches": [[319, 320], [319, 325], [330, 0], [330, 331], [331, 0], [331, 332]]}
# gained: {"lines": [319, 320, 323, 325, 326, 327], "branches": [[319, 320], [319, 325]]}

from unittest.mock import patch

import pytest

from pyinstrument.frame import Frame

SYNTHETIC_LEAF_IDENTIFIERS = {"synthetic_leaf"}


def test_self_check_synthetic_leaf():
    frame = Frame()
    frame.identifier = "synthetic_leaf"
    frame._children = []
    frame.time = 1.0
    frame.absorbed_time = 0.0

    with patch("pyinstrument.frame.SYNTHETIC_LEAF_IDENTIFIERS", new=SYNTHETIC_LEAF_IDENTIFIERS):
        frame.self_check()


def test_self_check_non_synthetic_leaf():
    frame = Frame()
    frame.identifier = "non_synthetic_leaf"
    frame._children = []
    frame.time = 1.0
    frame.absorbed_time = 0.0

    with patch("pyinstrument.frame.SYNTHETIC_LEAF_IDENTIFIERS", new=SYNTHETIC_LEAF_IDENTIFIERS):
        with pytest.raises(AssertionError):
            frame.self_check()


def test_self_check_time_mismatch():
    frame = Frame()
    frame.identifier = "non_synthetic_frame"
    frame._children = [Frame(), Frame()]
    frame._children[0].time = 0.5
    frame._children[1].time = 0.5
    frame.time = 1.1
    frame.absorbed_time = 0.0

    with patch("pyinstrument.frame.SYNTHETIC_LEAF_IDENTIFIERS", new=SYNTHETIC_LEAF_IDENTIFIERS):
        with pytest.raises(AssertionError):
            frame.self_check()


def test_self_check_recursive():
    frame = Frame()
    frame.identifier = "non_synthetic_frame"
    frame._children = [Frame(), Frame()]
    frame._children[0].time = 0.5
    frame._children[1].time = 0.5
    frame.time = 1.0
    frame.absorbed_time = 0.0

    with patch("pyinstrument.frame.SYNTHETIC_LEAF_IDENTIFIERS", new=SYNTHETIC_LEAF_IDENTIFIERS):
        with patch.object(Frame, "self_check") as mock_self_check:
            frame.self_check(recursive=True)
            mock_self_check.assert_any_call(recursive=True)
