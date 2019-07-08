from functools import reduce
def average(a):
	return reduce((lambda x,y:x+y),a)/len(a)


a=[1,2,3,4,5,6,7,8,9,10]

b=range(11)
print('the average is:', average(range(11)))

