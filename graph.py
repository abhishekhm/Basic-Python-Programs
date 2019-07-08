class graph:
	def __init__(self,gdict=None):
		if gdict==None:
			gdict=[]
		self.gdict=gdict

	def getvertices(self):
		return list(self.gdict.keys())

	def edges(self):
		edgenames=[]
		for vertex in self.gdict:
			for nextvertex in self.gdict[vertex]:
				if {nextvertex,vertex} not in edgenames:
					edgenames.append({vertex,nextvertex})
		return edgenames

	def addvertex(self,vertex):
		if vertex not in self.gdict:
			self.gdict[vertex]=[]

	def addedges(self,edge):
		edge=set(edge)
		(vertex1, vertex2)=tuple(edge)
		if vertex1 in self.gdict:
			self.gdict[vertex1].append(vertex2)
		else:
			self.gdict[vertex1]=[vertex2]


graphelements={'a':['b','c'], 'b':['a','d'], 'c':['a','d'], 'd':['c','b','e'], 'e':['d']}
	
a=graph(graphelements)
a.addvertex('f')
a.addedges({'f','e'})
a.addedges({'g','h'})
print(a.getvertices())
print(a.edges())



