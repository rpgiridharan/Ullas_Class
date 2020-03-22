# file-handling
f = open("animals.py") # if you don't give second parameter
#		it means you want to read the file

# file is iterable!
# unit of iteration is line
for word in f:
	print(word.rstrip())
