# [expr form item in list]

doubles = [i * 2 for i in range(10)]
print(doubles)


doubles = []

# without use list comprehension
for i in range(10):
    doubles.append(i*2)

print(doubles)

