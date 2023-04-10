from functions.funcs_09 import counter_numbers_in_list

def test_counter_numbers_in_list():
    result = counter_numbers_in_list([1,2,3,1,2,5,5,2,1,1,2,])
    assert result == {1,2,5,3}