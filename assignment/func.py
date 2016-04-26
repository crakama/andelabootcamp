def add(a, b):

    """prints out the sum of the two numbers
    """
    """import pdb; pdb.set_trace()
    """
    if type(a) and type(b)==int:
        print (a+b)
    else: 
     print "Please enter an integer as an argument"    

add(1, "nyakios")
add(1, 23)



def add1(a, d):
    print a + "  " + d
add1("a", "c" )

ls=[1,2,3,4]


def funky(a, b):

	if isinstance(a, (int,float,str,list)) and isinstance(b, (int,float,str,list)):
		print a + b

	elif isinstance(a, dict) and isinstance(b, dict ):

		sum_dict = dict(a.items() + b.items())
		print sum_dict



funky( 4,4)
funky([1,2,3], [4,5,6])
funky(3.2, 1.2)
funky("Boot", "CAMP")

dict1 = {1:"Andela" , 2:"Moringa"}
dict2 = {3:"Lakehub", 4:"ihub"} 
funky(dict1, dict2)