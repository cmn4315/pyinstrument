# file: pyinstrument/frame_info.py:30-40
# asked: {"lines": [30, 34, 36, 38, 40], "branches": [[36, 38], [36, 40]]}
# gained: {"lines": [30, 34, 36, 38, 40], "branches": [[36, 38], [36, 40]]}

import pytest

from pyinstrument.frame_info import ATTRIBUTES_SEP


@pytest.fixture
def frame_info_get_identifier():
    from pyinstrument.frame_info import frame_info_get_identifier

    return frame_info_get_identifier


def test_frame_info_get_identifier_no_attributes(frame_info_get_identifier):
    # Test when there are no attributes in the frame_info string
    frame_info = "some_frame_info"
    result = frame_info_get_identifier(frame_info)
    assert result == frame_info, (
        "The function should return the input string when there are no attributes."
    )


def test_frame_info_get_identifier_with_attributes(frame_info_get_identifier):
    # Test when there are attributes in the frame_info string
    frame_info = "some_frame_info" + ATTRIBUTES_SEP + "some_attributes"
    expected_result = "some_frame_info"
    result = frame_info_get_identifier(frame_info)
    assert result == expected_result, (
        "The function should return the part of the string before the first occurrence of ATTRIBUTES_SEP."
    )
