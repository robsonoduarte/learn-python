# [ expr form item in list if conditional]

doubles_of_even = [i * 2 for i in range(10) if i % 2 == 0]
print(doubles_of_even)


doubles_of_even = []

# without use list comprehension
for i in range(10):
    if i % 2 == 0:
        doubles_of_even.append(i*2)

print(doubles_of_even)