'''
Grep implemented in Python
'''

import os
import sys
import argparse


class RGrep(object):
    ''' Class that represents a grep object.
    Contains all required methods to handle
    special requests (most of the flags supported
    by grep)
    '''
    def __init__(self, pattern='', text='', filepath=''):
        self.pattern = pattern
        self.text = text
        self.filepath = filepath

    @classmethod
    def display_usage(cls):
        ''' Display usage in case no arguments are provided '''
        return 'Usage: python rgrep [options] pattern files\n' \
                'The options are the same as grep\n'

    @classmethod
    def get_version(cls):
        ''' Return the version '''
        return 'RGrep (BSD) 0.0.1'

    def get_count(self):
        ''' Return the count of matches '''
        count = 0
        text = self.text.split('\n')
        for line in text:
            if self.pattern in line:
                count += 1
        return count

    def get_exact_match(self, other_text=''):
        ''' Return if there is an exact match '''
        if other_text == '':
            return self.pattern == self.text
        else:
            return self.pattern == other_text

    def get_match(self, other_text=''):
        ''' Return if there is a match, exact or not '''
        if other_text == '':
            return self.pattern in self.text
        else:
            return self.pattern in other_text

    def get_match_case_insensitive(self, other_text=''):
        ''' Return if there is a case insensitive match '''
        self.pattern = self.pattern.lower()

        if other_text == '':
            self.text = self.text.lower()
            return self.get_match()
        else:
            return self.get_match(other_text=other_text.lower())

    def get_match_inverted(self):
        ''' Outputs all lines that inverse-match.
        Behavior might change later.
        '''
        vmatches = []
        text = self.text.split('\n')
        for line in text:
            if self.pattern not in line:
                vmatches.append(line)

        return vmatches

    def get_quiet_match(self):
        ''' Returns true as soon as a first match is found.
        '''
        text = self.text.split('\n')
        for line in text:
            if self.pattern in line:
                return True
        return False

    def get_match_maxcount(self, max_count):
        ''' Stop matching after a certain count
        Returns the match count for now.
        Behavior might change later.
        '''
        count = 0
        text = self.text.split('\n')
        for line in text:
            if self.pattern in line:
                count += 1
                if count == max_count:
                    break
        return count

    def get_line_numbers(self):
        ''' Return a list of line numbers where the
        match is found. For now, implemented to work with
        a newline-separated string as the text. Behavior
        will change to incorporate files.
        '''
        lines = []
        count = 0
        text = self.text.split('\n')
        for line in text:
            count += 1
            if self.pattern in line:
                lines.append(count)

        return lines

    def get_only_matching_parts(self):
        ''' Get only parts that match '''
        matches = []
        for text_elem in self.text.split('\n'):
            if self.pattern in text_elem:
                matches.append(self.pattern)

        return matches

    def match_in_files(self):
        ''' Return if there is a match in a file '''
        return self.handle_files(self.get_match)

    def exact_match_in_files(self):
        ''' Return if there is an exact match in files '''
        files = os.listdir(self.filepath)
        for one_file in files:
            with open(one_file, 'r') as fhi:
                content = fhi.readlines()
                for content_line in content:
                    if self.get_exact_match(other_text=content_line.strip()):
                        return True

        return False

    def match_case_insensitive_in_files(self):
        ''' Return if there is a match in files irrespective of case '''
        return self.handle_files(self.get_match_case_insensitive)

    def handle_files(self, function):
        ''' Handle grepping inside files '''
        files = os.listdir(self.filepath)
        for one_file in files:
            with open(one_file, 'r') as fhi:
                content = fhi.read()
                return function(other_text=content)

def main(args):
    ''' Main method for handling the flow when ran from the command line '''
    if len(args) < 2:
        print RGrep.display_usage()

if __name__ == '__main__':
    main(sys.argv)
