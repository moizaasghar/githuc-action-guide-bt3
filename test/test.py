import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from src.cal import calculator

@pytest.fixture
def calc():
    return calculator()

def test_add(calc):
    assert calc.add(5,3) == 8

def test_sub(calc):
    assert calc.sub(5,3) == 2

def test_mul(calc):
    assert calc.mul(5,3) == 15

def test_divide(calc):
    assert calc.divide(6,0) == "I can't divide it with zero"