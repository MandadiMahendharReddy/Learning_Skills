# test_calculator_pytest.py
import pytest
from calculator1 import add, divide

def test_add():
    assert add(3, 4) == 7
    assert add(-5, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
