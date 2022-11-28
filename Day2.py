def func(tup):
    if(tup[0]%2==0 and tup[1]%2==0):
        if(tup[0]<tup[1]):
            return tup[0]
        else:
            return tup[1]
    else:
        if (tup[0] < tup[1]):
            return tup[1]
        else:
            return tup[0]
var=func((4,5))
print(var)