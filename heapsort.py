def heapify(a,n,i):
	largest=i
	l=2*i+1
	r=2*i+2

	if l<n and a[i]<a[l]:
		largest=l
	if r<n and a[largest]<a[r]:
		largest=r

	if(largest!=i):
		a[i],a[largest]=a[largest],a[i]
		heapify(a,n,largest)


def heapsort(a):
	n=len(a)

	for i in range(n-1, -1, -1):
		heapify(a,n,i)


	for i in range(n-1, 0, -1):
		a[i],a[0]=a[0],a[i]
		heapify(a,i,0)


a=[5,6,3,1,32,4,7,8,4,2,3,4,5,7,54,43,3,5,7,8,90]
heapsort(a)
print(a)


# b=[1,2,4,3]
# heapify(b,4,3)
# print(b)
# heapify(b,4,2)
# print(b)
# heapify(b,4,1)
# print(b)
# heapify(b,4,0)
# print(b)









