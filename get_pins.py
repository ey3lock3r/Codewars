def get_pins(observed):
    pad = {
        '0': ('08'),
        '1': ('124'),
        '2': ('1235'),
        '3': ('236'),
        '4': ('1457'),
        '5': ('24568'),
        '6': ('3569'),
        '7': ('478'),
        '8': ('57890'),
        '9': ('689')
    }
    l = lambda a, b: [x+y for x in a for y in b]
    res = pad[observed[0]]
    for i in range(1, len(observed)):
        res = l(res, pad[observed[i]])
    return res

def assert_equals(a, b, c):
    assert a == b, c
    print('Testcase Passed. ' + c)

expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

#for tup in expectations:
#  assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])
print(get_pins('007'))