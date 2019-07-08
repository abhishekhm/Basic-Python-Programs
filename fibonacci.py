def fib(n):
	listfib=[]
	i=0
	fib1=0
	fib2=1

	while(i<n):
		if(n<=1):
			fib=fib1
		else:
			listfib.append(fib1)	
			fib=fib1+fib2
			fib1=fib2
			fib2=fib
		i=i+1

	return listfib





