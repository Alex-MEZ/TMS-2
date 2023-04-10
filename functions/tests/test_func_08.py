from functions.funcs_08 import avg_arifm, avg_geom


def test_avg_arifm():
    result = avg_arifm(3, 3, 3)
    assert result == 3


def test_avg_geom():
    result = avg_geom(2, 2, 2)
    assert result == 2


def test_avg_result():
    result = avg_result(2, 2, 2, mean_type=1)
    assert result == 2


def test_avg_result_arifm():
    result = avg_result_arifm(2, 2, 2, mean_type=0)
    assert result == 3
