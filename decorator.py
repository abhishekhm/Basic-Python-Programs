def mod_decorator(function):
	def inner_wrapper():
		inner_wrapper.modcount+=1
		print("This funtion is being called " + str(inner_wrapper.modcount) + " number of times")
		function()
	inner_wrapper.modcount=0
	return(inner_wrapper)

def my_function():
	print("This is my function")

decorated_function=mod_decorator(my_function)

decorated_function()