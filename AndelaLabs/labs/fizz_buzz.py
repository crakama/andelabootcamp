
def fizz_buzz(num):
    """
    a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz',
    or the argument it receives, all depending on the argument of the function,
    a number that is divisible by, 3, 5, or both 3 and 5, respectively.
    When the number is not divisible by 3 or 5,
    the number itself should be returned

    """




    if num % 3 == 0:

        if num % 5 == 0:

            return "FizzBuzz"

        return "Fizz"

    elif num % 5 == 0:

        return "Buzz"
    elif num % 3 or num % 5:


        return num
