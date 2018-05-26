import os

class ListNode(object):
	
	def __init__(self):
		self.next = None
		self.value = None
		self.prev = None

class LinkedList(object):
	
	def __init__(self):
		self.head = ListNode()
		self.tail = self.head
		self.head.value = 1
		self.num_nodes = 1
		
	def append(self,node_val):
		temp_node = ListNode()
		self.head.next = temp_node
		temp_node.prev = self.head
		self.head = temp_node
		self.head.value = node_val
		self.num_nodes += 1
		
	def prepend(self,node_val):
		temp_node = ListNode()
		self.tail.prev = temp_node
		temp_node.next = self.tail
		self.tail = temp_node
		self.tail.value = node_val
		self.num_nodes += 1
		
	def insert(self,node_num,node_val):
		new_node = ListNode()
		new_node.value = node_val
		new_node.prev = self.get_node(node_num-1)
		new_node.next = self.get_node(node_num)
		self.get_node(node_num).prev = new_node
		self.get_node(node_num-1).next = new_node
		if node_num == 0:
			self.tail = new_node
		if node_num == self.num_nodes - 1:
			self.head = new_node
		self.num_nodes += 1
		
	def remove(self,node_num):
		temp_node = self.get_node(node_num)
		self.get_node(node_num+1).prev = temp_node.prev
		self.get_node(node_num-1).next = temp_node.next
		del temp_node
		self.num_nodes -= 1
	
	def get_node(self,node_num):
		if node_num >= self.num_nodes or node_num < 0:
			print ("out of range")
			return 0
		elif node_num == 0:
			return tail.value
		elif node_num == self.num_nodes-1:
			return head.value
		else :
			temp_node = self.tail
			for x in range (0,node_num):
				temp_node = temp_node.next
			return temp_node
			
	
			


test_list = LinkedList()
for x in range (2,10):
	test_list.append(x)

test_list.insert(5,22)
test_list.remove(6)
print (test_list.get_node(5).value)
print (test_list.get_node(6).value)
	
