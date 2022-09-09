# Sequence method
my_sequence = "Bill Cheatham"
print(my_sequence.index("eat"))
print(min(my_sequence))
print(max(my_sequence))
print(my_sequence.count("a"))

# Sequence slicing
new_sequence = my_sequence[2:9:2]
print(new_sequence)

# List
pies = ["cherry", "apple"]
pies.append('rhubarb')
print(pies)
pies.insert(2, 'cream')
print(pies)

desserts = ['cookies', 'paste']
desserts.extend(pies)
print(desserts)
print(desserts.pop(3))
print(desserts)
desserts.remove('paste')
print(desserts)

# List comprehension
square = [i**2 for i in range(10)]
print(square)

# String
new_string = str(desserts)
print(new_string)
print(new_string[:9])

output = "Barry"
print(output.ljust(10, '*'))
print(output.rjust(10, '*'))

name = "Dang Hai"
print(name.swapcase())
print(name.upper())

values = {'first': 'Bill', 'last': 'Bailey'}
print("Won't you come home {first} {last}?".format(**values))
