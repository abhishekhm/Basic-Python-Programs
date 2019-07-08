listofyears=[]
i=0
while(i!=201):
	listofyears.append(1850+i)
	i+=1

listofleap2=list(filter(lambda year:(year%4==0 or year%400==0) and (year%100!=0),listofyears))

print(listofleap2)


