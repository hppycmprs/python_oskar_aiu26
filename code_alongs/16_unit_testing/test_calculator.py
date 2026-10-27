from calculator import Calculator

calc = Calculator()

def test_add():
    num1 = 5
    num2 = 3
    assert calc.add(num1,num2) == num1+num2

def test_add_negative():
    num1 = -5
    num2 = -3
    assert calc.add(num1, num2) == num1+num2

def test_multiply():
    num1 = 4
    num2 = 4
    assert calc.mul(num1, num2) == num1*num2