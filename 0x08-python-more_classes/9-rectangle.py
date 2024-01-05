#!/usr/bin/python3
"""9-rectangle.py"""


class Rectangle:
    """Class Rectangle that defines a rectangle.
    Args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This is the width, using getter and setter.
        Args:
            value(int): the value for the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if (
                type(value) is not int or value is None
                ):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This is the height, using getter and setter.
        Args:
            value(int): the value for the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if (
                type(value) is not int or value is None
                ):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter.
        Args:
        rectangle_p(int): the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            rectangle_p = 0
        else:
            rectangle_p = (2 * self.__width) + (2 * self.__height)

        return rectangle_p

    def __str__(self):
        """should print the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height):
                result += str(self.print_symbol) * self.__width

                if i < self.__height - 1:
                    result += "\n"

            return result

    def __repr__(self):
        """repr() should return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""
        return cls(size, size)
