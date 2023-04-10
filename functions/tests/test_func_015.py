from functions.funcs_015 import palindrom

def test_palindrom_T():
    result = palindrom('assa')
    assert result == True
def test_palindrom_F():
    result = palindrom('assq')
    assert result == False