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
        rgrep = RGrep('hello', 'hello')
        self.assertEquals(rgrep.get_match(), True)

    def test_grep_pattern_in_text(self):
        rgrep = RGrep('hello', 'hello world')
        self.assertEquals(rgrep.get_match(), True)

    def test_case_insensitive(self):
        rgrep = RGrep('hello', 'HELLO')
        self.assertEquals(rgrep.get_match_case_insensitive(), True)

    def test_count(self):
        rgrep = RGrep('hello', 'hello\nhello\nhello')
        self.assertEquals(rgrep.get_count(), 3)

    def test_version_information(self):
        self.assertEquals(RGrep.get_version(), 'RGrep (BSD) 0.0.1')

    def test_inverted_match(self):
        rgrep = RGrep('hello', 'hello\nworld\nhello')
        self.assertEquals(rgrep.get_match_inverted(), True)


if __name__ == '__main__':
    unittest.main()
