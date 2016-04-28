
def super_sum(*args):
    """
    Returns the sum of numbers e.g

    super_sum(2,3,4) ===> 9 ---tuples
    super_sum([12, 10, 20]) === 0
    super_sum([2],[3],[4]) ===> 9

    """
    total = 0
        if args:
            for x in args:
                # x is now ([1, 2, 3])
                if type(x) == list:
                    total += sum(x)
                elif type(x) == str:
                    return 0
                else:
                    total += x

            return total
        return 0

