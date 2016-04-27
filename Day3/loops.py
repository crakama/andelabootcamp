a = [10, 40, -9, 45, 60, 89]
# stop end at stop minus 1
"Stop at -1 means going upto the previous"
for i in range(len(a) - 1, -1, -1):
    print a[i]

for i in a:

    i = len(a)
    while i > 0:
        print a[i - 1]
        i -= 1

# Looping through a list of tuples

b = [(2, 4), (5, 10), (6, 20), (50, 50)]
"""
x: 2, y:4
x: 5, y:10

"""
for k, v in b:

    print "X: {}, Y: {}".format(k, v)
