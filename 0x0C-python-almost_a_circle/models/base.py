#!/usr/bin/python3
"""
Contains the class Base
"""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a json sting from list dictionary"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves object in file"""
        fileName = cls.__name__ + '.json'
        with open(fileName, 'w', encoding='utf-8') as output:
            if list_objs is None:
                output.write("[]")
            else:
                dictionary = [o.to_dictionary() for o in list_objs]
                output.write(Base.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        tryRun = []
        fileName = cls.__name__ + '.json'
        try:
            with open(fileName, 'r', encoding='utf-8') as file:
                tryRun = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        finally:
            return [cls.create(**d) for d in tryRun]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        fileName = cls.__name__ + '.csv'
        with open(fileName, 'w', encoding='utf-8') as output:
            if list_objs is None:
                output.write("[]")
            else:
                dictionary = [o.to_dictionary() for o in list_objs]
                output.write(Base.to_json_string(dictionary))

    @classmethod
    def load_from_file_csv(cls):
        tryRun = []
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                tryRun = cls.from_json_string(file.read())
        except FileNotFoundError:
            return tryRun
        return [cls.create(**obj) for obj in tryRun]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        my_turtle = turtle.Turtle()

        for item in list_rectangles:
            my_turtle.penup()
            my_turtle.goto(item.x, item.y)
            my_turtle.pendown()
            my_turtle.forward(item.width)
            my_turtle.right(90)
            my_turtle.forward(item.height)
            my_turtle.right(90)
            my_turtle.forward(item.width)
            my_turtle.right(90)
            my_turtle.forward(item.height)
            my_turtle.hideturtle()
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        for item in list_squares:
            my_turtle.goto(item.x, item.y)

            for _ in range(4):
                turtle.forward(item.size)
                turtle.right(90)
            my_turtle.hideturtle()
        turtle.mainloop()
