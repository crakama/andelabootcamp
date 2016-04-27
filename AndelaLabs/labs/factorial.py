def factorial(number):
    """
    factorial() is function factorial(number),
    take the number parameter been passed and
    return the factorial of it

    """

    if number == 0:
        # Base case
        return 1

    else:

        factorial_ = number * factorial(number - 1)

        return factorial_
