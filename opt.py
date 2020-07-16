class Linkedlist:
	def __init__(self):
		self.head=Listnode()

	def insert(self,k):
		temp=Listnode()
		temp.value=k
		temp.next=self.head.next
		self.head.next=temp
	
	def search(self,v):
		temp=self.head
		while(temp.next != None):
			if(temp.next.value ==v):
				return temp.next
			else:
				temp=temp.next
	
	def ladderinsert(self,a,b):
		x=self.search(a)
		y=self.search(b)
		x.ladder=y

	def hasladder(self,a):
		x=self.search(a)
		if(x.ladder != None):
			return True
		else:
			return False

	def ladderend(self,a):
		if(self.hasladder(a)):
			x=self.search(a)
			return x.ladder.value


	def snakeinsert(self,a,b):
		x=self.search(a)
		y=self.search(b)
		x.snake=y

	def hassnake(self,a):
		x=self.search(a)
		if(x.snake != None):
			return True
		else:
			return False

	def snakeend(self,a):
		if(self.hassnake(a)):
			x=self.search(a)
			return x.snake.value
	

	def position(self):
		return self.head.next.value
class Adjlist:
	def __init__(self,v):
			
		self.vertices=v
		self.head=[Listnode() for i in range(v)]
		for i in range(v):
			self.head[i].value=i

	def formlist(self,a,b):
		temp=Listnode()
		temp.value=b
		temp.next=self.head[a].next
		self.head[a].next=temp
	def printlst(self):
		for k in range(self.vertices):
			print("vertex",k,end=" : ")
			t=self.head[k]
			while(t.next):
				print(t.next.value,end=" ")
				t=t.next
			print()
	def BFS(self,s,b):
		Q=Queue()
		
		t=self.head[s]
		t.color="yellow"
		t.dist=0
		Q.enqueue(t.value)
		arry=[]
		print("Minimum number of dies from source vertex from source vertex is : ")
		#print("vertex ",t.value," : ",t.dist)
		while (not Q.isEmpty()):
			u=Q.dequeue()
			t=self.head[u].next
			
			while(t):
				i=t.value
				if(self.head[i].color=="white"):
					self.head[i].color="yellow"
					self.head[i].dist=self.head[u].dist+1
					if(i==b):
						print("vertex ",i," : ",self.head[i].dist)
					Q.enqueue(i)
					self.head[i].pred=self.head[u]
					if(i==b):
						arry.append(b)

						#print(b,end="<--")
						k=1
						while(k):
							#print(self.head[i].pred.value,end="<--")
							arry.append(self.head[i].pred.value)
							if(self.head[i].pred.value==s):
								k=0
							i=self.head[i].pred.value
						
				t=t.next
			self.head[u].color="black"
		print()	
		#print(arry)
		for i in range(int(len(arry)/2)):
			temp=arry[i]
			arry[i]=arry[len(arry)-i-1]
			arry[int(len(arry))-i-1]=temp
		print(arry)
		n=int(len(arry))
		count=0
		#print(a[0],end="==>")
		for i in range(n-1):

			if(arry[i+1]==arry[i]+1):
				count=count+1
				if(count>=6):
					print(6,end=",")
					count=count-6

			else:
				if(count != 0):
					print(count,end=",")
					count=0
		if(count != 0):			
			print(count)
		print("")
		

class Queue:
	def __init__(self):
		self.L=[]
		self.front=0
		self.tail=0
	def enqueue(self,k):
		self.tail=self.tail+1
		self.L.append(k)
	def dequeue(self):
		self.front=self.front+1
		return self.L[self.front-1]
	def isEmpty(self):
		if(self.front==self.tail):
			return True
		else:
			return False

		

class Listnode:
	
	def __init__(self):
		self.value=None
		self.next=None
		self.ladder=None
		self.snake=None
		self.skip=None
		self.color="white"

def main():
	L=Linkedlist()
	v=106
	A=Adjlist(v)

	for i in range(106,0,-1):
		L.insert(i)
	for i in range(100):
		for j in range(1,7):
			A.formlist(i,i+j)
	print("how many ladders do u want to insert?")
	l=int(input())
	i=1

	while(i<=l):
		ladd=input()
		z=ladd.split()
		a=int(z[0])
		b=int(z[1])
		if(a<b):
			A.head[a].next=None
			i=i+1
			k=a
			a=a-6
			#L.ladderinsert(a,b)
			o=1
			while(o<=6):
				if a>=0:
					z=k-a
					t=A.head[a]
					while(z!=0):
						t=t.next
						z=z-1
					t.value=b
					a=a+1
					o=o+1
				else:
					t1=a
					a= -1*a
					o=o+a
					a=0

			#A.formlist(a,b)
		else:
			print("Invalid input")
	A.printlst()
	print("How many snakes do you want to insert?")
	l=int(input())
	i=1

	while(i<=l):
		ladd=input()
		z=ladd.split()
		a=int(z[0])
		b=int(z[1])
		if(a>b):
			A.head[a].next=None
			i=i+1
			k=a
			a=a-6
			#L.ladderinsert(a,b)
			o=1
			while(o<=6):
				if a>=0:
					z=k-a
					t=A.head[a]
					while(z!=0):
						t=t.next
						z=z-1
					t.value=b
					a=a+1
					o=o+1
				else:
					t1=a
					a= -1*a
					o=o+a
					a=0

			#A.formlist(a,b)
		else:
			print("Invalid input")

	print("enter your source vertex and destination to find optimal path between them:")
	str1=input()
	z=str1.split()
	a=int(z[0])
	b=int(z[1])
	A.BFS(a,b)

	



		
	
		



if __name__ == '__main__':
	main()
	

