def passwordManager(x):
	def checkPassword(y):
		return x == y
	return checkPassword

p1 = passwordManager("Hello")
print(p1("hello"))
#print(p1(exec("x = True")))
print(p1("Hello"))

p2 = passwordManager("Python")
print(p2("hello"))
print(p2("Python"))

