def assertEqual(v1, v2, diff=10**-10):
    if isFloat(v1) or isFloat(v2):
        d = abs(v1 - v2)
        if d > diff:
            print(str(v1) + ' is not equal to ' + str(v2) + ' difference ' + str(d))
        else:
            print('Succeeded')
    elif v1 != v2:
        print(str(v1) + ' is not equal to ' + str(v2))
    else:
        print('Succeeded')
    
def assertNotEqual(v1, v2, diff=10**-10):
    if isFloat(v1) or isFloat(v2):
        d = abs(v1 - v2)
        if d <= diff:
            print(str(v1) + ' is not equal to ' + str(v2) + ' difference ' + str(d))
        else:
            print('Succeeded')
    elif v1 == v2:
        print(str(v1) + ' is equal to ' + str(v2))
    else:
        print('Succeeded')
        
def assertTrue(v):
    if not v:
        print(str(v) + ' is not True')
    else:
        print('Succeeded')

def assertFalse(v):
    if v:
        print(str(v) + ' is not False')
    else:
        print('Succeeded')
        
from numpy import float32, float64
def isFloat(v):
    return type(v) == float or type(v) == float32 or type(v) == float64