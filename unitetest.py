import unittest
from app import recommend
import json
import pandas as pd
import pickle

# Create Test Class
class test(unittest.TestCase):
    def test_moviename(self):
        result = recommend('Gandhi')
        key = ""
        container = result
        # error message in case if test case got failed 
        message = "key is not in container."
        # assertIn() to check if key is in container 
        self.assertIn(key, container, message) 

if __name__ == '__main__':
    unittest.main()

