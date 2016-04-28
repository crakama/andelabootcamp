"""
to check if the array passed as an argument is arithmetic, geometric,
neither arithmetic nor geometric in progression or if the array is empty.

For arithmetic progressions, return Arithmetic
For geometric progressions, return Geometric
For neither of the above, return -1
For an empty array, return 0


"""


def arith_geo(array_):
    if len(array_) != 0:
        array_geo = []
        array_ari = []
        for i in range(len(array_) - 1):
            if array_[i + 1] == 0 or array_[i] == 0:
                array_geo.append(0)
            else:
                array_geo.append(array_[i + 1] / float(array_[i]))
            array_ari.append(array_[i + 1] - array_[i])
        array_geo = set(array_geo)
        array_ari = set(array_ari)
        if len(array_geo) == 1:
            return 'Geometric'
        elif len(array_ari) == 1:
            return 'Arithmetic'
        else:
            return -1
    return 0
