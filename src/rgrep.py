def display_usage():
    return 'Usage: python rgrep [options] pattern files\nThe options are the same as grep\n'


def rgrep(pattern='', text='', case=''):
    if pattern == '' or text == '':
        return display_usage()
    else:
        if case == 'i':
            pattern = pattern.lower()
            text = text.lower()

        return pattern in text
