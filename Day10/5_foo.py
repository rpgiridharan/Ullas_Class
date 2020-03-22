# variable-number of args (positional)

# *-parameters will collect any number of positional arguments into a tuple
def f(*a):
	print(a)

f()
f(10)
f(10, 20, 40)

def f(a, b=20, *c):
	print(a,b,c)

f(10, 20, 30)
f(10)
#f(10, 30, c=(4000, 2000)) # no keyword parameter for *param

# any parameters listed after the *-parameter
#  become keyword-only parameter
def f(*c, a, b=20):
	print(a,b,c)
f(10, 20, 30, a=100, b=30)



# def print(*args, sep=" ", ):
def f(*, a, b, c):
	pass

#f(10, 20, 30) # error. this function does not take any positional parameters. only keyword





