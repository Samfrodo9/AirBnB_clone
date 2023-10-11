#!/usr/bin/python3
'''contains a file storage class'''

from json import dumps
from json import loads
from os.path import isfile

class FileStorage:
    '''file storage class'''
    __file_path = "storage.json"
    __objects = {} # will store all objects by classname.id

    def __init__(self):
        '''instance constructor'''

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects
    
    def new(self, obj):
        '''sets in __objects the obj with key <obj classname.id'''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj.to_dict() #do something

    def save(self):
        '''serializes __objects to the JSON file'''
        json_str = dumps(self.__objects)
        filename = self.__file_path
        with open(filename, 'w', encoding="utf-8") as file_:
            file_.write(json_str)

    def reload(self):
        '''deserializes the JSON file to __objects
        if the file doesnot exist do nothing'''

        filename = self.__file_path
        if isfile(filename):
            with open(filename, 'r', encoding="utf-8") as file_:
                line = file_.readline()
            self.__objects = loads(line)

        else:
            pass
