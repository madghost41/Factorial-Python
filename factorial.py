def factorial(num):
	fac_num = 0
	for i in range(num, 0, -1):
		fac_num *= i
		return fac_num

print(factorial(4))

	