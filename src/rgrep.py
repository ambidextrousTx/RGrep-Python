def display_usage():
    return 'Usage: python rgrep [options] pattern files\nThe options are the '\
           'same as grep\n'


class RGrep(object):
    def __init__(self):
        self.version = 'RGrep (BSD) 0.0.1'
        self.count = False
        self.pattern = ''
        self.text = ''
        self.case = ''

    def get_version(self):
        return self.version

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
