a = 10	# if we comment this line out, the following line will give error.
def f(x, y=a):
	print(x,y)

# remember, defaults are evaluated while processing def. Only once.
# hence at the time of encountering def statement, it checks the value of a, and binds that
# to the value of y.
# any changes to a made later on will not affect the default value given above.
# if we had commented out the first line, (a=10), then 
# def would have given an error, because at that point, there was no name called a.

#f(100)
#f(200, 300)
a = 500
f(20)

