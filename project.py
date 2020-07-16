import random

class Linkedlist:

	def __init__(self):
		self.head=Listnode()

	def random(self):

		k=random.randint(1,6)
		return k

	def insert(self,k):

		temp=Listnode()
		temp.value=k
		temp.next=self.head.next
		self.head.next=temp

	def skiplist(self):

		self.search(1).skip=self.search(10)
		self.search(10).skip=self.search(20)
		self.search(20).skip=self.search(30)
		self.search(30).skip=self.search(40)
		self.search(40).skip=self.search(50)
		self.search(50).skip=self.search(60)
		self.search(60).skip=self.search(70)
		self.search(70).skip=self.search(80)
		self.search(80).skip=self.search(90)

	def search(self,v):

		temp=self.head.next
		t=temp
		while(temp.skip):
			if v>temp.skip.value:
				t=temp
				temp=temp.skip
			
			else:
				t=temp
				break
		while(t):
			if(t.value==v):
				return t
			else:
				t=t.next

	
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

class Listnode:
	
	def __init__(self):
		
		self.value=None
		self.next=None
		self.ladder=None
		self.snake=None
		self.skip=None
		self.name=None
		self.count1=None

def main():
	print()
	print()
	print()
	print("                                       Welcome to Snake and Ladder Game")
	print()
	print()
	print("                                        ------------------------------")
	print("                                       |                              |")
	print("                                       |                              |")
	print("                                       |            PLAY              |")
	print("                                       |                              |")
	print("                                       |                              |")
	print("                                       |------------------------------|")
	print("                                       |                              |")
	print("                                       |          INSTRUCTIONS        |")
	print("                                       |                              |")
	print("                                       |                              |")
	print("                                        ------------------------------")
	print()
	print("                                          Enter 1 to see instructions")
	print("        ")
	m1=int(input())
	print()
	if(m1==1):
		print("RULES of this game:                                                                                                      ")
		print()
		print("    1) This is a multiplayer game.The board in this game consists of snakes and ladders.As u find a ladder you will have to climb it ")
		#print()
		print("     if u find a snake you have to come down to its tail.")
		
		#print()
		#print()
		print("    2)There should be atleast two players coz this is a mutiplayer game")
		#print()
		#print()
		print("    3)If your choice is 6 then you  will be given one more choice")
		#print()
		print("    4)The player who reaches 100 first is the WINNER. ")
		#print()
		print("    5)The game will terminate untill (n-1) players win ")
		#print()
		print("    6) you are not supposed to insert a snake and ladder at the same point.")
		#print()
		print()
		print("Hope you enjoy this game !!!")                                                                                                                                                                                               
		print()
		print("You can start playing now ")
		print()
	L=Linkedlist()

	for i in range(105,0,-1):
		L.insert(i)
	print("how many ladders do u want to insert?")
	l=int(input())
	i=1

	print("Enter ladder inputs in the form a b  ,a<b")
	while(i<=l):
		ladd=input()
		z=ladd.split()
		a=int(z[0])
		b=int(z[1])

		if(a<b):
			i=i+1
			L.ladderinsert(a,b)
		else:
			print("Invalid input")

	print("How many snakes do you want to insert?")
	s=int(input())

	print("Enter Snake inputs in the form a b  ,a>b")
	i=1
	while(i<=s):
		snak=input()
		y=snak.split()
		a=int(y[0])
		b=int(y[1])

		if(a>b):
			i=i+1
			L.snakeinsert(a,b)
		else:
			print("Invalid input")
	print("                        ------------------------------------------------")
	print("                       ",end="|")
	for i in range(100,90,-1):
		if(i==100):
			print(i,end =" |")
		else:
			print(i,end ="  |")
	print()
	print("                        ------------------------------------------------")
	print("                       ",end="|")
	for i in range(81,91):
		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(80,70,-1):

		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(61,71,):

		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(60,50,-1):

		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(41,51):

		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(40,30,-1):

		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(21,31):

		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(20,10,-1):
		print(i,end ="  |")
	print()
	print("                        -------------------------------------------------")
	print("                       ",end="|")
	for i in range(1,11):
		if(i==10):
			print(i,end ="  |")
		else:
			print(i,end ="   |")
	print()
	print("                        -------------------------------------------------")
		
	print("Enter number of players:")
	players=int(input())
	P=[None for i in range(players)]
	for i in range(players):
		P[i]=Linkedlist()
		P[i].insert(0)
	a=1

	print("enter player names:")
	for i in range(players):
		P[i].head.name=input()

	L.skiplist()
	count=0

	while(a):

		i=0
		if(count==players-1):
				break
		while(i<players):

			if(P[i].position()==100):
				i=i+1
				continue
			
			j=0
			n=1
			while(j<n):

				print("The die value of player ",P[i].head.name,":",end="")
				d1=L.random()
				print(d1,end="")
				str=input()
				#d1=int(input())
				k=P[i].position()+d1
				k1=k
				b=0
				if(k1<=100):
					if(d1==6):
						print("since you entered 6 you have one more choice:	")
						j=j

					else:
						j=j+1

					if(L.hasladder(k1)):
					
						q=L.ladderend(k1)
						t=L.search(q)
						while(t.snake or t.ladder):
							if (t.snake):
								t=L.snakeend(q)
								t=L.search(t)
								q=t.value
							else:
								t=L.ladderend(q)
								t=L.search(t)
								q=t.value
							

						P[i].insert(q)
						print("current position of player",P[i].head.name,"--. ",P[i].position())
						print()
						print()

					if(L.hassnake(k1)):
					
						q=L.snakeend(k1)
						t=L.search(q)
						while(t.snake or t.ladder):
							if (t.snake):
								t=L.snakeend(q)
								t=L.search(t)
								q=t.value
							else:
								t=L.ladderend(q)
								t=L.search(t)
								q=t.value
						P[i].insert(q)
						print("current position of player",P[i].head.name,"--> ",P[i].position())
						print()
						print()

					if(L.hasladder(k) != True and L.hassnake(k1)  !=True ):
						if(d1!=6):
							if(k<=100):
								P[i].insert(k)
							print("current position of player",P[i].head.name,"--> ",P[i].position())
							print()
							print()

						else:
							if(k<=100):
								P[i].insert(k)
							print("current position of player",P[i].head.name,"-->",P[i].position())

							print()
							print()

					if(P[i].position()==100):
						#a=0
						count=count+1
						P[i].head.count1=count
						print("Yeyy!",P[i].head.name," Prize : ",count)
						print("                                   ")
						print("      *          * * * *     *     *      *               *     * * *     *       *             ")
						print("       *       *  *      *   *     *       *             *    *      *    * *     *             ")
						print("         *   *    *      *   *     *        *     *     *     *      *    *  *    *             ")
						print("           *      *      *   *     *         *   * *   *      *      *    *   *   *             ")
						print("           *      *      *   *     *          * *   * *       *      *    *    *  *             ")
						print("           *       * * *     * * * *           *     *          * * *     *     * *             ")
						print("                                                                                          ")
						j=n
						#i=players
				else:
					print("current position of player",P[i].head.name,"--> ",P[i].position())
					print()
					print()
					j=j+1		
			i=i+1
	for i in range(players):
		if(P[i].head.count1==None):		
			print("Well played! ",P[i].head.name," ,You Lost,Better luck next time ")

	print("=====================================================================================================================")
	print("")
	for k in range(players):
		if P[k].head.count1!=None:
			print("      ",P[k].head.name,"              :            ",P[k].position(),"   prize :  ",P[k].head.count1 )
		else:
			print("      ",P[k].head.name,"              :            ",P[k].position(),"   prize :  No prize")
	print("")	
	print("=====================================================================================================================")



if __name__ == '__main__':
	main()
	

