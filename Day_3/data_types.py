def data_type(x):
	"""
	Takes in an argument, x:
	   --For an intergaer, return x ** 2
	   -- For a float, return x / 2
	   - For a string x, returns "Hello" + x
	   --- For a boolean, it returns a string "boolean"
	   --- For a long, return squareroot(x)

	"""

	if isinstance(x, int):
		return x ** 2
	elif isinstance(x, float):
		return x / 2
	elif isinstance(x, str):
		return "Hello {}".format(x)
	elif isinstance(x, bool):
		return " boolean"
	elif isinstance(x, long):
		return "Long"
	else:
		return "No data type found"

print data_type(1)
print data_type(2.5)
print data_type("Catherine")
print data_type(True)
print data_type(2 ** 32)
print data_type(2 ** 30)