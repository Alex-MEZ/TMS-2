from functions.funcs_03 import factorial

def test_factorial():
    result = factorial(3)
    assert 6 == result