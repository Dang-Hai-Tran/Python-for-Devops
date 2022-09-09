# Create dict from a sequence of key, value
from xxlimited import new


sequence_key_value = [('name', 'Dang Hai'), ('school', 42)]
new_dict = dict(sequence_key_value)
print(new_dict)

print(new_dict.get('name'))
print(new_dict.get('age'))

# Dict comprehension
letter = 'abcdef'
cap_dict = {char : char.upper() for char in letter}
print(cap_dict)
