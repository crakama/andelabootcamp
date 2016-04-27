people = {

    ("Joe", 58),
    ("Phoebe", 45),
    ("Brain", 7)
}


def super_sum(*args):
    return sum(args)


def hello_again(name, age):
    """    """
    return "I am {} and {} years old".format(name, age)


def max_min(A):
    """ Returns Max value - Min value [10,20,30,30,40] """

    max_, min_ = A[0], A[0]

    for i in A:
        if i > max_:
            max_ = i
        elif i < min_:
            min_ = i
    return max_ - min_

lst = [10, 20, 30, 30, 40]
print max_min(lst)
