'''
x = 0
y = 5
for i in range(x, y):
	print(i)
	y = 10
	print(i)
print (y)
'''
#-------------------

'''
for i in range(5):
	print(i)
	i = 10
	print(i)

#-----------------------
'''

'''
x = [10, 20, 30]
for i in x:
	print(i)
	i += 100
	print(i)
print(x)
'''
#-------------------------

'''
x = [[10], [20], [30]]
for i in x:
	print(i)
	i = i + [100]
	print(i)
print(x)
'''
#--------------------------

'''
x = [[10], [20], [30]]
for i in x:
	print(i)
	i += [100]
	print(i)
print(x)
'''
#-----------------------------

'''
x = [[10], [20], [30]]
for i in x:
	print(i)
	i = [200, 300]
print(x)
'''
#-----------------------------

'''
x = [10, 20, 30]
for i in x:
	print(i)
	x.append(40)
print(x)
'''
#--------------------------

'''
x = [10, 20, 30]
for i in x:
	print(i)
	x.append(40)
	x = [50, 60]
print(x)
'''
#--------------------

