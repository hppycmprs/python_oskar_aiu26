import pytest
from shape2Dplotter import Shape2Dplotter
from circle import Circle
from rectangle import Rectangle
from sphere import Sphere


def test_no_shapes():
    plotter = Shape2Dplotter()
    with pytest.raises(ValueError):
        plotter.shape2Dplotter()

def test_valid_shapes():
    plotter = Shape2Dplotter()
    c1 = Circle(2)
    r1 = Rectangle(3, 4)

    assert plotter.shape2Dplotter(c1, r1) == None

def test_invalid_shape():
    plotter = Shape2Dplotter()
    s1 = Sphere(5)
    with pytest.raises(TypeError):
        plotter.shape2Dplotter(s1)