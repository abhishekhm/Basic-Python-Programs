a=[5,3,2,1,4,64,2,1,8,6,45]

def selectionsort(a):
	l=len(a)
	for i  in range(l):
		mina=i
		for j in range(i+1,l):
			if(a[mina]>a[j]):
				mina=j
		a[i],a[mina]=a[mina],a[i]

	return(a)

selectionsort(a)
print(a)


