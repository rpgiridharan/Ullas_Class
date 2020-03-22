
# COW
a = [1,2,3]
b = a
c = list(a)
print(id(c), id(a), id(b))
d = a[:]
c[0] = 100
print(id(c), id(a))
print(c)
print(a)



# Ducks
# Duck-typing
# If it looks like a duck, and it quacks like a duck, then it is a duck
#print(a+b)



