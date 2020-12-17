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

@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "skip db storage")       
def test_show(self):
        '''
            Testing that show exists
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(isinstance(x, str))

def test_class_name_doest_exist(self):
        """ Testing errors if cls doesn't exist"""
        console = self.create()
        console.onecmd("create Index")
        x = (self.capt_out.getvalue())
        self.assertEqual(" class doesn't exist \n", x)
        
def test_show_no_instance_found(self):
        '''
            Test show message error for id missing
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "124356876")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
def test_create_fileStorage(self):
    """test filestorage engine"""
    console = self.create()
    console.onecmd("create User")
    self.assertTrue(isinstance(self.capt_out.getvalue(), str))

if __name__ == '__main__':
    unittest.main()

