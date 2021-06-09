#!bin/usr/python3
"""
class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width mus be an integer")
        if type(height) is not int:
            raise TypeError("height must be an intger")
        if type(x) is not int:
            raise TypeError("x mus be an integer")
        if type(y) is not int:
            raise TypeError("y must be an intger")
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Getter of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter of x
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        Getter of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
       Setter of y
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Return the area value of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle
        """
        for i in range(self.__y):
            print()

        for row in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Update the class Rectangle by overriding
        the __str__ method
        """
        firts = "[" + self.__class__.__name__ + "] (" + str(self.id) + ") "
        sec = str(self.__x) + "/" + str(self.__y) + " - " + str(self.__width)

        if self.__class__.__name__ == 'Square':
            return firts + sec
        return firts + sec + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """
        update of the class rectangle
        """
        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
        else:
            if len(args) < 1:
                return
            self.id = args[0]
            if len(args) < 2:
                return
            self.__width = args[1]
            if len(args) < 3:
                return
            self.__height = args[2]
            if len(args) < 4:
                return
            self.__x = args[3]
            if len(args) < 5:
                return
            self.__y = args[4]

    def to_dictionary(self):
        """
        Rectangle to Dictionary
        """
        dictionary = {}
        dictionary.setdefault('id', self.id)
        dictionary.setdefault('width', self.__width)
        dictionary.setdefault('height', self.__height)
        dictionary.setdefault('x', self.__x)
        dictionary.setdefault('y', self.__y)
        return dictionary
