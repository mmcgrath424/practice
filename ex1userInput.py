import os
import datetime
import random

#tell a user what year they will turn 100
def ex1userInput():
	name = raw_input("What is your name: ")
	age = input("What is your age: ")
	repeatnum = input("How many times to repeat: ")
	year = datetime.datetime.now().year
	hundo = year + 100 - age

	print ("Hello "+name+" you will turn 100 in the year "+str(hundo)+"\n")*repeatnum

#check if a number is even or odd
def ex2evenOdd():
	num_in = input("Check for even or odd: ")
	checkOdd = num_in % 2
	
	if checkOdd:
		print ("The number is odd")
	else:
		print ("The number is even")
		
#find all values less than 5 in a list				
def ex3lists():
	a_list = [1,1,2,3,5,8,13,21,34,55,89]
	temp_list = []
	
	for x in a_list:
		if x < 5:
			temp_list.append(x)
	print (temp_list)
	
	
#print all numbers the divide evenly into a user entered number
def ex4div():
	in_num = int(raw_input("enter a number for divisor check: "))
	for x in range(1,in_num+1):
		if (in_num % x)==0:
			print (x)

#find the intersection of 2 lists			
def ex5overlap():
	a_list = [1,1,2,3,5,8,13,21,34,55,89]
	b_list = [1,1,3,4,5,6,7,8,9,10,11,12,13]				
	c_list = []
	temp_dict = {}
	dupe_check = 0
	pos = 0

	for x in a_list:
		while pos<len(b_list) and x>=b_list[pos]:
			if x == b_list[pos] and x!=b_list[pos-1]:
				c_list.append(x)
			pos += 1			 	
	print (c_list)


# linear time using a Dict (unfinished)	
# 	if len(a_list)>len(b_list):
# 		for x,pos in enumerate(a_list):
# 			temp_dict.update({x:pos})
# 		
# 	else :
# 		for pos,x in enumerate(b_list):
# 			temp_dict.update({x:pos})		
# 	print temp_dict

	
		
# Old exponential solution	
# 	for x in a_list:
# 		for y in b_list:
# 			if x == y:
# 				if len(c_list)>0:
# 					for z in c_list:
# 						if x==z:
# 							dupe_check = 1
# 					if dupe_check==0:
# 						c_list.append(x)
# 					else: 
# 						dupe_check = 0
# 				else :
# 					c_list.append(x)
#	print c_list

#check if the user entered a palindrome
def ex6palindrome():
	u_input = raw_input("Enter a string to check for a palindrome: ")
	is_pal = 1
	
	for x in range(0, len(u_input)):
		if u_input[x] != u_input[-1-x]:
			is_pal = 0
			
	if is_pal == 1:
		print (u_input + " is a palindrome")
	else :
		print (u_input + " is NOT a palindrome")
		
#list all the even numbers in a list		
def ex7listeven():
	a_list = [1,4,9,16,25,36,49,64,81,100]
	b_list = [ x for x in a_list if x % 2 == 0]
	
	print (b_list)

#rock paper scissors
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
			print ("Its a tie")
		elif game_result in [1,-2]:
			print ("Player 1 wins with "+p1_choice)
		else :
			print ("Player 2 wins with "+p2_choice)
		
#guessing game for a random number from 1-9
#Tell the user higher or lower and keep track of the guesses		
def ex9guess():
	guess_count = 0
	rand_num = random.randint(1,9)
	while True:
		play_quit = raw_input("Type play or quit : ")
		if play_quit == 'quit':
			break
		
		while True:
			guess_count += 1
			u_guess = input("Guess my number between 1 and 9 :")
			if 	rand_num == u_guess:
				print ("You guessed it. It took "+str(guess_count)+" guesses")
				break
			elif rand_num < u_guess:
				print ("The number is lower than your guess")
			else:
				print ("The number is higher than your guess")
		
#check if the user entered a prime number
def ex11prime():
	in_num = int(raw_input("enter a number for prime number check: "))
	is_prime = 1
	for x in range(2,in_num):
		if (in_num % x)==0:
			is_prime = 0
	if is_prime==1:
		print (str(in_num)+" is a prime number")
	else:
		print (str(in_num)+" is not a prime number")
		
#create a fibonacci sequence of a user entered length
def ex13fib():
	u_input = input("Enter the length of the fibonacci sequence: ")
	fib_seq = []
	for x in range(0,u_input):
		if x <= 1:
			fib_seq.append(1) 
		else:
			fib_seq.append(fib_seq[x-1]+fib_seq[x-2])
	print (fib_seq)
	
#returns the supplied list without dupes
def ex14nodupes(in_list):
	temp_list = []
	temp_list.append(in_list[0])
	no_dupe = 1
	for x in in_list:
		for y in temp_list:
			if x==y:
				no_dupe = 0
				break
		if no_dupe:
			temp_list.append(x)
		else:
			no_dupe = 1
	
	print (temp_list)



#ex14nodupes([1,2,3,4,5,1,2,6,3,7,8,4,5,9])
#ex13fib()	
#ex11prime()
#ex9guess()
#ex8rps()
#ex7listeven()
#ex6palindrome()
ex5overlap()	
#ex4div()	
#ex3lists()	
#ex2evenOdd()



















