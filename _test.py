import pytest

def square(n):
    return n * n

def cube(n):
    return n * n * n

def fifth(n):
    return n * n * n * n * n

def test_square():
    assert square(5) == 25, "Test failed"
    assert square(3)==9, "Test failed"

def test_cube():
    assert cube(5) == 125, "Test failed"
    assert cube(3) == 27, "Test failed"

def test_fifth():
    assert fifth(5) == 3125, "Test failed"
    assert fifth(3) == 243, "Test failed"

def test_invalid():
    with pytest.raises(TypeError):
        square("string")