a=[5,1,3,2,4,1,56,22,78,25,6,45,100,9]

def insertionsor(a):
	l=len(a)
	for i in range(1,l):
		key=a[i]
		j=i-1
		while (j>=0 and key<a[j]):
			print(a)
			a[j+1]=a[j]
			j=j-1
		a[j+1]=key


insertionsor(a)
print(a)




