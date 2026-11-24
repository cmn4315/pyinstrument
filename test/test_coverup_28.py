# file: pyinstrument/frame.py:46-49
# asked: {"lines": [46, 47, 48, 49], "branches": []}
# gained: {"lines": [46, 47, 48, 49], "branches": []}

from typing import Sequence

import pytest

from pyinstrument.frame import FrameContext


def test_frame_context_shorten_path():
    class TestFrameContext(FrameContext):
        def shorten_path(self, path: str) -> str:
            return path[:10]  # Example implementation

        def sys_prefixes(self) -> Sequence[str]:
            return ["prefix1", "prefix2"]  # Example implementation

    context = TestFrameContext()
    assert context.shorten_path("test_path") == "test_path"[:10]


def test_frame_context_sys_prefixes():
    class TestFrameContext(FrameContext):
        def shorten_path(self, path: str) -> str:
            return path[:10]  # Example implementation

        def sys_prefixes(self) -> Sequence[str]:
            return ["prefix1", "prefix2"]  # Example implementation

    context = TestFrameContext()
    assert context.sys_prefixes() == ["prefix1", "prefix2"]
