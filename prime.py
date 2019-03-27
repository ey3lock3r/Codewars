import math as m
prime_lst = set()

def test():
    assert primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)", 'Testcase 1 Failed!'
    assert primeFactors(7919) == "(7919)", 'Testcase 2 Failed!'
    assert primeFactors(18195729) == "(3)(17**2)(31)(677)", 'Testcase 3 Failed!'
    assert primeFactors(933555431) == "(7537)(123863)", 'Testcase 4 Failed!'
    assert primeFactors(342217392) == "(2**4)(3)(11)(43)(15073)", 'Testcase 5 Failed!'
    #assert primeFactors(35791357) == "(7)(5113051)", 'Testcase 6 Failed!'
    #assert primeFactors(10720710) == "(2)(3**2)(5)(7**2)(11)(13)(17)(73)", 'Testcase 7 Failed!'
    #assert primeFactors(775878912) == "(2**8)(3**4)(17)(31)(71)", 'Testcase 8 Failed!'
    print("All Testcases Passed!")

def check_prime(n):
    for x in range(1, n+1):
        if x in prime_lst:
            yield x 
        elif not m.sqrt(x).is_integer():
            for i in range(2, x, 2):
                if x % i == 0:
                    break
            else:
                prime_lst.add(x)
                yield x
            
            #if x == 2:
            #    prime_lst.add(x)
            #    yield x

def primeFactors(n):
    d = {
        1: "({:n})",
        2: "({:n}**{power})"
    }
    q = n
    power = 0
    res = ''
    check_prime(n)
    for prime in check_prime(n):
        while q%prime==0:
            q /= prime
            power += 1
        if power > 0:
            res = ''.join((res,d[max(1, min(2, power))].format(prime,power=power)))
        power = 0
        if q == 1:
            break 
    print (len(prime_lst))           
    return res

#print(primeFactors(933555431))
test()
print([i for i in check_prime(22)])