#!/usr/bin/python3
"""Base model for core functionality"""
import json
import csv
import turtle


class Base:
    """Represents the base model for all shapes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance of the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string rep of ``list_dictionaries``
        Arguments:
            list_dictionaries (dict): a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string rep to a file
        Arguments:
            cls :  class
            list_objs (list): list of instances who inherit from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string rep ``json_string``
        Arguments:
            json_string (str): string repping a list of dicts
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Arguments:
            cls : class
            **dictionary (dict): k/v pairs of attribs
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Arguments:
            cls: class
            list_objs: list of base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    props = ["id", "width", "height", "x", "y"]
                else:
                    """Square"""
                    props = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=props)
                for inst in list_objs:
                    writer.writerow(inst.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a csv file

        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    props = ["id", "width", "height", "x", "y"]
                else:
                    props = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=props)
                list_dicts = [dict([key, int(value)] for key, value in
                                d.items()) for d in list_dicts]
                return (cls.create(**d) for d in list_dicts)
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all Rectangles and Squares

        Arguments:
            list_rectangles: list of rectangles
            list_squares: list of squares
        """
        drawing = turtle.Turtle()
        drawing.screen.bgcolor("#00ffad")
        drawing.pensize(2)
        drawing.shape("turtle")
        drawing.color("#ff0000")

        for rect in list_rectangles:
            drawing.showturtle()
            drawing.up()
            drawing.goto(rect.x, rect.y)
            drawing.down()
            for i in range(2):
                drawing.forward(rect.width)
                drawing.left(90)
                drawing.forward(rect.height)
                drawing.left(90)
            drawing.hideturtle()

        drawing.color("#8a00ff")
        for square in list_squares:
            drawing.showturtle()
            drawing.up()
            drawing.goto(square.x, square.y)
            drawing.down()
            for j in range(2):
                drawing.forward(square.size)
                drawing.left(90)
                drawing.forward(square.size)
                drawing.left(90)
            drawing.hideturtle()

        drawing.exitonclick()
