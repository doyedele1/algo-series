# converting first to decimal, then to binary
def add_two_binary_numbers(num1, num2):
	sum = int(num1,2) + int(num2,2)
	binary_sum = bin(sum)
	return str(binary_sum[2:])

# print(add_two_binary_numbers("100", "1"))
# print(add_two_binary_numbers("11", "1"))
# print(add_two_binary_numbers("1", "0"))

def addBinary(self, a: str, b: str) -> str:
	result = ''
	if len(a) > len(b):
		length = len(a)
	elif len(b) > len(a):
		length = len(b)
	else:
		length = len(a)
	a = a.zfill(length + 1)
	b = b.zfill(length + 1)
	carry = 0

	for i in range(length + 1):
		j = length - i
		sum = int(a[j]) + int(b[j])
		if carry != 0 and j < length:
			sum += carry
			carry = 0

		if sum == 0:
			result += '0'
		elif sum == 1:
			result += '1'
		elif sum == 2:
			result += '0'
			carry = 1
		elif sum == 3:
			result += '1'
			carry = 1
	return str(int(result[::-1]))
