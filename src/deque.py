"""An implementation of a Deque using Python."""

from dll import DbLinkedList

class Deque(object):
	"""Implementation of a deque data structure.

	append(value) adds value to the end of the deque.
	appendleft(value) adds value to the front of the deque.
	pop() removes value from the end of the deque.
	popleft() removes a value from the front of the deque.
	peek() returns the 
	"""

	def __init__(self, iterable=None):
		"""Initializes a deque."""
		self._dblinkedlist = DbLinkedList()
		# if iterable and hasattr(iterable, "__iter__"):
  #           for item in iterable:
  #               self.append(item)
  #       elif iterable:
  #           raise TypeError

	def append(self, value):
		""""""
		self._dblinkedlist.append(value)

	def appendleft(self, value):
		""""""
		self._dblinkedlist.push(value)

	def pop(self):
		""""""
		popped_value = self.shift()
		return popped_value

	# def popleft(self):
	# 	""""""
	# 	popped_value = self.pop()
		# return popped_value

	# def peek(self):
	# 	""""""
	# 	if self._dblinkedlist.head is None:
	# 		return self._dblinkedlist
	# 	return self._dblinkedlist.tail.value

	# def peekleft(self):
	# 	""""""
	# 	return self._dblinkedlist.head.value

	# size(self):
	# 	""""""
		
