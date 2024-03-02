from app.plugins.add import Add
import logging
import unittest
from unittest.mock import patch
from io import StringIO

class TestAddCommand(unittest.TestCase):

    def test_execute(self):
        command = Add()
        args = "10 5"
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            command.execute(args)
            output = fake_out.getvalue().strip()
        
        self.assertEqual(output, "The sum is: 15")
        self.assertEqual(logging.getLogger().getEffectiveLevel(), logging.INFO)

    def test_execute_invalid_args(self):
        command = Add()
        args = "10"
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            command.execute(args)
            output = fake_out.getvalue().strip()
        
        self.assertEqual(output, "Please provide at least two numbers.")
        self.assertEqual(logging.getLogger().getEffectiveLevel(), logging.ERROR)

if __name__ == '__main__':
    unittest.main()