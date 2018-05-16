import os

data_set = [108,7,50,22,37,108,88,53,34,44,92,107,67,-3,-7,97]
#data_set = [108,7,50,22,37]
n = 5
n_largest_offsets = []
largest = 0
second_largest = 0
counter = 0


for x in range (0,len(data_set)):
	if data_set[x]>=data_set[largest]:
		largest = x
	if data_set[largest] is data_set[second_largest]:
		second_largest = x
	if (data_set[x] > data_set[second_largest] and
	data_set[x] < data_set[largest] and   data_set[second_largest] < data_set[largest]):
		second_largest = x
		
for i in range (0,n):
	n_largest_offsets.append(i)

for y in range (0,len(data_set)):
	counter = 0
	while counter < n :
		if data_set[y] != data_set[n_largest_offsets[counter]]:
			if (data_set[y] > data_set[n_largest_offsets[counter]] and 
			data_set[y] != data_set[n_largest_offsets[counter-1]]):
				n_largest_offsets.insert(counter,y)
				n_largest_offsets.pop()
				counter = n # exit loop once a value is inserted
		else :
			counter = n  # exit loop if a dupe is found
		counter = counter + 1

		print n_largest_offsets  	

print "Largest: " + str(data_set[largest]) + " Offset: " + str(largest)
print ("Second largest: " + str(data_set[second_largest]) + " Offset: " + 
str(second_largest))
