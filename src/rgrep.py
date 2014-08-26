class RGrep(object):
    def __init__(self, pattern='', text=''):
        self.pattern = pattern
        self.text = text

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

    def get_match(self):
        return self.pattern in self.text

    def get_match_case_insensitive(self):
        self.pattern = self.pattern.lower()
        self.text = self.text.lower()
        return self.get_match()

    def get_match_inverted(self):
        ''' Outputs all lines that inverse-match.
        Behavior might change later.
        '''
        text = self.text.split('\n')
        for line in text:
            if self.pattern not in line:
                yield line
