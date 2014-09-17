'''
Tests focused on the functionality to deal with files
'''

import sys
import unittest
sys.path.append('../src/')
from rgrep import *


class TestRGrepFiles(unittest.TestCase):
    def test_match_in_files(self):
        ''' For now only look for a boolean
        found or not found
        '''
        rgrep = RGrep(pattern='hello', filepath='./')
        self.assertEqual(rgrep.match_in_files(), True)

if __name__ == '__main__':
    unittest.main()
