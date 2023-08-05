from wheeldemoado.funcs import exp2, exp3


def test_funcs():
    assert exp2(5.0) == 32.0
    assert exp3(3.0) == 27.0
