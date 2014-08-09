import sys
import unittest
sys.path.append('../src/')
from rgrep import *


class TestRGrep(unittest.TestCase):
    def test_grep_without_arguments(self):
        self.assertEquals(rgrep(), 'Usage: python rgrep [options] pattern files\nThe options are the same as grep\n')

    def test_grep_pattern_text(self):
        self.assertEquals(rgrep('hello', 'hello'), True)

if __name__ == '__main__':
    unittest.main()