import math
def test(a, b, num, msg):
    assert a == b, msg
    print('Test case {:1d} passed!'.format(num))

def cut_fruits(fruits):
    if len(fruits) == 0:
        return []

    new_arr = []
    [new_arr.extend(str(fruit[:math.ceil(len(fruit)/2)] + ' ' + fruit[math.ceil(len(fruit)/2):]).split()) if fruit in FRUIT_NAMES else new_arr.append(fruit) for fruit in fruits]
    return new_arr

#FRUIT_NAMES preloaded in site
test(cut_fruits([]), [], 1,'Test case failed! Should return empty.')
test(cut_fruits(["hydrogen-bomb"]), ["hydrogen-bomb"], 2,'Test case failed! Should return ["hydrogen-bomb"].')
test(cut_fruits(["apple", "pear", "banana"]), ["app", "le", "pe", "ar", "ban", "ana"], 3, 'Test case failed! Should return ["app", "le", "pe", "ar", "ban", "ana"].')
test(cut_fruits(["apple", "pear", "banana", "bomb"]), ["app", "le", "pe", "ar", "ban", "ana", "bomb"], 4, 'Test case failed! Should return ["app", "le", "pe", "ar", "ban", "ana", "bomb"].')