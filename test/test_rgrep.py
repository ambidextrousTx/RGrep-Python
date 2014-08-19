import sys
import unittest
sys.path.append('../src/')
from rgrep import *


class TestRGrep(unittest.TestCase):
    def test_grep_without_arguments(self):
        self.assertEquals(rgrep(), 'Usage: python rgrep [options] pattern files\nThe options are the same as grep\n')

    def test_grep_pattern_text(self):
        self.assertEquals(rgrep('hello', 'hello'), True)

    def test_grep_pattern_in_text(self):
        self.assertEquals(rgrep('hello', 'hello world'), True)

    def test_case_insensitive(self):
        self.assertEquals(rgrep('hello', 'HELLO', 'i'), True)

if __name__ == '__main__':
    unittest.main()
