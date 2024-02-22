#!/usr/bin/python3
""" test console module"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class test_Console(unittest.TestCase):
    """ test console module """

    def test_create_errors(self):
        """Test create command errors."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create not_class")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
