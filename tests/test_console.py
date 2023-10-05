#!/usr/bin/python3
"""console test module"""

from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
import unittest


class Test_console(unittest.TestCase):
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")  # execute the help command
            output = f.getvalue()  # get the captured value as a string
            expect = '''
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update\n'''

        # Remove any trailing whitespace, including newlines, for comparison
        output = output.strip()
        expect = expect.strip()

        self.assertEqual(output, expect)

    def test_help_arg(self):
        """tests the help command with arg"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue()

            expect = """
Usage: create <class-name>
create a new object/instance of <class-name>
            """
            output = output.strip()
            expect = expect.strip()

            self.assertEqual(output, expect)

    def test_help_err(self):
        '''tests the help command with an undefined command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help base")
            output = f.getvalue()
            expect = "*** No help on base"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_create(self):
        '''tests the create command wityh valid syntax'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue()
            self.assertEqual(type(output), str)

    def test_create_fake_class(self):
        '''tests the create command with fake class'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Mymodel")
            output = f.getvalue()
            expect = "** class doesn't exist **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_create_noclass(self):
        '''tests create without classname'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue()
            expect = "** class name missing **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_destroy_noclass(self):
        '''tests destroy without class name'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue()
            expect = "** class name missing **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_destroy_noid(self):
        '''tests destroy without id'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue()
            expect = "** instance id missing **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_destroy_fakeclass(self):
        '''tests destroy with fake class'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Base")
            output = f.getvalue()
            expect = "** class doesn't exist **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_destroy_fakeid(self):
        '''tests destroy with fake id'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel tyop")
            output = f.getvalue()
            expect = "** no instance found **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_destroy(self):
        '''tests destroy with correct syntax
        make a test class to set up where you delete the
        storage class create a class the destroy
        '''
        pass

    def test_show_noclass(self):
        ''''tests show with no class'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue()
            expect = "** class name missing **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_show_noid(self):
        '''tests the show command without id'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            output = f.getvalue()
            expect = "** instance id missing **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_show_fakeclass(self):
        '''tests show with fake class'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Base")
            output = f.getvalue()
            expect = "** class doesn't exist **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_show_fakeid(self):
        '''tests the show command with fake id'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel come")
            output = f.getvalue()
            expect = "** no instance found **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_show(self):
        '''tests the show command with correct syntax
        a different test class for this'''
        pass

    def test_update_noclass(self):
        '''tests update without class'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue()
            expect = "** class name missing **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_update_noid(self):
        '''testd update with no id'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue()
            expect = "** instance id missing **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_update_fakeclass(self):
        '''tests update with a fake class'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Base")
            output = f.getvalue()
            expect = "** class doesn't exist **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_update_fakeid(self):
        '''tests update with a fake id'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel get")
            output = f.getvalue()
            expect = "** no instance found **"

            output = output.strip()
            expect = expect.strip()
            self.assertEqual(output, expect)

    def test_update_noattr(self):
        '''tests update without attribut
        a different class'''
        pass

    def test_update_novalue(self):
        '''tests update without value
        a different class'''
        pass


class test_console_valid(unittest.TestCase):
    '''tests valis command syntax'''
    def setup(self):
        '''set up config'''
        file_ = storage.__file_path
        with open(file_, 'w', encoding="utf-8") as f:
            f.write("")

    def test_create_valid(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel get")
            output = f.getvalue()
            expect = "** no instance found **"


if __name__ == '__main__':
    unittest.main()
