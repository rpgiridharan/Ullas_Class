# reduce

# input:  n elements
# output: 1 element

a = [10, 20, 30, 40]

# reduce :
# callable: fn that takes two parameters
# a = [a1, a2, a3, ...]
# reduce(f, a) => f(f(f(a1, a2), a3), a4)
import functools
print(functools.reduce(int.__add__, a))
