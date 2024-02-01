def factorial(num):
	fac = 1
	for i in range(num, 0, -1):
		fac *= i
	return fac

print(factorial(4))

	