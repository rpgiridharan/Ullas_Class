# dict: has key-value pairs
# index a dictionary only based on key
# if you access a non-existent key, gives error
# 	however, assignment to a non-existent key creates a key
# keys of dict must be immutable
# values of dict need not be immutable
# dict is iterable
# unit of iteration is key
# so we can use in operator on a dict
#	it checks if a key exists in the dict
f = open("books.txt")
d = {}
for line in f:
	author, book = line.rstrip().split("-")
	if author not in d:	
		d[author] = [] # 0
	d[author].append(book)	# += 1
print(d)
print(d["J. K. Rowling "])
