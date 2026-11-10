from pytest import raises
from circle import Circle
from rectangle import Rectangle

def test_valid_init():
    r1 = Rectangle(5, 5, 5, 5)
    assert r1.width == 5
    assert r1.height == 5
    assert r1.x == 5
    assert r1.y == 5

def test_valid_default_value_init():
    r1 = Rectangle(5, 5)
    assert r1.width == 5
    assert r1.height == 5
    assert r1.x == 0
    assert r1.y == 0

def test_invalid_width_height_init():
    with raises (TypeError):
        Rectangle("5", 5)
    with raises (TypeError):
        Rectangle(5, "5")
    with raises (TypeError):
        Rectangle(True, 5)
    with raises (TypeError):
        Rectangle(5, False)
    with raises (TypeError):
        Rectangle(5)
    with raises (ValueError):
        Rectangle(-5, 5)
    with raises (ValueError):
        Rectangle(5, -5)
    with raises (ValueError):
        Rectangle(0, 5)
    with raises (ValueError):
        Rectangle(5, 0)

def test_invalid_x_y_init():
    with raises (TypeError):
        Rectangle(5, 5, "5", 5)
    with raises (TypeError):
        Rectangle(5, 5, 5, "5")
    with raises (TypeError):
        Rectangle(5, 5, True, 5)
    with raises (TypeError):
        Rectangle(5, 5, 5, False)

def test_valid_area():
    r1 = Rectangle(5, 4)
    assert r1.area == 20

def test_read_only_area():
    r1 = Rectangle(5, 4)
    with raises (AttributeError):
        r1.area = 6

def test_valid_perimeter():
    r1 = Rectangle(5, 4)
    assert r1.perimeter == 18

def test_read_only_perimeter():
    r1 = Rectangle(5, 4)
    with raises(AttributeError):
        r1.perimeter = 6

def test_valid_translate():
    r1 = Rectangle(5, 5, 5, 5)
    r1.translate(5, 5)
    assert r1.x == 10
    assert r1.y == 10
    r1.translate(0.5, 0.5)
    assert r1.x == 10.5
    assert r1.y == 10.5

def test_invalid_translate():
    r1 = Rectangle(5, 5, 5, 5)
    with raises (TypeError):
        r1.translate("5", 5)
    with raises (TypeError):
        r1.translate(5, "5")
    with raises (TypeError):
        r1.translate(True, 5)
    with raises (TypeError):
        r1.translate(5, False)
    assert r1.x == 5
    assert r1.y == 5

def test_valid_change_width():
    r1 = Rectangle(5, 5)
    r1.width = 6
    assert r1.width == 6

def test_invalid_change_width():
    r1 = Rectangle(5, 5)
    with raises (TypeError):
        r1.width = "6"
    with raises (TypeError):
        r1.width = True
    with raises (ValueError):
        r1.width = -6
    assert r1.width == 5

def test_valid_change_height():
    r1 = Rectangle(5, 5)
    r1.height = 6
    assert r1.height == 6

def test_invalid_change_height():
    r1 = Rectangle(5, 5)
    with raises (TypeError):
        r1.height = "6"
    with raises (TypeError):
        r1.height = True
    with raises (ValueError):
        r1.height = -6
    assert r1.height == 5

def test_square():
    r1 = Rectangle(5, 5)
    r2 = Rectangle(5, 6)
    assert r1.square_or_not() == True
    assert r2.square_or_not() == False

def test_eq():
    r1 = Rectangle(5, 5, 5, 5)
    r2 = Rectangle(5, 5, 5, 6)
    r3 = Rectangle(5, 6, 5, 5)
    c1 = Circle(5)
    assert r1 == r2
    assert r1 != r3
    assert r1 != c1

def test_lt():
    r1 = Rectangle(5, 5)
    r2 = Rectangle(5, 4)
    r3 = Rectangle(4, 5)
    r4 = Rectangle(5, 5)
    assert r2 < r1
    assert r3 < r1
    assert not (r1 < r4)

def test_gt():
    r1 = Rectangle(5, 5)
    r2 = Rectangle(5, 6)
    r3 = Rectangle(6, 5)
    r4 = Rectangle(5, 5)
    assert r2 > r1
    assert r3 > r1
    assert not (r1 > r4)

def test_le():
    r1 = Rectangle(5, 5)
    r2 = Rectangle(5, 5)
    r3 = Rectangle(5, 4)
    r4 = Rectangle(4, 5)
    assert r1 <= r2
    assert r3 <= r1
    assert r4 <= r1
    assert not (r1 <= r3)

def test_ge():
    r1 = Rectangle(5, 5)
    r2 = Rectangle(5, 5)
    r3 = Rectangle(5, 6)
    r4 = Rectangle(6, 5)
    assert r1 >= r2
    assert r3 >= r1
    assert r4 >= r1
    assert not (r1 >= r3)

# Learned too late about @pytest.mark.parametrize, could probably be simplified using that.
# Deicided to stick with what I had since it would probably take longer to rewrite everything.