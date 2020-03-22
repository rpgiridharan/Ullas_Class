def f(a, b=[]):
	print(a, b)
	b.append(10)

#f(10)
#f(10, 20)

# defaults get evaluated at the time of def
# not at the time of call!
# so, the following will print "Hello" just once, at the time of def
def f(a=print("Hello")):
	print(a)

#f(10)
##f(20)
#f()
#f()



def f(a, b=[]):
	print(b)
	b.append(a)

f(10)
f(100, [20])
f(200, [30])
f(400)

f(500)









