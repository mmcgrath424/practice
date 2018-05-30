import os

class ListNode(object):
	
	def __init__(self):
		self.next = None
		self.value = None
		self.prev = None

	def get_next(self):
		return self.next

	def get_prev(self):
		return self.prev

	def get_value(self):
		return self.value

	def set_next(self, new_next):
		self.next = new_next

	def set_prev(self, new_prev):
		self.prev = new_prev
	
	def set_value(self, new_value):
		self.value = new_value

class LinkedList(object):
	
	def __init__(self):
		self.tail = None
		self.head = None
		self.num_nodes = 0

# Add a new node at the tail of the list		
	def append(self,node_val):
		if self.num_nodes==0:
			self.tail = ListNode()
			self.head = self.tail
		else:
			temp_node = ListNode()
			self.tail.set_next(temp_node)
			temp_node.set_prev(self.tail)
			self.tail = temp_node
			self.tail.set_value(node_val)
		self.num_nodes += 1

# Add a new node before the head of the list		
	def prepend(self,node_val):
		if self.num_nodes==0:
			self.head = ListNode()
			self.tail = self.head
		else:
			temp_node = ListNode()
			self.head.set_prev(temp_node)
			temp_node.set_next(self.head)
			self.head = temp_node
			self.head.set_value(node_val)
		self.num_nodes += 1
		
# Insert a node at the given node number		
	def insert(self,node_num,node_val):
		if self.num_nodes == 0:
			print ("You can't insert into an empty list")
			return None
		new_node = ListNode()
		new_node.set_value(node_val)
		temp_node = self.get_node(node_num) # store node to adjust prev value
		temp_node2 = temp_node.get_prev() # store prev node to adjust next value
		new_node.set_prev(temp_node.get_prev())
		new_node.set_next(temp_node)
		temp_node.set_prev(new_node)
		temp_node2.set_next(new_node)
		if node_num == 0:
			self.head = new_node
		if node_num == self.num_nodes - 1:
			self.tail = new_node
		self.num_nodes += 1

# Remove the node number supplied		
	def remove(self,node_num):
		temp_node = self.get_node(node_num) # get node to remove
		temp_node2 = temp_node.prev # get previous node to adjust next value
		temp_node3 = temp_node.next # get next node to adjust prev value
		temp_node3.set_prev(temp_node.get_prev())
		temp_node2.set_next(temp_node.get_next())
		del temp_node
		self.num_nodes -= 1

# Return the pointer to the node number requested. 
	def get_node(self,node_num):
		if node_num >= self.num_nodes or node_num < 0:
			print ("out of range")
			return 0
		elif node_num == 0:
			return self.head.get_value()
		elif node_num == self.num_nodes-1:
			return self.tail.get_value()
		else :
			temp_node = self.head
			for x in range (0,node_num):
				temp_node = temp_node.get_next()
			return temp_node

# Print the values for all nodes in the list. 			
	def print_list(self):
		temp_node = self.head
		for x in range (0,self.num_nodes):
			print (temp_node.get_value())
			temp_node = temp_node.get_next()
			


if __name__=='__main__':
	test_list = LinkedList()
	for x in range (1,10):
		test_list.append(x)
	
	test_list.print_list()

	test_list.insert(5,22)
	test_list.print_list()
	test_list.remove(6)
	test_list.print_list()
	
