def dbl_linear(n):
    temps = set([1])
    arr = [1]
    l = lambda a: (2*a+1, 3*a+1)
    tar = 0
    #while a <= 
    #for i in range(int(n/2)+1):
    for i in range(n+1):
        a, b = l(arr[i])
        temps.update((a, b))
        arr = sorted(list(temps))
        
        if len(arr) <= n:
            print ('{:2n} {:3n} {:3n} {:3n} {:3n}'.format(i, arr[i], 0, a, b))
        else:
            print ('{:2n} {:3n} {:3n} {:3n} {:3n}'.format(i, arr[i], arr[n], a, b))
            if tar == arr[n]:
                break
            tar = arr[n]
    
    print(arr)
    return arr[n]

def testing(actual, expected, n):
    assert actual == expected, 'Testcase {:1n} Failed!'.format(n)
    print('Test Passed!')

print(dbl_linear(50))
#testing(dbl_linear(10), 22, 1)
#testing(dbl_linear(20), 57, 2)
#testing(dbl_linear(30), 91, 3)
#testing(dbl_linear(50), 175, 4)