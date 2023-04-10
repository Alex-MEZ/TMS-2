from functions.funcs_011 import is_power_n


def test_is_power_n_T():
    result = is_power_n(9,3)
    assert result == True
def test_is_power_n_F():
    result = is_power_n(7,3)
    assert result == False