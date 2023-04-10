from functions.funcs_07 import print_from_dict

def test_func_07():
    result = print_from_dict(a=2,bb=24,cccc=222)
    assert result == {'bb':2, 'dddd': 4}

def test_func_07_without_data_in_dict():
    result = print_from_dict(a=2,cccc=222)
    assert result == {}
