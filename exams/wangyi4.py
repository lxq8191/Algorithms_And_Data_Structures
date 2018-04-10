def LSS(x, y):
    if (len(x) == 0 or len(y) == 0):
        return 0
    else:
        a = x[0]
        b = y[0]
        if (a == b):
            return LSS(x[1:], y[1:])+1
        else:
            return LSS(x[:], y[1:])

s1 = 'you i am a student'
s2 = 'ha i am'
print(LSS(s1,s2))

def diff(lst):
    
    pass