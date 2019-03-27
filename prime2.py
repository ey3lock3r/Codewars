import math as m
def primeFactors(n): 
    d = {
        1: "({:1.0f})",
        2: "({:1.0f}**{power})"
    }
    power = 0
    res = '' 
    while n % 2 == 0: 
        n /= 2
        power += 1

    if power > 0:
        res = ''.join((res,d[max(1, min(2, power))].format(2,power=power)))
        power = 0

    for i in range(3,int(m.sqrt(n))+1,2): 
        while n % i== 0: 
            n = n / i
            power += 1
        
        if power > 0:
            res = ''.join((res,d[max(1, min(2, power))].format(i,power=power)))
            power = 0   
    if n > 2: 
        res = ''.join((res, d[1].format(n)))
    
    return res

def test():
    assert primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)", 'Testcase 1 Failed!'
    assert primeFactors(7919) == "(7919)", 'Testcase 2 Failed!'
    assert primeFactors(18195729) == "(3)(17**2)(31)(677)", 'Testcase 3 Failed!'
    assert primeFactors(933555431) == "(7537)(123863)", 'Testcase 4 Failed!'
    assert primeFactors(342217392) == "(2**4)(3)(11)(43)(15073)", 'Testcase 5 Failed!'
    assert primeFactors(35791357) == "(7)(5113051)", 'Testcase 6 Failed!'
    assert primeFactors(782611830) == "(2)(3**2)(5)(7**2)(11)(13)(17)(73)", 'Testcase 7 Failed!'
    assert primeFactors(775878912) == "(2**8)(3**4)(17)(31)(71)", 'Testcase 8 Failed!'
    print("All Testcases Passed!")

#test()
#print(primeFactors(14789166241))
print(primeFactors(51923))
print(primeFactors(378))