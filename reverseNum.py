import os

def reverseNum(i_num):
	o_num = 0
	neg_check = 1
	
	if i_num < 0:
		neg_check = -1
	
	i_num = i_num * neg_check	
	
	while i_num > 0:
		o_num = o_num * 10
		o_num = o_num + (i_num % 10)
		i_num = i_num / 10
		
	o_num = o_num * neg_check
	return o_num

print reverseNum(-178564)

print 2**31




