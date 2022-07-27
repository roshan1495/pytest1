from src.calc import add, sub, mul

def test_add_func():
    assert add(1,2) == 3
    assert add(3,4) == 7

def test_sub_func():
    assert sub(1,2) == 1
    assert sub(1,10) != 8

# def test_mul_func():
#     assert mul(1,2) == 2