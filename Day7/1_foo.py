#iterable:
# something you can "walk through"
# iterator:
#	something that does the "walking through"

# Every iterable object can obtain iterator(s) for it
# When we walk through an object, we call the iterator
# and the iterator does the walking through

# Formally, what is an iterable?
# Answer: Any object that supports the __iter__ method. 
# This __iter__ method returns back an "iterator"

# What is an iterator?
# Answer: Any object that supports the __next__ method.
# This __next__ method when called gives the next element of the iterable.
# At the end, it raises StopIteration exception.

# What if an object supports both the __iter__ and __next__ methods?
# Then that object is an iterable that is its own iterator.

# Since the iterator "walks through" the iterable,
# it is therefore the job of the iterator to keep track of 
# the position in the iterable where it is.
# Hence once the iterator has finished "walking through" the iterable
# it is done, and it cannot be reset to start from beginning.
# So, if we want to iterate over the iterable again,
# we need another iterator (by calling __iter__)

# Thus, if we have an iterable object which is its own iterator,
# then, walking through the iterable once via the iterator will exhaust traversal.
# This iterable object, since it is its own iterator,
# cannot be asked to give more iterators.
# All calls to __iter__ on this iterable will give back the same iterable as iterator.
# This object only can be traversed once.

# Examples of such iterables which are their own iterators: zip object, file object, enumerate object, generator object, ...

a = [10,20,30]
t = '''
for i in a:
	print(i)
	print(i*2)
'''
'''
a is iterable
it = get the iterator for a
until the iterable does not exhaust itself:
	keep asking "it" to give next element
	assign this next element to i
'''

a = [10,20,30]
# iteration protocol
s = '''
temp = a.__iter__()
while True:
	try:
		# Below not ok because we will walk through further than intended
		#print(temp.__next__())
		#print(temp.__next__()*2)
		i = temp.__next__()
	except StopIteration:
		break
	print(i)
	print(i*2)
'''
import timeit
print(timeit.timeit(stmt=s, number=1000, setup="a=[10,20,30]"))
#print(timeit.timeit(stmt=t, number=1000, setup="a=[10,20,30]"))


# if an iterable is its own iterator
# 	f.__iter__ == f 
# f.__next__() 
# this exhausts itself on traversal

# contexts in which iteration protocol is used:
# list comprehension
# all constructor functions like list, tuple, set, dict, ...
# for loop
# in operator
# zip() function takes iterables
# sorted
# any, all
# functions that take iterable as parameter

