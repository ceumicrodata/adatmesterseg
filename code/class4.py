def noop():
    pass

print "noop", noop()

def is_divisible(a, b):
    if int(a / b) * b == a:
        return True
    else:
        return False

print "is_divisible", is_divisible(8, 3)
print "is_divisible", is_divisible(8, 2)

def is_divisible(a, b):
    return int(a / b) * b == a

print "is_divisible", is_divisible(8, 3)
print "is_divisible", is_divisible(8, 2)


list1 = ['', 1, None]
list2 = list1
list1.append('surprise')
print list2

list1.reverse()
print list1

list1.sort()
print list1

print list1 + list2

list1.extend([1, 2, 3])
print list1
#print dir(list)
print 'surprise' in list1

# ciklus:
#     favagas
#     kovetkezo_fahoz_menes

forest = [1, 2, 3, 4, 5, 6]
def cut_tree(tree):
    print 'tree', tree

# tree_index = 0
# cut_tree(forest[tree_index])
# tree_index = 1
# cut_tree(forest[tree_index])
# tree_index = 2
# cut_tree(forest[tree_index])

# tree_index = 0
# cut_tree(forest[tree_index])
# tree_index = tree_index + 1
# cut_tree(forest[tree_index])
# tree_index = tree_index + 1
# cut_tree(forest[tree_index])
# tree_index = tree_index + 1
# cut_tree(forest[tree_index])
# tree_index = tree_index + 1
# cut_tree(forest[tree_index])
# tree_index = tree_index + 1
# cut_tree(forest[tree_index])

tree_index = 0
while tree_index < len(forest):
    tree = forest[tree_index]
    cut_tree(tree)
    tree_index = tree_index + 1

for tree_index in [3, 2, 1, 0]:
    cut_tree(forest[tree_index])
    if tree_index == 1:
        break

for tree in forest:
    cut_tree(tree)

def new_matrix(rows, columns):
    matrix = [ [0] * columns for i in range(rows)]
    return matrix

assert new_matrix(2, 3) == [[0, 0, 0], [0, 0, 0]]
assert new_matrix(3, 4) == [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

print new_matrix(3, 4)


def new_matrix(rows, columns):
    matrix = []
    row_num = 0
    while row_num < rows:
        row = [0] * columns
        matrix.append(row)
        row_num = row_num + 1
    return matrix


print new_matrix(3, 4)

matrix = new_matrix(3, 4)
matrix[1][2] = 1
print matrix


def print_matrix(matrix):
    print '0000'
    print '0010'
    print '0000'

print_matrix(matrix)

def print_matrix(matrix):
    print 0,
    print 0,
    print 0,
    print 0
    print 0,
    print 0,
    print 1,
    print 0
    print 0,
    print 0,
    print 0,
    print 0

print_matrix(matrix)
print len(matrix)
