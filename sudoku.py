import numpy as np

val = set((1,2,3,4,5,6,7,8,9))
sections = [[0,1,2],[3,4,5],[6,7,8]]
loc = lambda a: [n[0] for n in sections if a in n][0]
possible_val = lambda r, c, s: val.difference(r).difference(c).difference(s)

def update_tosolve(i, j, temp_dict, puzzle):
    row = set(puzzle[i:i+1,:][0])
    col = set(puzzle[:,j:j+1].ravel())
    r = loc(i)
    c = loc(j)
    cube = set(puzzle[r:r+3, c:c+3].ravel())
    temp_dict['{}:{}'.format(i,j)] = possible_val(row, col, cube)
    return temp_dict

def sudoku(puzzle):
    h = len(puzzle)
    if h == 0:
        return []

    l = len(puzzle[0])
    puzzle = np.array(puzzle)
    to_solve = {}

    for i in range(h):
        for j in range(l):
            if puzzle[i,j] == 0:
                to_solve = update_tosolve(i, j, to_solve, puzzle)

    while len(to_solve) > 0:
        keys = sorted(to_solve, key=lambda a: len(to_solve[a]))
        for key in keys:
            if len(to_solve[key]) > 1:
                break

            puzzle[int(key[0]), int(key[-1])] = to_solve[key].pop()
            del to_solve[key]

        temp = {}
        for key in to_solve:
            i = int(key[0])
            j = int(key[-1])
            temp = update_tosolve(i, j, temp, puzzle)
        
        to_solve = temp
    
    print(puzzle)
    return puzzle.tolist()

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
          
sudoku(puzzle)