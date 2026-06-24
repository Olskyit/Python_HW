from calculator import Calculator

calc = Calculator()


def test_sum():
    assert calc.sum(4, 5) == 9


def test_sub():
    assert calc.sub(10, 3) == 7


def test_mul():
    assert calc.mul(3, 3) == 9


def test_div():
    assert calc.div(10, 2) == 5


def test_pow():
    assert calc.pow(2, 3) == 8


def test_avg():
    assert calc.avg([1, 2, 3]) == 2.0
