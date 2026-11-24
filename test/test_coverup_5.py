# file: pyinstrument/magic/_utils.py:44-60
# asked: {"lines": [44, 53, 54, 55, 56, 58, 59, 60], "branches": [[53, 54], [53, 55], [55, 56], [55, 58]]}
# gained: {"lines": [44, 53, 54, 55, 56, 58, 59, 60], "branches": [[53, 54], [53, 55], [55, 56], [55, 58]]}

import ast
from ast import parse

import pytest

from pyinstrument.magic._utils import PrePostAstTransformer


def assert_transformer_properties(transformer, expected_pre, expected_post):
    assert isinstance(transformer.pre, list)
    assert isinstance(transformer.post, list)
    assert all(isinstance(node, ast.AST) for node in transformer.pre)
    assert all(isinstance(node, ast.AST) for node in transformer.post)
    assert [ast.dump(node) for node in transformer.pre] == [ast.dump(node) for node in expected_pre]
    assert [ast.dump(node) for node in transformer.post] == [
        ast.dump(node) for node in expected_post
    ]
    assert transformer.active is True


def test_pre_post_ast_transformer_with_string_pre():
    pre_str = "x = 1"
    post_str = "y = 2"
    transformer = PrePostAstTransformer(pre=pre_str, post=post_str)
    assert_transformer_properties(transformer, [parse(pre_str).body[0]], [parse(post_str).body[0]])


def test_pre_post_ast_transformer_with_ast_module_pre():
    pre_ast = parse("x = 1")
    post_ast = parse("y = 2")
    transformer = PrePostAstTransformer(pre=pre_ast, post=post_ast)
    assert_transformer_properties(transformer, pre_ast.body, post_ast.body)


def test_pre_post_ast_transformer_with_string_post():
    pre_str = "x = 1"
    post_str = "y = 2"
    transformer = PrePostAstTransformer(pre=pre_str, post=post_str)
    assert_transformer_properties(transformer, [parse(pre_str).body[0]], [parse(post_str).body[0]])


def test_pre_post_ast_transformer_with_ast_module_post():
    pre_ast = parse("x = 1")
    post_str = "y = 2"
    transformer = PrePostAstTransformer(pre=pre_ast, post=post_str)
    assert_transformer_properties(transformer, pre_ast.body, [parse(post_str).body[0]])
