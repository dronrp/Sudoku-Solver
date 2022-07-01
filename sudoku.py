a = [
    [0,0,6,0,9,0,0,5,0],
    [8,3,4,0,0,5,0,0,0],
    [5,9,1,2,8,0,0,6,0],
    [0,0,0,4,3,0,0,0,2],
    [0,0,9,7,0,1,5,4,8],
    [0,0,8,5,0,0,6,7,0],
    [1,0,0,9,7,0,4,0,5],
    [0,0,3,0,0,0,0,1,6],
    [6,4,0,0,5,0,2,8,0]
]

def print_board(a):
    for i in range(9):
        if i%3 == 0:
            for k in range(13):
                print("-", end= " ")
            print()
        for j in range(9):
            if j%3 == 0:
                print("|",end=" ")
            print(a[i][j], end=" ")
        print("|")
    
    for i in range(13):
        print("-", end=" ")
    print("\n\n")

def nxtCell(a):
    for i in range(9):
        for j in range(9):
            if a[i][j] == 0:
                return [i, j]
    return None

def check(a, row, col, num):
    for i in range(9):
        if (i != col and a[row][i] == num):
            return False
        if (i != row and a[i][col] == num):
            return False

    qx = row//3
    begin_x = qx*3
    qy = col//3
    begin_y = qy*3

    for i in range(begin_x, begin_x+3):
        for j in range(begin_y,begin_y+3):
            if i == row and j == col: 
                continue
            if a[i][j] == num:
                return False
    return True

def solve(a):
    nxt = nxtCell(a)
    if nxt == None:
        return True
    else:
        r = nxt[0]
        c = nxt[1]
    for i in range(1, 10):
        if check(a, r, c, i):
            a[r][c] = i
            if solve(a):
                return True
            a[r][c] = 0
    return False
 
def main():
    print_board(a)
    solve(a)
    print_board(a)

main()