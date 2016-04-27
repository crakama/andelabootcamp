from person import Person
from kenyan import Kenyan

# ASIDE:
# Read about:
# PEP8
# Instance variables vs class varaibles

b = []

p = Person('joe', 23)
p2 = Person('felix', 23)
print p.name
print p.age
print p2.people_count
print p.say_hello()

a = [('jane', 23),('Cate',43),('jee', 52)]
for name, age in a:
	person = Person(name,age)
	b.append(person)
	print b

k = Kenyan('Anita Wanguru', 20)
# k.probe(True)
print "Is {} corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello()
		