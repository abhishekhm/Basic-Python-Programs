class Tree:
	def __init__(self,value,left=None,right=None):
		self.value=value
		self.right=right
		self.left=left


	def insert(self,value):
		if(self.value):
			if(value<self.value):
				if(self.left==None):
					self.left=Tree(value)
				else:
					self.left.insert(value)
			elif(value>self.value):
				if(self.right==None):
					self.right=Tree(value)
				else:
					self.right.insert(value)
		else:
			self.value=value

	def printtree(self):
		if(self.left):
			self.left.printtree()
		print(self.value)
		if(self.right):
			self.right.printtree()

	def findval(self,value):
		if(value<self.value):
			if(self.left==None):
				print(value," not found")
			else:
				return self.left.findval(value)
		elif(value>self.value):
			if(self.right==None):
				print(value," not found")
			else:
				return self.right.findval(value)
		else:
			print(value," found")





a=Tree(5)
a.insert(4)
a.insert(8)
a.insert(9)
a.findval(7)

# a.printtree()

print(a.left.value)
print(a.right.value)
print(a.right.right.value)






