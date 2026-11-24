# file: pyinstrument/frame.py:304-306
# asked: {"lines": [304, 305, 306], "branches": []}
# gained: {"lines": [304, 305, 306], "branches": []}

import pytest

from pyinstrument.frame import Frame
from pyinstrument.frame_info import ATTRIBUTE_MARKER_CLASS_NAME


def test_frame_class_name_property():
    frame = Frame()
    frame.get_attribute_value = lambda attr: (
        "TestClassName" if attr == ATTRIBUTE_MARKER_CLASS_NAME else None
    )

    assert frame.class_name == "TestClassName"


def test_frame_class_name_property_none():
    frame = Frame()
    frame.get_attribute_value = lambda attr: (
        None if attr == ATTRIBUTE_MARKER_CLASS_NAME else "SomeValue"
    )

    assert frame.class_name is None
