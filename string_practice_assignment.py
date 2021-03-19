def upup(s):
    if len(s) < 2:
        return s.upper()
    return ''.join((s[0:-1].title(),s[-1].upper()))

print(' '.join(upup(s) for s in 'i like cats'.split()))