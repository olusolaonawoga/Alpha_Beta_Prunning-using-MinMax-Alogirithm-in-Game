p1List=[]
p2List=[]
ch=['A','B','C','D','E','F','G','H']
class Pieces:
	p1pos=['A-2','A-4','A-6','A-8','B-1','B-3','B-5','B-7','C-2','C-4','C-6','C-8']
	p2pos=['F-1','F-3','F-5','F-7','G-2','G-4','G-6','G-8','H-1','H-3','H-5','H-7']
	state='NORMAL'
	def __init__(self,p1pos,p2pos):
		self.p1pos=p1pos
		self.p2pos=p2pos
	def display1(self):
		for i in self.p1pos:
			self.p1List.append(i.split('-'))
		print(self.p1List)
	def display2(self):
		for i in self.p2pos:
			self.p2List.append(i.split('-'))
		print(self.p2List)
	





	

