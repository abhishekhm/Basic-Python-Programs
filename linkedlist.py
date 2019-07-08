class Node:
	def __init__(self,data):
		self.data=data
		self.next=None


class LinkedList:

	def __init__(self):
		self.head=None

	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node


	def printlist(self):
		temp=self.head
		while(temp!=None):
			print(temp.data,"-----",temp.next)
			temp=temp.next

	def getcount(self):
		temp=self.head
		count=0
		while(temp!=None):
			count+=1
			temp=temp.next
		return count

	def removefromlist(self,element):
		temp=self.head
		while(True):
			last_node=temp
			temp=temp.next
			if(element==temp.data):
				last_node.next=temp.next
				return

	def elementinlist(self,element):
		temp=self.head
		c=1
		while(temp!=None):
			if(element==temp.data):
				print("Element ",temp.data," found in position ",c)
			temp=temp.next
			c+=1


	def stackdelete(self):
		temp=self.head
		a=temp.next
		self.head=a

	def queuedelete(self):
		temp=self.head
		count=0
		while(temp!=None):
			count+=1
			temp=temp.next
		n=count-2
		temp=self.head
		if(count==0):
			print("The queue is empty")
		elif(count==1):
			return None	
		else:
			while(n!=0):
				temp=temp.next
				n-=1
			temp.next=None


a=LinkedList()

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.printlist()

a.elementinlist(4)
print(a.getcount())
# a.stackdelete()
a.stackdelete()
# a.queuedelete()
a.printlist()
print(a.getcount())





