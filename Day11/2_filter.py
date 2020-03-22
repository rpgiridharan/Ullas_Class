# filter

# input: n elements
# output: between 0 to n elements

a = [10, 20, 82, 40, 67]

print(list(filter(lambda x: x%10==0, a)))
print(list(map(lambda x: x%10==0, a)))

