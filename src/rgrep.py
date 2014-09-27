import os


class RGrep(object):
    def __init__(self, pattern='', text='', filepath=''):
        self.pattern = pattern
        self.text = text
        self.filepath = filepath

    @classmethod
    def display_usage(cls):
        return 'Usage: python rgrep [options] pattern files\nThe options are the '\
            'same as grep\n'

    @classmethod
    def get_version(cls):
        return 'RGrep (BSD) 0.0.1'

    def get_count(self):
        count = 0
        text = self.text.split('\n')
        for line in text:
            if self.pattern in line:
                count += 1
        return count

    def get_match(self, other_text=''):
        if other_text == '':
            return self.pattern in self.text
        else:
            return self.pattern in other_text

    def get_match_case_insensitive(self):
        self.pattern = self.pattern.lower()
        self.text = self.text.lower()
        return self.get_match()

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

    def get_match_maxcount(self, m):
        ''' Stop matching after a certain count
        Returns the match count for now.
        Behavior might change later.
        '''
        count = 0
        text = self.text.split('\n')
        for line in text:
            if self.pattern in line:
                count += 1
                if count == m:
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
        matches = []
        for text_elem in self.text.split('\n'):
            if self.pattern in text_elem:
                matches.append(self.pattern)

        return matches

    def match_in_files(self):
        files = os.listdir(self.filepath)
        for f in files:
            with open(f, 'r') as fhi:
                content = open(f).read()
                return self.get_match(other_text=content)

    def exact_match_in_files(self):
        files = os.listdir(self.filepath)
        for f in files:
            with open(f, 'r') as fhi:
                content = open(f).readlines()
                for content_line in content:
                    if self.pattern == content_line.strip():
                        return True

        return False
