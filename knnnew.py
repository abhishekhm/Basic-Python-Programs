from math import sqrt
import pandas as pd
from sklearn import preprocessing

def cdist(a,b):
	x=b[0]-a[0]
	y=b[1]-a[1]
	ans=sqrt((x**2)+(y**2))
	return ans

def sorta(a):
	b=sorted(a)
	return b

def returnkvalues(a,k):
	return(a[0:k])

def calcdist(train,test):
	b=[]
	l=len(train)

	for i in range(l):
		b.append(0)
	for i in range(l):
		k=cdist(test,train[i])
		b[i]=[k,train[i][2]]
	return b

def calcypred(a):
	l=len(a)
	sum=0
	for i in range(l):
		sum=sum+a[i][1]
		# print(a[i][1])
	ans=sum/l
	return ans

def knn(train,test,kvalue):
	b=calcdist(train,test)
	b=sorta(b)
	val1=returnkvalues(b,kvalue)
	ans=calcypred(val1)
	# print(ans)
	return ans


def knnwithrmse(train,test,k):
	a=[]
	residual=[]
	for i in range(len(test)):
		a.append(0)
		residual.append(0)

	for i in range(len(test)):
		t=[test[i][0],test[i][1]]
		ans=knn(train,t,k)
		a[i]=ans
	
	for i in range(len(test)):
		residual[i]=(a[i]-test[i][2])**2

	#print(sum(residual))
	#print(len(residual))
	a=sum(residual)/len(residual)
	final=sqrt(a)
	print("The RMSE is: ",final)
	return


# train=[[6,6,135],[5,5,123],[6,5,140],[1,1,50],[2,2,68]]
# test=[[6,6,200],[5,7,113],[1,2,40],[2,3,70],[2,9,268]]
# testpoint=[4,4]

# print(knn(train,testpoint,3))
# knnwithrmse(train,test,3)

df = pd.read_csv("nba.csv")

x=df.drop(['pos','age','bref_team_id','g','gs','mp','fg','fga','fg.','x3p','x3pa','x3p.','x2p','x2pa','x2p.','efg.','ft','fta','ft.','orb','trb', 'ast', 'stl' ,'blk', 'tov', 'pts', 'season', 'season_end','player'],axis=1)
y=df.drop(['pos','age','bref_team_id','g','gs','mp','fg','fga','fg.','x3p','x3pa','x3p.','x2p','x2pa','x2p.','efg.','ft','fta','ft.','orb','drb', 'trb', 'ast', 'stl' ,'blk', 'tov', 'player', 'pf','season', 'season_end'],axis=1)
# print(x.head())
# print(y.head())
z=pd.concat([x,y], axis=1)


train_1=df1 = z.iloc[:385, :]
test_1 = z.iloc[385:, :]

a = pd.np.array(train_1)
b = pd.np.array(test_1)

# print(test_1)
# print(train_1)
knnwithrmse(a,b,19)




