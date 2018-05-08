import os

data_set = [108,7,50,22,37,108,88,53,34,44,92,107,67,-3,-7,97]
n = 10
n_largest_offsets = [0]
largest = 0
second_largest = 0


for x in range (0,len(data_set)):
	if data_set[x]>=data_set[largest]:
		second_largest = largest
		largest = x
	elif data_set[x] > data_set[second_largest] or second_largest is 0:
		second_largest = x
		
for y in range (0,len(data_set)):
	for z in range (0,len(n_largest_offsets)):
		if data_set[y] > data_set[n_largest_offsets[z]]:
			n_largest_offsets.insert(z,y)
	print data_set[y]
	print data_set[n_largest_offsets[z]]
	print n_largest_offsets  	


print "Largest: " + str(data_set[largest]) + " Offset: " + str(largest)
print "Second largest: " + str(data_set[second_largest]) + " Offset: " + str(second_largest)
