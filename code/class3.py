# coding: utf-8

# comment
from __future__ import division

# None
print None

# integer
print (1 + 2) * 3
print 1 / 2
print 3 / 2
print 10 ** 200

# float
print 1.
print 1e10
print 0.1 * 8
print 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1

import math
print math.sin(math.pi)

# sequences
# tuples
print (1, 2)
print (1, (2, 2), 3)
print len((1, 2))
print (1, 2) + (3, 4)
print (1, 2, 3, 4)[3]
print (1, 2, 3, 4)[0:2]
print (1, 2, 3, 4)[:2]
print (1, 2, 3, 4)[2:]
print (1, 2, 3, 4)[:]
print (1, 2) * 3
print (1,)
print len(())

print tuple()
print tuple((1, 2))

# {f(x) | x in N : P(x)}
# {2 * x | x in N}

# list comprehension
print tuple(2 * x for x in (1, 2, 3, 4, 5))
print tuple(2 * x for x in (1, 2, 3, 4, 5) if x < 3)

# string
print 'string'
print "string"
print '''\
1
2
3
'''

print tuple('string')
print 'Tenfergo Tobias'[7:]
print str((1, 2))
# print '1' + 2

print 'a {} b {} c'.format(1, 2)
print str(str)

# names
tukorfurogep = 'árvíztűrő tükörfúrógép'
print tukorfurogep
print len(tukorfurogep)

# functions

def noop():
    pass

print noop()

def identity(x):
    return x

print identity(tukorfurogep)

assert tukorfurogep == identity(tukorfurogep)

def abs(x):
    if x < 0:
        return -x
    return x

print abs(-1), abs(0), abs(3)

def add_tuples(t1, t2):
    if t1 == ():
        return t2
    if t2 == ():
        return t1
    return (t1[0] + t2[0],) + add_tuples(t1[1:], t2[1:])

assert add_tuples((1, 2), ()) == (1, 2)
assert add_tuples((), (1, 2)) == (1, 2)
assert add_tuples((1,), (8, 10)) == (9, 10)
assert add_tuples((1, 2), (8, 9, 10)) == (9, 11, 10)
print 'Tenfergo Tobiasián'.split('e')
print ' ** '.join(('words', 'and', 'worms'))

# Boolean
True 
False
print 1 > 2
print 2 > 1

print bool(1)
print bool(0)
print bool(bool)

def is_divisible(x, y):
    if x == 8 and y == 2:
        return True
    return False

assert is_divisible(8, 2)
assert not is_divisible(8, 3)
assert not is_divisible(1, 2)

assert limited_name('x y') == 'x y'
assert limited_name('xxxxxxxxxxxxxxxx yyy') == 'yyy'

assert reversed('asd') == 'dsa'