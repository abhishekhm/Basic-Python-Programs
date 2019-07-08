a=[5,1,3,2,4,1,56,22,78,25,6,45,100,9]

def bubblesort1(a):
	count=len(a)
	for x in range(count):
		flag=False
		for y in range(count-x-1):
			if(a[y]>a[y+1]):
				temp=a[y+1]
				a[y+1]=a[y]
				a[y]=temp
				flag=True
		if(flag==False):	break
	return a

c=bubblesort1(a)
print(c)




