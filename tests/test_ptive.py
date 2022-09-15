import pytest
from ptive.pcore import Bety


def test_crossf():
    bety = Bety()
    assert round(bety.cross(), 2) == 1.52