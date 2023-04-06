def summ(a, b):
    return a + b


def test_summ():
    result = summ(2, 5)
    assert result == 7


def test_summ_2():
    result = summ(8, 5)
    assert result == 13