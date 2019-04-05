def test(a, b, num, msg):
    assert a == b, msg
    print('Test case {} passed!'.format(num))

def escape(carpark):
    l = len(carpark)
    w = len(carpark[0])

    if w == 0:
        return []

    directions = []
    lr = {
        0: 'L{}',
        1: 'R{}',
        2: 'D{}'
    }

    me = 0
    start = 0
    for i in range(l):
        for j in range(w):
            if carpark[i][j] == 2:
                start = i
                me = j
                break
        if me > 0:
            break

    if start == l-1:
        if me == w-1:
            return []
        else:
            return [lr[1].format(w-1-me)]

    dcnt = 0
    stair = 0
    for i in range(start, l):
        for j in range(w):
            if carpark[i][j] == 1:
                stair = j
                break

        if stair < me:
            if dcnt > 0:
                directions.append(lr[2].format(dcnt))
                dcnt = 0
            directions.append(lr[0].format(me-stair))
        elif stair > me:
            if dcnt > 0:
                directions.append(lr[2].format(dcnt))
                dcnt = 0
            directions.append(lr[1].format(stair-me))

        if i == l-1:
            if dcnt > 0:
                directions.append(lr[2].format(dcnt))
            if me != w-1:
                directions.append('R'+ str(w-1-me))
            break

        #print('me:',me, ' stair:',stair, ' dcnt:',dcnt)
        me = stair
        dcnt += 1

    return directions

test1 = [[]]
res1 = []

test2 = [[0, 2, 0, 0, 0]]
res2 = ["R3"]

test3 = [[0, 0, 0, 0, 2]]
res3 = []

test4 = [[1, 0, 0, 0, 2],
        [0, 0, 0, 0, 0]]
res4 = ["L4", "D1", "R4"]

test5 = [[1, 0, 0, 0, 2],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]]
res5 = ["L4","D2","R4"]

test6 = [[0, 1, 0, 0, 2],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]]
res6 = ["L3","D2","R3","D2"]

test7 = [[2, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]]
res7 = ["R3","D2","R1"]

test8 = [[1, 0, 0, 0, 2],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
res8 = ["L4","D1","R4","D1","L4","D1","R4"]

test(escape(test1),res1, 1, 'Should return empty')
test(escape(test2),res2, 2, 'Should return ["R3"]')
test(escape(test3),res3, 3, 'Should return empty')
test(escape(test4),res4, 4, 'Should return ["L4", "D1", "R4"]')
test(escape(test5),res5, 5, 'Should return ["L4","D2","R4"]')
test(escape(test6),res6, 6, 'Should return ["L3","D2","R3","D2"]')
test(escape(test7),res7, 7, 'Should return ["R3", "D2", "R1"]')
test(escape(test8),res8, 8, 'Should return ["L4","D1","R4","D1","L4","D1","R4"]')