#!/usr/bin/python3
''' Class Test '''
import unittest
import pep8
import inspect
import datetime
import sys
from console import HBNBCommand

class TestCodeconsole(unittest.TestCase):

    def test_pep8_conformance(self):
    """Test that we conform to PEP8."""
    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files(['models/base_model.py'])
    self.assertEqual(result.total_errors, 0,
                     "Found code style errors (and warnings).")

def do_quit(self):
    """ Test Quit """
    c = self.create()
    self.assertTrue(c.onecmd("quit"))

def do_EOF(self):
    """ Test EOF """
    c = self.create()
    self.assertTrue(c.onecmd("EOF"))

def create(self):
    """ create an instance of the HBNBCommand class"""
    return HBNBCommand()

def test_all(self):
    """ Test all exists """
    c = self.create()
    c.onecmd("all")
    self.assertTrue(isinstance(self.capt_out.getvalue(), str))

def test_class_name(self):
        """
            Testing the error msg .
        """
        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

if __name__ == '__main__':
    unittest.main()

