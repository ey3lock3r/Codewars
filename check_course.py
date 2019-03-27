sea_map =  ['000NN00NNN0', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            '00000000000', 
            'X0000000000', 
            '00000NN0000']

def intersept(xshp, nship, h, l):
    crash = True
    tmpA = xshp*2
    tmpB = (h - 1 - xshp)*2

    for ship in nship:
        x = set((ship, ship+1, ship-1))
        a, b = xshp, xshp + tmpB
        N = set((a,b,a+1,a-1,b+1,b-1))
        while a <= l and b <= l:
            a = b + tmpA
            b = a + tmpB
            N.update((a,b,a+1,a-1,b+1,b-1))
        
        N = set(i for i in N if i <= l)
        if len(x & N) >= 1:
            crash = False
            break
    return crash

def check_course(sea_map):
    h = len(sea_map)
    l = len(sea_map[0])
    xloc = [i for i in range(h) if sea_map[i][:1] == 'X'].pop()
    ntop = [i for i in range(l) if sea_map[0][i] == 'N']
    nbot = [i for i in range(l) if sea_map[-1][i] == 'N']
    Safe = intersept(xloc, ntop, h, l)
    if not Safe:
        return False
    else:
        xloc = h - 1 - xloc
        Safe = intersept(xloc, nbot, h, l)
    return Safe

x = check_course(sea_map)
print (x)