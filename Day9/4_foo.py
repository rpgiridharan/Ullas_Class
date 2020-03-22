# factory-functions
def multiplier(x):
    def f(y):
        return x * y

    return f


twice = multiplier(2)
print(twice(5))
print(twice(10))

thrice = multiplier(3)
# closure remembers the parameter x,
# hence, multiplier(3) returns a different function object than multiplier(2)
print(thrice(4))
print(thrice(5))
