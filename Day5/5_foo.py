f = open("test.txt", "w")
f.write("Hello")
f.write("World")
print("Python", file=f)
print(1+2, [10,20,30], {100, 200}, "World", file=f)

