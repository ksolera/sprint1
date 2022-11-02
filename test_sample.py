import pytest

def sum(a,b):
    return 5

def test_sum():
    assert sum(4, 3) == 7