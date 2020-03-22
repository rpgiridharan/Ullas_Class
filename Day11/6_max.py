# write your own max

a = [92, 123, 45, 56, 78, 23]

import functools
print(functools.reduce(lambda x, y: x if x>y else y, a))
