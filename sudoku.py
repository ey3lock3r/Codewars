puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def cross(A, B):
    return [(a,b) for a in A for b in B]


def sudoku(puzzle):
    row = '012345678'
    col = row

    squares = cross(row, col)
    print ([cross(rs, cs) for rs in ['ABC','DEF','GHI'] for cs in ['123','456','789']])

    return puzzle

sudoku(puzzle)