class Person:
    # class variable
    people_count = 0

    """Initialises an object of a class"""

    def __init__(self, name, age):
        # instance variable to access a class varaible you use the name of the class
        # to use an instance varaible you use
        # can access class variable thru instance

        self.name = name
        self.age = age
        Person.people_count += 1

        """
        The repr method suggests the format of outpu
        """

    def __repr__(self):
        return "<Object: {},  {}>".format(self.name, self.age)

        print "Object created"

    def say_hello(self):
        return "Hello, I'm {}  and I'm {} y/o".format(self.name, self.age)
