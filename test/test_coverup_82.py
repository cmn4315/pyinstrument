# file: pyinstrument/magic/_utils.py:44-60
# asked: {"lines": [54, 56], "branches": [[53, 54], [55, 56]]}
# gained: {"lines": [54, 56], "branches": [[53, 54], [55, 56]]}

from ast import parse

import pytest

from pyinstrument.magic._utils import PrePostAstTransformer


def test_pre_is_string():
    pre = "def func(): pass"
    post = parse("def post_func(): pass")
    transformer = PrePostAstTransformer(pre, post)
    assert isinstance(transformer.pre, list)
    assert len(transformer.pre) > 0


def test_post_is_string():
    pre = parse("def pre_func(): pass")
    post = "def func(): pass"
    transformer = PrePostAstTransformer(pre, post)
    assert isinstance(transformer.post, list)
    assert len(transformer.post) > 0


def test_both_are_strings():
    pre = "def pre_func(): pass"
    post = "def post_func(): pass"
    transformer = PrePostAstTransformer(pre, post)
    assert isinstance(transformer.pre, list)
    assert len(transformer.pre) > 0
    assert isinstance(transformer.post, list)
    assert len(transformer.post) > 0
