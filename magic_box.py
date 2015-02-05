# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_wishes(mat):
    wish = 0
    for x in mat:
        if x.count('P') == len(mat[0]) or x.count('T') == len(mat[0]):
            wish += 1
    return wish


def flip(mat, cols):
    r = range(len(mat))
    c = range(len(mat[0]))
    for j in c:
        if j in cols:
            for i in r:
                if mat[i][j] == 'P':
                    mat[i][j] = 'T'
                else:
                    mat[i][j] = 'P'

def magic_box(mat):
    cols = {}
    max_wish = []
    prev_mat = mat
    for x in mat:
        cols.clear()
        if x.count('P') > x.count('T'):
            for i in range(len(x)):
                if x[i] == 'T':
                    cols[i] = 1
            flip(mat, cols)
        else:
            for i in range(len(x)):
                if x[i] == 'P':
                    cols[i] = 1
            flip(mat, cols)
        max_wish.append(get_wishes(mat))
        mat = prev_mat
    return max(max_wish)

dim = raw_input().split(' ')
row, col = int(dim[0]), int(dim[1])
mat = []
while row > 0:
    R = []
    line = raw_input()
    for x in line:
        R.append(x)
    mat.append(R)
    row -= 1
print mat
print magic_box(mat)
