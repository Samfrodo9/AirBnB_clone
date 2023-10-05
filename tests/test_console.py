#!/usr/bin/python3
"""console test module"""

from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand
import unittest


class Test_console(unittest.TestCase):
    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")  # execute the help command
            output = f.getvalue()  # get the captured value as a string

            expect = "Documented commands (type help <topic>):\n========================================\nEOF  help  quit\n"

        # Remove any trailing whitespace, including newlines, for comparison
        output = output.strip()
        expect = expect.strip()

        self.assertEqual(output, expect)


if __name__ == "__main__":
    unittest.main()
