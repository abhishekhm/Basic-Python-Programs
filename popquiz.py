from functools import reduce

a1=["     sam", "sam             ","    sam  ","sam","             sam sam"]




def countsam(a):
	lena=len(a)
	i=0
	count=0
	while(i!=(lena-2)):
		if(a[i:i+3]=="sam"):
			count+=1
		i+=1

	return count


print(reduce(lambda a,x:a+x.count('sam'),a1,0))


