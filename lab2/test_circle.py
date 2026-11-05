from pytest import raises, approx
from circle import Circle
from rectangle import Rectangle
import numpy as np

def test_valid_init():
    c = Circle(5, 5, 5)
    assert c.radius == 5
    assert c.x == 5
    assert c.y == 5

def test_valid_radius_init():
    c = Circle(5)
    assert c.radius == 5
    assert c.x == 0
    assert c.y == 0

def test_invalid_radius_init():
    with raises (TypeError):
        Circle("5")
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
    c = Circle(5)
    assert c.area == approx(5**2*np.pi) # approx function learnt from ChatGPT

#def test_read_only_area():
#    assert

def test_valid_perimeter():
    c = Circle(5)
    assert c.perimeter == approx(5*2*np.pi)

#def test_read_only_perimeter():
#    assert

#def test_translate():
#    assert

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