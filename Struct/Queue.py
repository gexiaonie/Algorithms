# -*- coding:utf-8 -*-

class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.items = []

	def enqueue(self,item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

if __name__ == '__main__':
	items = [1,2,3,4,5]
	print items
	queue = Queue()
	for item in items:
		queue.enqueue(item)
	print 'size : ' + str(queue.size())
	for i in range(0,5):
		print queue.dequeue()
	print 'size : ' + str(queue.size())	
		