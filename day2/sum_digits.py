def sum_digits(A):
    '''
    Takes a list A, and returns the sum of all the 
    digits in the list e.g [10, 30, 45]
    should return 1 + 0 + 3 + 0 + 4 + 5

    '''
    base = 10
    lst = []

    for i in A:
        while i > 0:

            lst.append(i % base)
            i = i // base

    """
        lst.append() function does a modulo, 
        45 modulo base is 5, 5 is appended to the new list
        i is assigned to the float (//) of i and base, which is 4, 
        4 is again appended to the list
        since the while loop is still evaluating to True. 

        The loop evaluates to False when all the values has been appended to the list. The for loop now
        continues with the iteration.

    """

    return sum(lst)


ls = [10, 30, 45]

sum_digits(ls)
