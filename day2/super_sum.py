
def super_sum(A):
	'''
     Tkeas a list A and:
                        Halves every even number
                        doubles every odd number
                        and returns the sums of all
	'''

	ls = []
	for i in A:
		if i % 2 == 0:
			nw = i /2
			ls.append(nw)

		else:
			n = i * 2
			ls.append(n)
	return sum(ls)
l = [2,3]
print super_sum(l)



def super_sum_two(A):
	total = 0
	for k in A:
		if k % 2 == 0:
			total += (k / 2)
		else:
			total += (k * 2)
	return total

a = [2,3]
print super_sum_two(a) 




