def add_two(a, b):
    """
       add_two is a function that prints out the sum of the two numbers
       a and b
    """
    # import pdb; pdb.set_trace()
    if type(a) and type(b) == int:

        return a + b

    else:

        return "Please enter an integer as an argument"

add_two(1, "nyakios")

add_two(1, 23)


def add_one(a, d):
    """
       add_one is a function that prints out the sum of the two numbers
       a and d
    """

    return " The sum of {} and {} is:".format(a, d)

add_one("a", "c")

ls = [1, 2, 3, 4]


def funky(a, b):
    """
    This function checks the type of values of a and b 
    if it is int,float,str,list
    and does their summation. If the type is a dictionary 
    then its tested in the else statement
    """

        if isinstance(a, (int, float, str, list)) and isinstance(b, (int, float, str, list)):

            return a + b

        elif isinstance(a, dict) and isinstance(b, dict):

            sum_dict = dict(a.items() + b.items())
            return sum_dict


funky(4, 4)

funky([1, 2, 3], [4, 5, 6])

funky(3.2, 1.2)
funky("Boot", "CAMP")

dict1 = {1: "Andela", 2: "Moringa"}
dict2 = {3: "Lakehub", 4: "ihub"}
funky(dict1, dict2)
