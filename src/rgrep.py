def display_usage():
    return 'Usage: python rgrep [options] pattern files\nThe options are the '\
           'same as grep\n'


def rgrep(pattern='', text='', case='', count=False, version=False):
    if pattern == '' or text == '':
        return display_usage()
    elif not count:
        if case == 'i':
            pattern = pattern.lower()
            text = text.lower()

        return pattern in text


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
