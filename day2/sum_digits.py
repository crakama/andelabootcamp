def sum_digits(A):

	'''
	Takes a list A, and returns the sum of all the digits in the list e.g [10, 30, 45]
	should return 1 + 0 + 3 + 0 + 4 + 5

	'''
	base = 10
	lst = []

	for i in A:
		while i > 0:

			lst.append(i % base)

			"""lst.append() function does a modulo, 45 modulo base is 5, 5 is appended to the new list
               float (\//)

			"""

			i = i // base
	
	return sum(lst)


			



ls = [10, 30, 45]
			
print sum_digits(ls)
