# Python program to find count of subarrays with sum divisible by k.
def subCount(arr, n, k):
	mod = []
	for i in range(k + 1):
		mod.append(0)

	cumSum = 0
	for i in range(n):
		cumSum = cumSum + arr[i]
		mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1

	res = 0

	for i in range(k):
		if (mod[i] > 1):
			res = res + (mod[i]*(mod[i]-1))//2

	res = res + mod[0]
	
	return res

# print(subCount([4, 5, 0, -2, -3, 1], 6, 5))
# print(subCount([4, 5, 0, -12, -23, 1], 6, 5)