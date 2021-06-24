# Import unittest to write or tests
import unittest
# Import or basic function
from some_basic_code import my_basic_function 

# Unittest boilerplate
class TestStringMethods(unittest.TestCase):

    # Only one test and it shold pass - meaning build will be successful!
    def test_my_basic_function_passes(self):
        self.assertEqual(my_basic_function(), "Hi from my basic function!") # Pass!

if __name__ == '__main__':
    unittest.main()
