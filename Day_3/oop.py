class Person:
	# class variable
	people_count = 0
	def __init__(self, name, age):
		# instance variable to access a class varaible you use the name of the class 
		# to use an instance varaible you use
		# can access class variable thru instance

		self.name = name
		self.age= age
		Person.people_count  += 1
	def __repr__(self):
		return "<Object: {},  {}>".format(self.name, self.age)

		print "Object created"
	def say_hello(self):
		return "Hello, I'm {}  and I'm {} y/o".format(self.name,self.age)

b = []

p = Person('joe', 23)
p2 = Person('felix', 23)
# print p.name
# print p.age
print p2.people_count
print p.say_hello()

a = [('jane', 23),('Cate',43),('jee', 52)]
for name, age in a:
	person = Person(name,age)
	b.append(person)
	print b

