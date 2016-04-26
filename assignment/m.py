#Concatenating data types and data structures
def add(a,b):
    if type(a) == type(b):
        print a + b
    else:
        print 'Type Error, cannot concatenate'

c= ['r']
d = ['f']
e = {1:'today',}
f = {2:'tommorrow'}
add (c,d)
add (e.items(),f.items())
add (c,f)