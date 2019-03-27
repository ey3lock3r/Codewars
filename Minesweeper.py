import copy
def opengm(a, b):
    arr = result.split('\n')
    temp_arr = []
    for rw in arr:
        temp_arr.append(rw.split())
    return temp_arr[a][b]

def count(arr):
    arr = result.split('\n')
    temp_arr = []
    for rw in arr:
        temp_arr.extend(rw.split())
    return sum([1 for i in temp_arr if i == 'x'])

def test_game(arr2, solve2, test=False, mark=None, xcnt=0):
    temp_arr = copy.deepcopy(arr2)
    to_solve = copy.deepcopy(solve2)
    del_keys = set()
    changed = False
    passed  = True
    u_lq = lambda a: str(sum([1 for j, k in a if temp_arr[j][k] == '?']))
    u_lx = lambda a: str(sum([1 for j, k in a if temp_arr[j][k] == 'x']))

    if test and (temp_arr[mark[0]][mark[1]] == 'x' or temp_arr[mark[0]][mark[1]] == 'z'):
        return copy.deepcopy(temp_arr), copy.deepcopy(to_solve), xcnt, False

    if test or mark is not None:
        temp_arr[mark[0]][mark[1]] = 'x'
        lst = to_solve[mark][0]
        xcnt += 1
        for l, m in lst:
            to_solve[(l,m)][1] = u_lq(to_solve[(l,m)][0])
            to_solve[(l,m)][2] = u_lx(to_solve[(l,m)][0])

    while True:
    # if current element number matches the number of unsolved coordinates, mark as x.
    # delete that element from to_solve
        changed = False
        for i in to_solve:
            # if current coordinate matches with number of adjacent x, safe to open
            if temp_arr[i[0]][i[1]] == '?' or temp_arr[i[0]][i[1]] == 'x': continue
            if temp_arr[i[0]][i[1]] == to_solve[i][2]:
                for j, k in to_solve[i][0]:
                    if temp_arr[j][k] == '?':
                        if test:
                            temp_arr[j][k] = 'z'
                        else:
                            temp_arr[j][k] = str(opengm(j,k))
                        # update ?
                        lst = to_solve[(j,k)][0]
                        for l, m in lst:
                            to_solve[(l,m)][1] = u_lq(to_solve[(l,m)][0])
                del_keys.add(i)
                changed = True
            # if current coordinate matches with number of adjacent ?
            elif (temp_arr[i[0]][i[1]] == to_solve[i][1] and to_solve[i][2] == '0') or \
                temp_arr[i[0]][i[1]] == str(int(to_solve[i][1]) + int(to_solve[i][2])):
                for j, k in to_solve[i][0]:
                    if temp_arr[j][k] == '?':
                        temp_arr[j][k] = 'x'
                        xcnt += 1
                        # update ? & x
                        lst = to_solve[(j,k)][0]
                        for l, m in lst:
                            to_solve[(l,m)][1] = u_lq(to_solve[(l,m)][0])
                            to_solve[(l,m)][2] = u_lx(to_solve[(l,m)][0])
                changed = True
        while len(del_keys) > 0:
            del to_solve[del_keys.pop()]
        if changed == False:
            break
    
    # validate
    for i in to_solve:
        #print ("tosolve,",i)
        if temp_arr[i[0]][i[1]] != 'x' and temp_arr[i[0]][i[1]] != 'z':
            if temp_arr[i[0]][i[1]] != u_lx(to_solve[(i)][0]):
                passed = False
                break
    
    return copy.deepcopy(temp_arr), copy.deepcopy(to_solve), xcnt, passed

def solve_mine(map, n):
    arr = map.split('\n')
    temp_arr = []
    tempstr = []
    #convert to list
    for rw in arr:
        temp_arr.append(rw.split())
    
    h = len(temp_arr)
    l = len(temp_arr[0])
    adjacent_el = []
    to_solve    = {}
    temp        = []
    # store list of unsolved coordinates and their adjacents elements
    for a in range(h):
        for b in range(l):
            adjacent_el = [(r,c) for r in range(a-1, a+2) for c in range(b-1, b+2) if min(r, c) >= 0 and (r < h and c < l) and (r,c) != (a,b) and temp_arr[r][c] != '0']
            if temp_arr[a][b] == '0':
                # open all adjacent elements if current el is 0
                for e, f in adjacent_el:
                    temp_arr[e][f] = str(opengm(e,f))
                pass
            else:
                temp.append(adjacent_el[:])
                to_solve[(a,b)] = temp[:]
                temp = []
                adjacent_el = []

    # update job
    u_lq = lambda a: str(sum([1 for j, k in a if temp_arr[j][k] == '?']))
    u_lx = lambda a: str(sum([1 for j, k in a if temp_arr[j][k] == 'x']))

    for i in to_solve:
        unsolved_q = u_lq(to_solve[i][0])
        to_solve[i].append(unsolved_q)
        unsolved_x = u_lx(to_solve[i][0])
        to_solve[i].append(unsolved_x)
    
    temp_arr, to_solve, cnt, passed = test_game(temp_arr, to_solve)
    guesses = [i for i in to_solve if temp_arr[i[0]][i[1]] == '?']

    if passed:
        for rw in temp_arr:
            tempstr.append(' '.join(rw))
        return '\n'.join(tempstr)
    
    lucky_guess = []
    lucky_out_list  = []
    lucky_cnt   = 0
    lucky_save   = []

    print("X Count: ",n)
    for i in range(len(guesses)):
        temp_guesses = guesses[:]
        temp_arr2, to_solve2, cnt2, passed = copy.deepcopy(temp_arr), copy.deepcopy(to_solve), cnt, False
        t_i = i
        while not passed and len(temp_guesses) > 0:
            temp_arr2, to_solve2, cnt2, passed = test_game(temp_arr2, to_solve2, test=True, mark=temp_guesses.pop(t_i), xcnt=cnt2)
            if cnt2 == n:
                break
            if len(temp_guesses) == i:
                t_i = 0
        
        print ("Guess Count: ",cnt2)
        if cnt2 == n:
            #if lucky_save != temp_arr2:
            #lucky_out_list.append(temp_arr2[:])
            lucky_guess = i
            lucky_cnt += 1
            
    print("lucky count", lucky_cnt)
    #for i in lucky_out_list:
    #    print('sample result')
    #    for rw in i:
    #        tempstr.append(' '.join(rw))
    #    print('\n'.join(tempstr))
    #    tempstr.clear()
    temp_arr, to_solve, cnt, passed = test_game(temp_arr, to_solve)


    if lucky_cnt == 0 or lucky_cnt > 1:
        print ('?')
    #else:
    #for _ in range(2):
    #    temp_arr, to_solve, cnt, passed = test_game(temp_arr, to_solve, mark=lucky_guess, xcnt=cnt)

    #put together
    for rw in temp_arr:
        tempstr.append(' '.join(rw))
    return '\n'.join(tempstr)

gamemap = """
0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0
0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
? ? ? 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 0 0
? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0
? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0
? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 0 0 0 0
""".strip()
result = """
0 0 0 0 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 0 0 0 0 2 x 2 1 x 1 0
1 1 1 0 0 0 0 1 1 1 0 0 0 0 1 1 2 x 1 0 0 0 0 2 x 2 1 1 1 0
1 x 1 1 1 1 0 1 x 2 1 1 0 0 1 x 2 1 1 0 0 0 0 1 1 1 0 0 0 0
1 2 2 3 x 2 0 1 1 2 x 1 0 0 1 2 2 1 0 0 0 0 0 1 1 1 0 0 1 1
0 1 x 3 x 2 0 0 0 1 1 1 0 1 2 3 x 1 0 0 0 0 0 1 x 1 0 0 1 x
0 1 1 3 3 3 2 1 1 1 1 2 1 2 x x 2 2 1 1 0 0 0 1 1 1 1 1 2 1
0 0 0 1 x x 2 x 1 1 x 2 x 2 3 3 3 2 x 1 0 1 1 1 0 0 2 x 2 0
0 1 1 2 2 2 3 2 2 1 1 2 1 1 1 x 2 x 2 1 0 1 x 1 0 0 2 x 2 0
1 2 x 1 0 1 2 x 1 0 0 0 1 1 2 2 3 2 1 0 0 1 1 1 0 0 1 1 1 0
1 x 2 1 0 1 x 3 2 1 0 0 1 x 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 0
1 1 2 1 2 2 2 2 x 1 0 0 1 1 1 1 2 x 1 0 0 0 1 x 2 1 0 0 0 0
1 1 2 x 2 x 1 1 1 1 0 0 0 0 1 1 2 1 1 0 0 0 1 2 x 1 0 0 0 0
1 x 3 2 2 1 1 0 0 1 1 1 0 0 1 x 1 0 0 0 0 0 1 2 2 1 0 0 0 0
1 2 x 1 0 0 0 0 0 1 x 1 0 0 1 1 1 0 0 0 0 0 1 x 1 0 0 0 0 0
""".strip()

print(solve_mine(gamemap, count(result)))
#game.read(gamemap, result)
#makeAssertion(solve_mine(gamemap, game.count), result)