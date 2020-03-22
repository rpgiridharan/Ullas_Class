a = [10,20,30]

# Given an iterable a, 
# every for loop of the following form
# for i in a:
#	stmts
# is equivalent to the following:
'''
temp = a.__iter__()
while True:
	try:
		i = temp.__next__()
	except StopIteration:
		break
	#stmts
'''
