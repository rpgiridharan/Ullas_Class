'''
f1 = open("f1.txt")
f2 = open("f2.txt")
s1 = f1.readlines()
s2 = f2.readlines()
print(set(s1) & set(s2))
'''

print(set(open("f1.txt")) & set(open("f2.txt")))

# f.seek(0)
#	=> f.seek(0, 0)
# f.seek(-1, 2)
# f.seek(10, 2)
# f.seek(2)
