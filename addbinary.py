import math as m
def add_binary(a,b):
    quo = a+b
    log = int(m.log2(quo))+1
    x = lambda x: (x/2, x%2)
    bstr = ''
    for _ in range(log):
        quo, r = x(int(quo))
        bstr += str(int(r>0))
    return bstr[::-1]
    #str = ''
    #while quo != 0:
    #    quo, r = divmod(quo, 2)
    #    if r == 0:
    #        str += '0'
    #    else:
    #        str += '1'
    
def add_binary1(a,b):
    return bin(a+b)[2:]

#add_binary(51, 12)
print(str(add_binary1(290, 4)))