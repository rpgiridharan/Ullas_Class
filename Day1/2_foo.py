# assignment!

# dynamic typing: type of variable depends on the value associated with it (this works because type descriptor not attached to variable but to object it is pointing to).
# garbage collection: this is done automatically. You don't have to say free.
# reference count: This is the algo that Python uses.
# reference count: each object has a number telling how many links are there to it
# every time a new var is assigned to an existing object, reference count increments by 1
#   every time a var is changed to refer to something else, the original object's
#   reference count decrements by 1
# if rc == 0 => object is garbage. Immediately freed* (* - this is only theoretically so. Different implementations of Python can choose not to do it immediately as an optimization).


# assignment:
# works from right  to left
# creates an object of RHS if it is not already there*
#		* - not completely true, will explore this in depth later

# then assigns the variable on LHS to point to object




a = 10
b = 10
a = 20
print(a)
# use of a variable without initialization is ALWAYS ERROR!
#print(b)
#a = "Hello"
print(b)


