#!/usr/bin/python3
'''console test module'''

from unittest.mock import patch
from io import StringIO
import sys
from AirBnB_clone.console import HBNBCommand

with patch('sys.stdout', new=StringIO()) as f:

    HBNBCommand().onecmd("help") #execute the help command
    output = f.getvalue() #get the captured value as a string
assert output == "Documented commands (type help <topic>):\n========================================\nEOF  help  quit\n"
