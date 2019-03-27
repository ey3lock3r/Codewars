import numpy as np
a = [67, 93, 100, -16, 65, 97, 92]

def valley_test(arr):
    #arr.sort(reverse=True)
    print(arr)
    print(arr[:7:2])
    print(arr[1:7:2])

    return arr.sort() or arr

print(valley_test(a))

def make_valley_1(arr):
    arr = sorted(arr, reverse = True)
    return arr[::2] + arr[1::2][::-1]

make_valley_2 = lambda a: a.sort() or a[::-2]+a[len(a)%2::2]

def make_valley_fin(arr):
    a_sorted = sorted(arr, reverse=True)
    x = len(a_sorted)
    larr = [a_sorted[a] for a in range(x) if a%2 == 0]
    rarr = [a_sorted[a] for a in range(x) if a%2 != 0]
    rarr = sorted(rarr)
    #larr.extend(rarr)
    return larr + rarr

def make_valley2(arr):
    arr_sorted = sorted(arr, reverse=True)
    lengt = len(arr)
    half = int(lengt / 2) + 1

    i = 0
    while i < lengt:
        dots = '.' * half * 2
        if i + 1 < lengt:
            if i > 1 and arr_sorted[i] != arr_sorted[i+1]:
                print(' '*i, arr_sorted[i], dots)
                print(' '* int(i + 2 + len(dots)), dots, arr_sorted[i+1])
            else:
                print(' '*i, arr_sorted[i], dots*2, arr_sorted[i+1])
        else:
            print(' '* (i + 1 + len(dots)), arr_sorted[i])
        i += 2
        half -= 1


def make_valley(arr):
    temp = sorted(arr, reverse=True)
    print (temp)
    lent = len(temp)
    depth = int(round(lent / 2,0))
    i = 0
    linelen = depth ** 2 + 4
    print (linelen)
    while i < lent:
        dots = '.'* depth ** 2
        spc = int((linelen - len(dots) - 4) /2)
        space = ' ' * spc
        if i+1 < lent:
            if i > 1 and temp[i] != temp[i+1]:
                string = str(temp[i]) + dots
                spc = int(linelen / 2 - len(string))
                string = ' '* spc + string
                print (string)
                
                rstring = dots + str(temp[i+1])
                rstring = ' ' * len(string) + rstring
                print (rstring)
            else:
                print (space, temp[i], dots, temp[i+1])
        else:
            print (space, temp[i])
        i = i + 2
        depth -= 1

#print(make_valley_fin(a))