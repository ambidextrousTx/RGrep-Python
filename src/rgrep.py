def rgrep(pattern='', text='', case=''):
    if pattern == '' or text == '':
        return 'Usage: python rgrep [options] pattern files\nThe options are the same as grep\n'
    else:
        if case == 'i':
            return pattern.lower() in text.lower()
        else:
            return pattern in text
