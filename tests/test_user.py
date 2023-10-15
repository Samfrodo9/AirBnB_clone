#!/usr/bin/python3
"""test cases for user"""

from models.engine.file_storage import FileStorage
from console import HBNBCommand
import unittest
from os.path import isfile


class Test_user(unittest.Testcase):
    """test units"""

    def set_up():
<<<<<<< HEAD
        '''set up refactoring'''
        json = FileStorage.__file_path
        if isfile(json):
            with open(json, "w", encoding="utf-8") as f:
                f.write("")

if __name__ == '__main__':
    unittest.main()
=======
        """set up refactoring"""
        """
        rm storage.py

        """
>>>>>>> 491a0cf4657c4aa0c36cafedb235bd0d82e7065c
