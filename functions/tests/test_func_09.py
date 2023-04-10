from functions.funcs_09 import schet, schet_2


def test_schet():
    result = counter_numbers_in_list([1, 2, 3, 1, 2, 5, 5, 2, 1, 1, 2, ])
    assert result == {1, 2, 5, 3}
