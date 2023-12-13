from Pieces import Pieces
p1po=Pieces.p1pos
p2po=Pieces.p2pos
row=['A','B','C','D','E','F','G','H']
columns=[1,2,3,4,5,6,7,8]
kingP1=[]
kingP2=[]
class Board():	
	
	def __init__(self,row,column):
		self.row=row
		self.column=column
	def display(self):
		print('','','','',end='')
		for i in columns:
			print(i,end='')
		print('')
		print('-----------')
		for j in row:
			print(j,'-',end='')
			for k in columns:
				c=0
				p1=' 🟫 '
				p2=' 🟫 '
				check=j+'-'+str(k)
				if check in Pieces.p1pos:
					p1=' 🆖 '
					p2=' 🆖 '
				elif check in Pieces.p2pos:
					p1=' 🆗 '
					p2=' 🆗 '
				if k%2==1:
					print(p1,end='')
				elif k%2==0:
					print(p2,end='')
			print('')

	def inputcheckp1(self,st,str1):
		a=str1.split('-')
		b=st.split('-')
		
		if a[0] and b[0] in row:
			p=row.index(a[0])
			q=row.index(b[0])
			print(p)
			print(q)
			print(kingP1)
			if str1 in kingP1:
				print('Yes')
				if int(q)==int(p)+1 or int(q)==int(p)-1:
					if int(a[1])==int(b[1])+1 and int(b[1])<8:
						return 1
					elif int(b[1])==int(a[1])+1 and int(a[1])<8:
						return 1
					else:
						print('Wrong move!! You cannot move beyond game rules!!')
						return 0
				else:
					print('Wrong move!! You can only move one square DIAGONALLY')
					return 0

			
			else:	
				if int(q)==int(p)+1:
					if int(a[1])==int(b[1])+1 and int(b[1])>0 and int(b[1])<8:
						return 1
					elif int(b[1])==int(a[1])+1 and int(a[1])>0 and int(a[1])<8:
						return 1
					else:
						print('Wrong move!! You cannot move beyond game rules!!')
						return 0
				else:
					print('Wrong move!! You can only move one square DIAGONALLY')
					return 0
		else:
			print('Wrong move!! You can only move through one square ahead diagonally and along the squares on board!!')
			return 0


	def inputcheckp2(self,st,str1):
		a=str1.split('-')
		b=st.split('-')
		if a[0] and b[0] in row:
			p=row.index(a[0])
			q=row.index(b[0])
			if str1 in kingP2:
				print('Yes')
				if int(q)==int(p)+1 or int(q)==int(p)-1:
					if int(a[1])==int(b[1])+1 and int(b[1])<8:
						return 1
					elif int(b[1])==int(a[1])+1 and int(a[1])<8:
						return 1
					else:
						print('Wrong move!! You cannot move beyond game rules!!')
						return 0
				else:
					print('Wrong move!! You can only move one square DIAGONALLY')
					return 0

			else:
				if int(q)==int(p)-1:
					if int(a[1])==int(b[1])+1 and int(b[1])<8:
						return 1
					elif  int(b[1])==int(a[1])+1 and int(a[1])<8:
						return 1
					else:
						print('Wrong move!! You cannot move beyond game rules!!')
						return 0
				else:
					print('Wrong move!! You can only move one square DIAGONALLY ')
					return 0
		else:
			print('Wrong move!! You can only move through one square ahead diagonally and along the squares on board!!')
			return 0


	
	def nonKingp1(self,str1,str2):
		c=str1.split('-')
		d=str2.split('-')
		a=row.index(c[0])
		b=row.index(d[0])
		if str1 in p1po:
			print('Your pick is on the way!! you Cannot go past your pick !! Play fair')
		elif str1 in p2po:
			if c[1]>d[1] and int(c[1])>1 and int(c[1])<8:
				j=row[a+1]+'-'+str(int(c[1])+1)
				if str2 in kingP1:
					if a<b:
						j=row[a-1]+'-'+str(int(c[1])+1)
					else:
						j=row[a+1]+'-'+str(int(c[1])+1)
				if j not in p1po and p2po:
					p2po.remove(str1)
					p1po[p1po.index(str2)]=j
					m=j.split('-')
					if str2 in kingP1:
						kingP1.remove(str2)
						kingP1.append(j)
					elif m[0]=='H':
						print('hahahaha')
						kingP1.append(j)
					return 1
				else:
					print('Wrong move!! You cannot move there!!')
					return 0
			elif c[1]<d[1] and int(d[1])>1 and int(d[1])<9:
				j=row[a+1]+'-'+str(int(c[1])-1)
				if str2 in kingP1:
					if a<b:
						j=row[a-1]+'-'+str(int(c[1])-1)
					else:
						j=row[a+1]+'-'+str(int(c[1])-1)
				if j not in p1po and p2po:
					p2po.remove(str1)
					p1po[p1po.index(str2)]=j
					m=j.split('-')
					if str2 in kingP1:
						kingP1.remove(str2)
						kingP1.append(j)
					elif m[0]=='H':
						print('hhahahaha')
						kingP1.append(j)
					return 1
				else:
					print('Wrong move!! Piece cannot move there!!')
					return 0

		else:
			if d in kingP1:
				if int(a)==int(b)+1 or int(a)==int(b)-1 and int(c[1])==int(d[1])+1 or int(c[1])==int(d[1])-1:
					p1po[p1po.index(str2)]=str1
					kingP1[kingP1.index(str2)]=str1
					print('Valid move!!!')
					return 1

			else:
				if int(a)==int(b)+1 and int(c[1])==int(d[1])+1 or int(c[1])==int(d[1])-1:
					p1po[p1po.index(str2)]=str1
					print('Valid move!!!')
					return 1
				else:
					print('Wrong move!! Piece can only move diagonally!!')
					return 0			
			

	def nonKingp2(self,str1,str2):
		c=str1.split('-')
		d=str2.split('-')
		a=row.index(c[0])
		b=row.index(d[0])
		if str1 in p2po:
			print('Your pick is on the way!! you Cannot go past your pick !! Play fair')
		elif str1 in p1po:
			if c[1]>d[1] and int(c[1])>1 and int(c[1])<8:
				j=row[a-1]+'-'+str(int(c[1])+1)
				if str2 in kingP2:
					if a<b:
						j=row[a-1]+'-'+str(int(c[1])+1)
					else:
						j=row[a+1]+'-'+str(int(c[1])+1)
				if j not in p1po and p2po:
					p1po.remove(str1)
					p2po[p2po.index(str2)]=j
					m=j.split('-')
					if str2 in kingP2:
						kingP2.remove(str2)
						kingP2.append(j)
					elif m[0]=='A':
						kingP2.append(j)
					return 1
				else:
					print('Piece cannot move there!!')
					return 0
			elif c[1]<d[1] and int(d[1])>1 and int(d[1])<9:
				j=row[a-1]+'-'+str(int(c[1])-1)
				if str2 in kingP2:
					if a<b:
						j=row[a-1]+'-'+str(int(c[1])-1)
					else:
						j=row[a+1]+'-'+str(int(c[1])-1)
				if j not in p1po and p2po:
					p1po.remove(str1)
					p2po[p2po.index(str2)]=j
					m=j.split('-')
					if str2 in kingP2:
						kingP2.remove(str2)
						kingP2.append(j)
					elif m[0]=='A':
						kingP2.append(j)
					return 1
				else:
					print('Piece cannot move there!!')
					return 0

		else:
			if d in kingP2:
				if int(a)==int(b)-1 or int(a)==int(b)+1 and int(c[1])==int(d[1])+1 or int(c[1])==int(d[1])-1:
					p2po[p2po.index(str2)]=str1
					kingP2[kingP2.index(str2)]=str1
					print('Valid move!!!')
					return 1
			else:
				if int(a)==int(b)-1 and int(c[1])==int(d[1])+1 or int(c[1])==int(d[1])-1:
					p2po[p2po.index(str2)]=str1
					print('Valid move!!!')
					return 1
				else:
					print('Piece can only move diagonally!!')
					return 0
		
		


while(True):
	Bo=Board(row,columns)
	Bo.display()
	
	while(True):
		print('Player1 Turn!!')
		i=input('Please Enter the position of pick you wanna move:')
		if i in Pieces.p1pos:
			while(True):
				c=input(f'Please Enter where to move the pick from {i} to:')
				if(Bo.inputcheckp1(c,i)):
					if(Bo.nonKingp1(c,i)):
						break
					else:
						pass
				else:
					pass
		elif i not in Pieces.p1pos:
			print('No piece in that position!!Please Try again!!')
			continue
		Bo.display()
		break	
	


	
	
	
	while(True):
		print('Player2 Turn!!')
		i=input('Please Enter the position of piece you want move:')
		if i in Pieces.p2pos:
			while(True):
				c=input(f'Please Enter where to move the piece from {i} to:')
				if(Bo.inputcheckp2(c,i)):
					if(Bo.nonKingp2(c,i)):
						break
					else:
						pass
				else:
					break
		elif i not in Pieces.p2pos:
			print('Player you dont have piece in that position !!Please Try again!!')
			continue

		Bo.display()
		break
	print(p1po)
	print(p2po)
