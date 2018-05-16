import os
import datetime

def ex1userInput():
	name = raw_input("What is your name: ")
	age = input("What is your age: ")
	repeat = input("How many times to repeat: ")
	year = datetime.datetime.now().year
	hundo = year + 100 - age

	print repeat*("Hello "+name+" you will turn 100 in the year "+str(hundo)+"\n")


def ex2evenOdd():
	num_in = input("Check for even or odd: ")
	checkOdd = num_in % 2
	
	if checkOdd:
		print "The number is odd"
	else:
		print "The number is even"
		
				
def ex3lists():
	a_list = [1,1,2,3,5,8,13,21,34,55,89]
	temp_list = []
	
	for x in a_list:
		if x < 5:
			temp_list.append(x)
	print temp_list
	
	
def ex4div():
	in_num = int(raw_input("enter a number for divisor check: "))
	for x in range(1,in_num+1):
		if (in_num % x)==0:
			print x
			
def ex5overlap():
	a_list = [1,1,2,3,5,8,13,21,34,55,89]
	b_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]				
	c_list = []
	dupe_check = 0
	
	for x in a_list:
		for y in b_list:
			if x == y:
				if len(c_list)>0:
					for z in c_list:
						if x==z:
							dupe_check = 1
					if dupe_check==0:
						c_list.append(x)
					else: 
						dupe_check = 0
				else :
					c_list.append(x)
	print c_list


def ex6palindrome():
	u_input = raw_input("Enter a string to check for a palindrome: ")
	is_pal = 1
	
	for x in range(0, len(u_input)):
		if u_input[x] != u_input[-1-x]:
			is_pal = 0
			
	if is_pal == 1:
		print u_input + " is a palindrome"
	else :
		print u_input + " is NOT a palindrome"
		
		
def ex7listeven():
	a_list = [1,4,9,16,25,36,49,64,81,100]
	b_list = [ x for x in a_list if x % 2 == 0]
	
	print b_list

def ex8rps():
	rules = {'r':1, 'p':2, 's':3}
	
	while True:
		play_quit = raw_input("Type p to play and q to quit: ")
		if play_quit == 'q':
			break
		p1_choice = raw_input("Player 1 Choose one to play\nr = rock\np = paper\ns = scissors: ")
		p2_choice = raw_input("Player 2 Choose one to play\nr = rock\np = paper\ns = scissors: ")

		game_result = rules[p1_choice] - rules[p2_choice]
		
		if game_result == 0:
			print "Its a tie"
		elif game_result in [1,-2]:
			print "Player 1 wins with "+p1_choice
		else :
			print "Player 2 wins with "+p2_choice
		
		
		

ex8rps()
#ex7listeven()
#ex6palindrome()
#ex5overlap()	
#ex4div()	
#ex3lists()	
#ex2evenOdd()



















