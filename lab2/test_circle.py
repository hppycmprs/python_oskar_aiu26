from pytest import raises
from circle import Circle

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

def test_area():
    assert 

def test_perimeter():
    assert

def test_translate():
    assert

def test_eq():
    assert

def test_lt():
    assert

def test_gt():
    assert

def test_le():
    assert

def test_ge():
    assert