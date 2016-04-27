
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
            nw = i / 2
            ls.append(nw)

        else:
            n = i * 2
            ls.append(n)
    return sum(ls)
l = [2, 3]
print super_sum(l)


def super_sum_two(A):
    total = 0
    for k in A:
        if k % 2 == 0:
            total += (k / 2)
        else:
            total += (k * 2)
    return total

a = [2, 3]
print super_sum_two(a)


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
            i = i // base

    """
	    lst.append() function does a modulo, 45 modulo base is 5, 5 is appended to the new list
        i is assigned to the float (//) of i and base, which is 4, 4 is again appended to the list
        since the while loop is still evaluating to True. 

        The loop evaluates to False when all the values has been appended to the list. The for loop now
        continues with the iteration.

	"""

    return sum(lst)


ls = [10, 30, 45]

print sum_digits(ls)
