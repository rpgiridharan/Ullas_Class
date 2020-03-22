# file-handling
f = open("animals.py") # if you don't give second parameter
#		it means you want to read the file

s = f.readline()[:-1]	# reads a line along with \n
print(s)
while s:
	s = f.readline().rstrip()	# reads a line along with \n
	print(s)

