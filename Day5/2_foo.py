# file-handling
f = open("animals.py") # if you don't give second parameter
#		it means you want to read the file

a = f.readlines()
print(a)
a = f.readlines()
print(a)

# You can only read a file once!!!
f.seek(0)
# Unless you seek back to the beginning.
# Reason: There is only one file offset variable that keeps track of
#	position in file from where to read/write.
print(f.readline())	#Calling any of the read/readline/readlines will advance this offset
print(f.readlines())
