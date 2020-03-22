def f(a, b):
	print(a,b)

#f(*(10, 20, 30)) # unpacking
def f(dd, mm, yy):
	print(dd, mm, yy)

a = input("Enter the date: ") # a = 'dd-mm-yy'
b = a.split("-") # ['dd', 'mm', 'yy']

f(a[0], a[1], a[2])
f(*b)
