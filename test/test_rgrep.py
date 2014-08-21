import sys
import unittest
sys.path.append('../src/')
from rgrep import *


class TestRGrep(unittest.TestCase):
    def test_grep_without_arguments(self):
        self.assertEquals(RGrep.display_usage(), 'Usage: python rgrep '
                          '[options] pattern files\nThe options '
                          'are the same as grep\n')

    def test_grep_pattern_text(self):
        rgrep = RGrep()
        self.assertEquals(rgrep('hello', 'hello'), True)

    def test_grep_pattern_in_text(self):
        self.assertEquals(rgrep('hello', 'hello world'), True)

    def test_case_insensitive(self):
        self.assertEquals(rgrep('hello', 'HELLO', 'i'), True)

    def test_count(self):
        self.assertEquals(rgrep('hello', 'hello\nhello', count=True), 2)

    def test_version_information(self):
        self.assertEquals(rgrep('', '', version=True), 'RGrep (BSD) 0.0.1')


if __name__ == '__main__':
    unittest.main()
