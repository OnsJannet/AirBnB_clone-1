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


if __name__ == '__main__':
    unittest.main()

