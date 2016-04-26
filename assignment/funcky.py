def funky(a,b):
    if type(a) and type(b) == dict:
        print "Cant add dictionaries"
    else:
        print a + b

funky([1,2,3],[2,3,4])
funky("toni","joy")
funky({1:"mangoes", 2:"apples"},{3:"pears",4:"oranges"})