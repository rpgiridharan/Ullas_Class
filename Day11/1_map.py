# functional programming

# functions become "first-class citizens" 

# map
# input: n elements
# output: n elements
import math
a = [10, 20, 30]
b = [2, 5, 6]

# generators

print(list(map(math.sqrt, a)))

print(list(map(lambda x: x*x, a)))

# map can take multiple iterables
# if there are n iterables, the callable should take n args

print(list(map(int.__truediv__, a, b)))

