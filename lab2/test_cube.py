from sphere import Sphere
from cube import Cube
from pytest import raises

def test_valid_init() -> None:
    cu1 = Cube(5, 5, 5, 5)
    assert cu1.side_length == 5
    assert cu1.x == 5
    assert cu1.y == 5
    assert cu1.z == 5

def test_valid_default_value_init() -> None:
    cu1 = Cube(5)
    assert cu1.side_length == 5
    assert cu1.x == 0
    assert cu1.y == 0
    assert cu1.z == 0

def test_invalid_side_length_init() -> None:
    with raises (TypeError):
        Cube("5")
    with raises (TypeError):
        Cube(True) # since bool is subclass of int
    with raises (ValueError):
        Cube(-5)
    with raises (ValueError):
        Cube(0)

def test_invalid_x_y_z_init() -> None:
    with raises (TypeError):
        Cube(5, "5", 5, 5)
    with raises (TypeError):
        Cube(5, 5, "5", 5)
    with raises (TypeError):
        Cube(5, 5, 5, "5")
    with raises (TypeError):
        Cube(5, True, 5, 5)
    with raises (TypeError):
        Cube(5, 5, False, 5)
    with raises (TypeError):
        Cube(5, 5, 5, True)

def test_valid_volume() -> None:
    cu1 = Cube(5)
    assert cu1.volume == 125

def test_read_only_volume() -> None:
    cu1 = Cube(5)
    with raises (AttributeError):
        cu1.volume = 6

def test_valid_surface_area() -> None:
    cu1 = Cube(5)
    assert cu1.surface_area == 150

def test_read_only_surface_area() -> None:
    cu1 = Cube(5)
    with raises(AttributeError):
        cu1.surface_area = 6

def test_valid_translate() -> None:
    cu1 = Cube(5, 5, 5, 5)
    cu1.translate(5, 5, 5)
    assert cu1.x == 10
    assert cu1.y == 10
    assert cu1.z == 10
    cu1.translate(0.5, 0.5, 0.5) # asserts that float is also valid
    assert cu1.x == 10.5
    assert cu1.y == 10.5
    assert cu1.z == 10.5

def test_invalid_translate() -> None:
    cu1 = Cube(5, 5, 5, 5)
    with raises (TypeError):
        cu1.translate("5", 5, 5)
    with raises (TypeError):
        cu1.translate(5, "5", 5)
    with raises (TypeError):
        cu1.translate(5, 5, "5")
    with raises (TypeError):
        cu1.translate(True, 5, 5)
    with raises (TypeError):
        cu1.translate(5, False, 5)
    with raises (TypeError):
        cu1.translate(5, 5, True)
    assert cu1.x == 5 # asserts that x y and z stay unaltered after invalid translate
    assert cu1.y == 5
    assert cu1.z == 5

def test_valid_change_side_length() -> None:
    cu1 = Cube(5)
    cu1.side_length = 6
    assert cu1.side_length == 6

def test_invalid_change_side_length() -> None:
    cu1 = Cube(5)
    with raises (TypeError):
        cu1.side_length = "6"
    with raises (TypeError):
        cu1.side_length = True
    with raises (ValueError):
        cu1.side_length = -6
    assert cu1.side_length == 5 # asserts that side_length stays unaltered after invalid change

def test_unit_cube_or_not() -> None:
    cu1 = Cube(1)
    cu2 = Cube(2)
    assert cu1.unit_cube_or_not() == True
    assert cu2.unit_cube_or_not() == False

def test_eq() -> None:
    cu1 = Cube(5, 5, 5, 5)
    cu2 = Cube(5, 5, 5, 6)
    cu3 = Cube(6, 5, 5, 5)
    s1 = Sphere(5)
    assert cu1 == cu2
    assert cu1 != cu3
    assert cu1 != s1

def test_lt() -> None:
    cu1 = Cube(5)
    cu2 = Cube(4)
    assert cu2 < cu1
    assert not (cu1 < cu2)

def test_gt() -> None:
    cu1 = Cube(4)
    cu2 = Cube(5)
    assert cu2 > cu1
    assert not (cu1 > cu2)

def test_le() -> None:
    cu1 = Cube(5)
    cu2 = Cube(5)
    cu3 = Cube(4)
    assert cu1 <= cu2
    assert cu3 <= cu1
    assert not (cu1 <= cu3)

def test_ge() -> None:
    cu1 = Cube(5)
    cu2 = Cube(5)
    cu3 = Cube(6)
    assert cu1 >= cu2
    assert cu3 >= cu1
    assert not (cu1 >= cu3)