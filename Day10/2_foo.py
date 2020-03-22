#parameter-passing techniques

# default-parameters

def f(a,b):
	print(a,b)

#f(10)
#f(10,20,30)
# default parameters
#  allow us to skip parameters
# 



def f(a, b=10, c=20): # assignment in def
	print(a,b, c)

f(20)
f(20,30)

# default parameters have to be rightmost
def g(a=10, b, c=20):	#error
	print(a,b,c)

g(20,30)







