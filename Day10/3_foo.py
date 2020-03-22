# keyword-parameters
def f(a,b,c,d):
	print(a,b,c,d)

# keyword-args have to be rightmost in call
# so both the following give errors:
#f(b=10, c=20, 30, 40)
#f(b=10, a=30, 10, 40)	


# same parameter cannot be passed more than once
# how does it check? please find out! I don't know answer myself!

#f(10,20,30,40)
#f(c=20, b=10, a=40, d=400, a=20)	# Error!

# keyword parameters are useful
# you can pass parameters by name in any order you wish

def area(length, breadth=20, height=30):
	print(length, breadth, height)

#area(10,20,30)
#area(length=20, breadth=20, height=10)
#area(height=20, breadth=20, length=10)	# can pass in any order!




area(10, height=200, breadth=10)
area(10, height=2000)	# when combined with default parameters, we can now skip middle values such as in this case letting breadth get default. Without keyword, this was not possible.
#area(10, length=20) # ERROR! length gets assigned twice

area(10,20) # we can still continue to pass positionally as well.

