from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube
from utils import validate_positive_value, validate_type
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

class Shape2Dplotter:
    def shape2Dplotter(self, *args):
        fig, ax = plt.subplots()
        for shape in args:
            if isinstance(shape, Circle):
                ax.add_patch(ptc.Circle((shape.x, shape.y), (shape.radius)))
            if isinstance(shape, Rectangle):
                lower_left_corner = (shape.x-(shape.width/2), shape.y-(shape.height/2))
                ax.add_patch(ptc.Rectangle(lower_left_corner, shape.width, shape.height))