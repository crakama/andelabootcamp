"""
You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77

"""


def find_missing(array_a, array_b):
    if array_a or array_b == []:
        return 0
    elif len(array_b) > len(array_a):
        diff2 = list(set(array_b) - set(array_a))
        return diff2
    else:
        for i in array_a:
            if i not in array_b:
                diff = list(set(array_b) - set(array_a))
                return diff
