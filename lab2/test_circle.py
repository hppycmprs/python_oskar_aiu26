from pytest import raises, approx
from circle import Circle
from rectangle import Rectangle
import numpy as np

def test_valid_init():
    c1 = Circle(5, 5, 5)
    assert c1.radius == 5
    assert c1.x == 5
    assert c1.y == 5

def test_valid_default_value_init():
    c1 = Circle(5)
    assert c1.radius == 5
    assert c1.x == 0
    assert c1.y == 0

def test_invalid_radius_init():
    with raises (TypeError):
        Circle("5")
    with raises (TypeError):
        Circle(True)
    with raises (ValueError):
        Circle(-5)
    with raises (ValueError):
        Circle(0)

def test_invalid_x_y_init():
    with raises (TypeError):
        Circle(5, "5", 5)
    with raises (TypeError):
        Circle(5, 5, "5")
    with raises (TypeError):
        Circle(5, True, 5)
    with raises (TypeError):
        Circle(5, 5, False)

def test_valid_area():
    c1 = Circle(5)
    assert c1.area == approx(5**2*np.pi) # approx function learnt from ChatGPT

def test_read_only_area():
    c1 = Circle(5, 5)
    with raises (AttributeError):
        c1.area = 6

def test_valid_perimeter():
    c1 = Circle(5)
    assert c1.perimeter == approx(5*2*np.pi)

def test_read_only_perimeter():
    c1 = Circle(5, 5, 5)
    with raises(AttributeError):
        c1.perimeter = 6

def test_valid_translate():
    c1 = Circle(5, 5, 5)
    c1.translate(5, 5)
    assert c1.x == 10
    assert c1.y == 10
    c1.translate(0.5, 0.5)
    assert c1.x == 10.5
    assert c1.y == 10.5

def test_invalid_translate():
    c1 = Circle(5, 5, 5)
    with raises (TypeError):
        c1.translate("5", 5)
    with raises (TypeError):
        c1.translate(5, "5")
    with raises (TypeError):
        c1.translate(True, 5)
    with raises (TypeError):
        c1.translate(5, False)
    assert c1.x == 5
    assert c1.y == 5

def test_valid_change_radius():
    c1 = Circle(5)
    c1.radius = 6
    assert c1.radius == 6

def test_invalid_change_radius():
    c1 = Circle(5)
    with raises (TypeError):
        c1.radius = "5"
    with raises (TypeError):
        c1.radius = True
    with raises (ValueError):
        c1.radius = -5
    assert c1.radius == 5

def test_unit_circle():
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1.unit_circle_or_not() == True
    assert c2.unit_circle_or_not() == False

def test_eq():
    c1 = Circle(5, 5, 5)
    c2 = Circle(5, 5, 6)
    c3 = Circle(6)
    r1 = Rectangle(5, 5, 5, 5)
    assert c1 == c2
    assert c1 != c3
    assert c1 != r1

def test_lt():
    c1 = Circle(5)
    c2 = Circle(6)
    c3 = Circle(5)
    assert c1 < c2
    assert not (c1 < c3)

def test_gt():
    c1 = Circle(5)
    c2 = Circle(6)
    c3 = Circle(5)
    assert c2 > c1
    assert not (c1 > c3)

def test_le():
    c1 = Circle(5)
    c2 = Circle(5)
    c3 = Circle(4)
    assert c1 <= c2
    assert c3 <= c1
    assert not (c1 <= c3)

def test_ge():
    c1 = Circle(5)
    c2 = Circle(5)
    c3 = Circle(6)
    assert c1 >= c2
    assert c3 >= c1
    assert not (c1 >= c3)