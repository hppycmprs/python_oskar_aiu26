from circle import Circle
from rectangle import Rectangle
import matplotlib.pyplot as plt
import matplotlib.patches as ptc


class Shape2Dplotter:
    """Class to plot 1 or more 2D-shapes in the same axes.
    """

    def shape2Dplotter(self, *args: Circle | Rectangle) -> None:
        """Method to plot 1 or more 2D-shapes in the same axes.

        Args:
            *args (Circle | Rectangle): The shapes to plot.

        Raises:
            ValueError: If no shapes are provided.
            TypeErrorr: If an object is not a Circle or Rectangle.
        """
        if len(args) == 0:
            raise ValueError("At least one shape is required")

        for shape in args:
            if not isinstance(shape, (Circle, Rectangle)):
                raise TypeError("Can only plot 2D-shapes")
            
        fig, ax = plt.subplots()

        for shape in args:
            if isinstance(shape, Circle):
                ax.add_patch(ptc.Circle((shape.x, shape.y), shape.radius))

            if isinstance(shape, Rectangle):
                lower_left_corner = (shape.x-(shape.width/2), shape.y-(shape.height/2)) # learnt from ChatGPT
                ax.add_patch(ptc.Rectangle(lower_left_corner, shape.width, shape.height))

        ax.autoscale_view() # learnt from ChatGPT
        ax.set_aspect('equal') # learnt from ChatGPT
        plt.show()