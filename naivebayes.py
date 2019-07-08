inputarray=[['sunny',0],['overcast',1],['rainy',1],['sunny',1],['sunny',1],['overcast',1],['rainy',0],['rainy',0],['sunny',1],['rainy',1],['sunny',0],['overcast',1],['overcast',1],['rainy',0]]
inputvar=['sunny','rainy','overcast']

def freqtab(inputarray,inputvar):

	new=[]

	for i in inputvar:
		a=[i,0,0]
		new.append(a)

#code applicable only for 3 input variables: need to rewrite the code
	for i in inputarray:
		if(i[0]==inputvar[0] and i[1]==1):
			new[0][1]=new[0][1]+1
		elif(i[0]==inputvar[0] and i[1]==0):
			new[0][2]=new[0][2]+1
		elif(i[0]==inputvar[1] and i[1]==1):
			new[1][1]=new[1][1]+1
		elif(i[0]==inputvar[1] and i[1]==0):
			new[1][2]=new[1][2]+1
		elif(i[0]==inputvar[2] and i[1]==1):
			new[2][1]=new[2][1]+1
		elif(i[0]==inputvar[2] and i[1]==0):
			new[2][2]=new[2][2]+1

	l=len(new)
	new.append([0,0,0])
	sum1=0
	sum2=0
	for i in range(len(new)-1):
		sum1=sum1+new[i][1]
		sum2=sum2+new[i][2]
	new[l][0]='Total'
	new[l][1]=sum1
	new[l][2]=sum2
	print("Frequency: ")
	print("  X          P(X|Yes)               P(X|No)")
	print(new[0][0],"    : ",new[0][1]/new[3][1],"   ",new[0][2]/new[3][2])
	print(new[1][0],"    : ",new[1][1]/new[3][1],"   ",new[1][2]/new[3][2])
	print(new[2][0]," : ",new[2][1]/new[3][1],"   ",new[2][2]/new[3][2])
	return new


def likelihoodtab(inputarray,inputvar):
	a=freqtab(inputarray,inputvar)
	l=len(a)
	total=a[l-1][1]+a[l-1][2]

	newcol=[]
	newrow=[0,0]
	sum1=0
	sum2=0


	for i in range(len(a)-1):
		newcol.append(0)

	for i in range(len(a)-1):
		newcol[i]=(a[i][1]+a[i][2])/total
		sum1=sum1+a[i][1]
		sum2=sum2+a[i][2]

	newrow[0]=sum1/total
	newrow[1]=sum2/total

	print("\nLikelihood:")
	print("  X          P(X)")
	print(a[0][0],"    : ",newcol[0])
	print(a[1][0],"    : ",newcol[1])
	print(a[2][0]," : ",newcol[2])
	print("P(Yes)    : ",newrow[0])
	print("P(No)     : ",newrow[1])




a=likelihoodtab(inputarray,inputvar)


#Eg: probability that players will play if it is raining
#P(Yes|Rain)=(P(Rain|Yes)*P(Yes)) 
#(0.22*0.64)/0.357

ans=(0.22*0.64)
print("\nProbability that players will play if it is raining: ",ans)

