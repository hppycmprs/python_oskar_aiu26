from sphere import Sphere
from cube import Cube
from pytest import raises, approx
import numpy as np

def test_valid_init() -> None:
    s1 = Sphere(5, 5, 5, 5)
    assert s1.radius == 5
    assert s1.x == 5
    assert s1.y == 5
    assert s1.z == 5

def test_valid_default_value_init() -> None:
    s1 = Sphere(5)
    assert s1.radius == 5
    assert s1.x == 0
    assert s1.y == 0
    assert s1.z == 0

def test_invalid_radius_init() -> None:
    with raises (TypeError):
        Sphere("5")
    with raises (TypeError):
        Sphere(True) # since bool is subclass of int
    with raises (ValueError):
        Sphere(-5)
    with raises (ValueError):
        Sphere(0)

def test_invalid_x_y_z_init() -> None:
    with raises (TypeError):
        Sphere(5, "5", 5, 5)
    with raises (TypeError):
        Sphere(5, 5, "5", 5)
    with raises (TypeError):
        Sphere(5, 5, 5, "5")
    with raises (TypeError):
        Sphere(5, True, 5, 5)
    with raises (TypeError):
        Sphere(5, 5, False, 5)
    with raises (TypeError):
        Sphere(5, 5, 5, True)

def test_valid_volume() -> None:
    s1 = Sphere(5)
    assert s1.volume == approx(((4*np.pi)*(5**3))/3)

def test_read_only_volume() -> None:
    s1 = Sphere(5)
    with raises (AttributeError):
        s1.volume = 6

def test_valid_surface_area() -> None:
    s1 = Sphere(5)
    assert s1.surface_area == approx((4*np.pi)*(5**2))

def test_read_only_surface_area() -> None:
    s1 = Sphere(5)
    with raises(AttributeError):
        s1.surface_area = 6

def test_valid_translate() -> None:
    s1 = Sphere(5, 5, 5, 5)
    s1.translate(5, 5, 5)
    assert s1.x == 10
    assert s1.y == 10
    assert s1.z == 10
    s1.translate(0.5, 0.5, 0.5) # asserts that float is also valid
    assert s1.x == 10.5
    assert s1.y == 10.5
    assert s1.z == 10.5

def test_invalid_translate() -> None:
    s1 = Sphere(5, 5, 5, 5)
    with raises (TypeError):
        s1.translate("5", 5, 5)
    with raises (TypeError):
        s1.translate(5, "5", 5)
    with raises (TypeError):
        s1.translate(5, 5, "5")
    with raises (TypeError):
        s1.translate(True, 5, 5)
    with raises (TypeError):
        s1.translate(5, False, 5)
    with raises (TypeError):
        s1.translate(5, 5, True)
    assert s1.x == 5 # asserts that x y and z stay unaltered after invalid translate
    assert s1.y == 5
    assert s1.z == 5

def test_valid_change_radius() -> None:
    s1 = Sphere(5)
    s1.radius = 6
    assert s1.radius == 6

def test_invalid_change_radius() -> None:
    s1 = Sphere(5)
    with raises (TypeError):
        s1.radius = "6"
    with raises (TypeError):
        s1.radius = True
    with raises (ValueError):
        s1.radius = -6
    assert s1.radius == 5 # asserts that radius stays unaltered after invalid change

def test_unit_sphere_or_not() -> None:
    s1 = Sphere(1)
    s2 = Sphere(2)
    s3 = Sphere(1, 1, 1)
    assert s1.unit_sphere_or_not() == True
    assert s2.unit_sphere_or_not() == False
    assert s3.unit_sphere_or_not() == False

def test_eq() -> None:
    s1 = Sphere(5, 5, 5, 5)
    s2 = Sphere(5, 5, 5, 6)
    s3 = Sphere(6, 5, 5, 5)
    cu1 = Cube(5)
    assert s1 == s2
    assert s1 != s3
    assert s1 != cu1

def test_lt() -> None:
    s1 = Sphere(5)
    s2 = Sphere(4)
    assert s2 < s1
    assert not (s1 < s2)

def test_gt() -> None:
    s1 = Sphere(4)
    s2 = Sphere(5)
    assert s2 > s1
    assert not (s1 > s2)

def test_le() -> None:
    s1 = Sphere(5)
    s2 = Sphere(5)
    s3 = Sphere(4)
    assert s1 <= s2
    assert s3 <= s1
    assert not (s1 <= s3)

def test_ge() -> None:
    s1 = Sphere(5)
    s2 = Sphere(5)
    s3 = Sphere(6)
    assert s1 >= s2
    assert s3 >= s1
    assert not (s1 >= s3)