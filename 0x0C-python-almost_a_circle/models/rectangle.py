#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor initializes a rectangle with dimensions, postions & id
        '''
        super().__init__(id)

        ''' calls the validation function '''
        self.valid_setter(width, 'width')
        self.valid_setter(height, 'height')
        self.valid_setter(x, 'x')
        self.valid_setter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        ''' retrieves the value of the private attr '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        sets the value of the private attr
        and calls the validation function
        '''

        self.valid_setter(value, 'width')
        self.__width = value

    @property
    def height(self):
        ''' retrieves the value of the private attr '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        sets the value of the private attr
        and calls the validation function
        '''

        self.valid_setter(value, 'height')
        self.__height = value

    @property
    def x(self):
        ''' retrieves the value of the private attr '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        sets the value of the private attr
        and calls the validation function
        '''

        self.valid_setter(value, 'x')
        self.__x = value

    @property
    def y(self):
        ''' retrieves the value of the private attr '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        sets the value of the private attr
        and calls the validation function
        '''

        self.valid_setter(value, 'y')
        self.__y = value

    def valid_setter(self, value, attr):
        ''' method that adds validation of attr '''
        if not isinstance(value, int):
            raise TypeError(f'{attr} must be an integer')

        if value <= 0 and attr in ('width', 'height'):
            raise ValueError(f'{attr} must be > 0')

        if value < 0 and attr in ('x', 'y'):
            raise ValueError(f'{attr} must be >= 0')

    def area(self):
        ''' method returns the area '''

        a = self.__height * self.__width
        return a

    def display(self):
        '''
        method that prints a rectangle
        instance with the character <#>,
        handles the w, h & postions: x, y
        '''

        for _ in range(self.__y):
            print()

        for rows in range(self.__height):
            for _ in range(self.__x):
                print(" ", end='')

            for cols in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        '''
        string representation of an object:
        this method is called when an object
        is printed
        '''

        return (f'[Rectangle] ({self.id})         {self.x}/{self.y}'
                f' - {self.width}/{self.height}'
                )

    def update(self, *args, **kwargs):
        '''
        function that assigns attributes
        based on positional and keyword
        arguments
        '''

        attr = ['id', 'width', 'height', 'x', 'y']

        for i, arg in enumerate(args):
            if i < len(attr):
                setattr(self, attr[i], arg)

        for key, value in kwargs.items():
            if key in attr:
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        function that returns the
        dictionary representation of a
        rectangle
        '''

        d_ict = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
        return d_ict
