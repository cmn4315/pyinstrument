# file: pyinstrument/magic/magic.py:54-84
# asked: {"lines": [55, 56, 59, 60, 61, 63, 67, 68, 70, 72, 73, 74, 76], "branches": [[55, 56], [55, 70]]}
# gained: {"lines": [55, 56, 59, 60, 61, 63, 67, 68, 70, 72, 73, 74, 76], "branches": [[55, 56], [55, 70]]}

import pytest
from IPython import get_ipython

from pyinstrument.magic.magic import PyinstrumentMagic


@pytest.fixture
def pyinstrument_magic():
    ip = get_ipython()
    magic = PyinstrumentMagic(shell=ip)
    yield magic


def test_recreate_transformer_pre_post_ast_transformer(pyinstrument_magic, monkeypatch):
    import IPython

    monkeypatch.setattr(IPython, "version_info", (8, 14))
    pyinstrument_magic.recreate_transformer("test_description")
    assert isinstance(pyinstrument_magic._transformer, type(pyinstrument_magic._transformer))


def test_recreate_transformer_replace_code_transformer(pyinstrument_magic, monkeypatch):
    import IPython

    monkeypatch.setattr(IPython, "version_info", (8, 15))
    pyinstrument_magic.recreate_transformer("test_description")
    assert isinstance(pyinstrument_magic._transformer, type(pyinstrument_magic._transformer))
