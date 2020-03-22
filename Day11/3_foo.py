a = ["Python", "C", "Java", "Haskell"]

# make all strings uppercase
# and pick out those strings that are more than 5 characters

print(list(filter(lambda x: len(x) > 5, (map(str.upper, a)))))

# filter first, and on that result map
print(list(map(str.upper, filter(lambda x: len(x)>5, a))))

# [o/pexpr for var in iterable if cond]
# 
