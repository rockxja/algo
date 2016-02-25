# implementing the queue ADT
# I will implement it using an underlying Array data structure

class Queue:

	def __init__(self):
		self.instack = []
		self.outstack = []
	def isEmpty(self):
		return len(self.instack)+len(self.outstack)==0
	def dequeue(self):
		if(self.isEmpty()):
			return None
		if len(self.outstack)!=0:
			return self.outstack.pop()
		else:
			while len(self.instack)>0:
				self.outstack.append(self.instack.pop())
			return self.outstack.pop()
	def enqueue(self, item):
		self.instack.append(item)

def main():
	q = Queue()
	q.enqueue(0)
	q.enqueue(5)
	q.enqueue(25)
	q.enqueue(4)
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()
	q.enqueue(22)
	q.enqueue(25)
	q.enqueue(-32)
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()



if __name__ == "__main__":
 	main()