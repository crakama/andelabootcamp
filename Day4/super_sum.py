
def super_sum(*args):
    """
    Returns the sum of numbers e.g

    super_sum(2,3,4) ===> 9 ---tuples
    super_sum([12, 10, 20]) === 0
    super_sum([2],[3],[4]) ===> 9

    """
    if not args:

        # return "Please Enter Numbers"
        return 0
    else:

        total = 0
        for x in args:
            total += x
        return total
