"""
Pyhton implementation of linked list
"""

class ListNode(object):
	"""
	Node object containing reference to a value and 
	reference to next Node object.

	_____
	| 2 |
	-----
      ^
	__|___________
	| val | next |--->
	--------------  
	"""
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
	"""
	Class representing singly linked list.

			_____             _____
			| 2 |			  | 3 |
			-----			  -----
		      ^                 ^
			__|___________    __|___________
		    | val | next |--->| val | next |--->None
			--------------    --------------
	          ^                  ^
	          |	                 |
	          head               tail

	"""
	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def prepend(self, x):
		"""
		Insert node at the beginning of list
		"""
		node = ListNode(x)
		if self._head is None:
			self._head = node
			self._tail = self._head
		else:
			node.next = self._head
			self._head = node
		self._size += 1

	def append(self, x):
		"""
		Insert node at the end of list
		"""
		node = ListNode(x)
		if self._tail is None:
			self._tail = node
		else:
			self._tail.next = node
			self._tail = node
		self._size += 1

	def traverse(self):
		"""
		traverse linked list
		"""
		temp_ptr = self._head
		eles = list()
		while temp_ptr is not None:
			eles.append(temp_ptr.val)
			temp_ptr = temp_ptr.next
		return eles

	def delete_first(self):
		"""
		delete first element from the list
		"""
		if self._head is None:
			return False
		ptr = self._head
		self._head = self._head.next
		ptr.next = None
		self._size -= 1
		return True

	def __str__(self):
		"""
		String representation
		"""
		return '-->'.join(["[%s]" % str(i) for i in self.traverse()])

	def delete(self, x):
		"""
		delete the first node, whose value matches argument
		"""
		if self._head is None:
			return False
		if self._head.val == x:
			return self.delete_first()
		temp_ptr = self._head
		while temp_ptr.next is not None:
			if temp_ptr.next.val == x:
				temp_ptr.next = temp_ptr.next.next
			temp_ptr = temp_ptr.next
			if temp_ptr is None:
				break
		self._size -=1
		return True
