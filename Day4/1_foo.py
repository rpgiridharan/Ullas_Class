# To check if a given string is a palindrome
s = "aibohphobia"
'''
#s = "testcase"
a = list(s)	# ctor creates a new object
b = list(a)
b.reverse()
print(a == b)
'''

# Assignment for all:
#  find out the black magic behind slicing!

# slice of a sequence:
# a[x:y:z]
# a[x:]
# a[:y:]

# a[::]
# gives a copy of a subsection of a list
#     from index x upto but not including y
# has defaults: x -> 0; y->len(list);  if z->1
# if step size is -ve, then swap x and y's defaults

s = "aibohphobia"
#s = "testcase"

print(s[::-1] == s)






