# converting first to decimal, then to binary
def add_two_binary_numbers(num1, num2):
	sum = int(num1,2) + int(num2,2)
	binary_sum = bin(sum)
	return str(binary_sum[2:])

# print(add_two_binary_numbers("100", "1"))
# print(add_two_binary_numbers("11", "1"))
# print(add_two_binary_numbers("1", "0"))
