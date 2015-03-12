def new_matrix(rows, columns):
    return [[0]*columns for _ in range(rows)]

original_new_matrix = new_matrix


# let's define a new - more verbose - one, that can be visualized in detail
# at http://pythontutor.com/visualize.html#mode=edit

def new_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append(new_row(columns))
    return matrix

def new_row(columns):
    row = []
    for _ in range(columns):
        row.append(0)
    return row


def print_matrix(matrix):
    rows = matrix
    for row in rows:
        print_row(row)

def print_row(row):
    row_as_string_list = [str(cell) for cell in row]
    print ''.join(row_as_string_list)


# test:
m = new_matrix(3, 4)

m[1][2] = 1
m[2][1] = 1
m[2][2] = 2
m[2][3] = 3

print_matrix(m)


# outstanding problems came to light:
# - print vs. return
# - programs are exact - read/experiment/ask to understand how things work
