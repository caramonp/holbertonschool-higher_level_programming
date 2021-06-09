#!/usr/bin/python3
"""
the first class Base:
"""


import json


class Base:
    """
    class Base is the base for all the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """inizialitation of the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to use Json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to write the string rep in a file
        """
        name = cls.__name__ + '.json'
        empty = []
        if list_objs is not None:
            for objets in list_objs:
                aux = cls.to_dictionary(objets)
                empty.append(aux)
        with open(name, mode='w', encoding="UTF8") as xfile:
            xfile.write(cls.to_json_string(empty))

    @staticmethod
    def from_json_string(json_string):
        """Method to return the list of JSON string rep"""
        empty = []
        if json_string is None or not json_string:
            return empty
        else:
            aux = json.loads(json_string)
            return aux

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        name = cls.__name__ + '.json'
        empty = []
        list3 = []
        try:
            with open(name, mode='r', encoding='UTF8') as xfile:
                aux = xfile.read()
                empty = cls.from_json_string(aux)
                """List of dicts"""
                for objets in empty:
                    aux2 = cls.create(**objets)
                    list3.append(aux2)
                return list3
        except FileNotFoundError:
            return empty
