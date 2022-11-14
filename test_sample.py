import pytest
from main import fibonacci

def test_fibonacci_1_is_1():
    assert fibonacci(1) == 1

def test_fibonacci_9_is_34():
    assert fibonacci(9) == 34

def test_fibonacci_negative_raise_exception():
    with pytest.raises(ValueError):
        fibonacci(-10)
