def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting2(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0

##############################################################################33
def is_palindrome(n):
    c = str(n)
    if len(c) > 1:
        half = int(len(c)/2)
        l, r = c[:half], c[:-half-1:-1]
        check = max(list(map(lambda pair: 0 if pair[0] == pair[1] else 1, zip(l, r))))
        if check == 0:
            return True
    
    return False

def is_followed_byzero(n):
    c = str(n)
    if len(c) > 1:
        if max(c[1:]) == '0':
            return True

    return False

def is_sorted(n):
    last0 = False
    c = str(n)
    if c[-1] == '0':
        c = c[:len(c)-1]
        last0 = True
    l = len(c)
    check1 = max(list(map(lambda pair: 0 if pair[0] == pair[1] else 1, zip(list(c), [str(x) for x in range(int(c[0]), int(c[0])+l)]))))
    check2 = max(list(map(lambda pair: 0 if pair[0] == pair[1] else 1, zip(list(c), [str(x) for x in range(int(c[0]), int(c[0])-l,-1)]))))
    if check1 == 0 or check2 == 0:
        if last0 and (c[-1] != '9' and c[-1] != '1'):
            return False
        else:
            return True
    else:
        return False

def is_monotone(n):
    c = str(n)
    check = max(list(map(lambda x: 0 if x == c[0] else 1, c)))
    if check == 0:
        return True
    else:
        return False

def is_interesting(number, awesome_phrases):
    if number > 99:
        if is_palindrome(number) or is_followed_byzero(number) or is_sorted(number) or is_monotone(number):
            return 2

        for great in awesome_phrases:
            if number == great:
                return 2

    if number > 97:
        for great in awesome_phrases:
            if (number >= great - 2 and number <= great):
                return 1

        if is_followed_byzero(number+1) or is_followed_byzero(number+2) or  \
            is_palindrome(number+1) or is_palindrome(number+2) or           \
            is_sorted(number+1) or is_sorted(number+2) or                   \
            is_monotone(number+1) or is_monotone(number+2):
            return 1
        
    return 0

def assert_equals(a, b):
    assert a == b, 'Testcase failed!'

tests = [
	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
	{'n': 1336, 'interesting': [1337, 256], 'expected': 1},
	{'n': 1337, 'interesting': [1337, 256], 'expected': 2},
	{'n': 11208, 'interesting': [1337, 256], 'expected': 0},
	{'n': 11209, 'interesting': [1337, 256], 'expected': 1},
	{'n': 11211, 'interesting': [1337, 256], 'expected': 2},
]
#for t in tests:
#	assert_equals(is_interesting(t['n'], t['interesting']), t['expected'])

n = 'double  spaces'
x = list(n)
print (x)
temp = []
res = []
while True:
    temp.append(x.pop(0))
    if temp[-1] == ' ':
        res = res + temp[-2:-len(temp)-1:-1] + [' ']
        temp.clear()
    
    if len(x) == 0:
        res = res + temp[-1:-len(temp)-1:-1]
        break

print (''.join(res)) 