# Recursive solution
def reverse_string(str):
	if len(str) == 0:
		return str

	else:
		return reverse_string(str[1:]) + str[0]

print(reverse_string("Demilade"))

# Using the Python slicing method
def reverse_string_slice(str):
	reversed_str = str[::-1]
	return reversed_str

# print(reverse_string_slice("Cat"))
# print(reverse_string_slice("The Daily Byte"))
# print(reverse_string_slice("civic"))
