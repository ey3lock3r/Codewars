gcdl = lambda a, b: b if a%b==0 else a % gcdl(b, a%b)
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

number = 14789166241
x_fixed = 2
cycle_size = 2
x = 2
factor = 1
tstep = 0
while factor == 1:
    count = 1
    while count <= cycle_size and factor <= 1:
        x = (x*x + 1) % number
        factor = gcd(x - x_fixed, number)
        count += 1
        tstep += 1
        print ('{:3n} {:5n} {:4n} {:2n} {:2n} {:2n}'.format(tstep, x, x_fixed, count, cycle_size, factor))
        
    cycle_size *= 2
    x_fixed = x

print(factor)