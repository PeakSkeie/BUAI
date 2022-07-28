def HoursToMinutes(x):
    x = x * 60
    return x

def hTOt_OR_tTOh(x, y):
    if x == 'h':
        y = y * 60
    elif x == 'm':
        y = y / 60
    else:
        return 'Please type h or m.'
    return y

def NumberOfWords(x):
    y = len(str(x))
    return y

print(HoursToMinutes(3))
print(hTOt_OR_tTOh('m', 120))
print(NumberOfWords('apple'))
