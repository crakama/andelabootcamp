# f = [(10, 20, 40), (10, 40), (4, 5, 50)]
def super_sum(*args):
    '''
    Takes in a variable number of items,
    and returns the sum.
    e.g super_sum

    '''
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_
n = (2, 5, 45, 23)
print super_sum(*n)
print super_sum(2, 5, 45, 23)
