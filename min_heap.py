# Implementation of the heap data structure
import random
class MinHeap:

	def __init__(self):
		self.container_ = [0]
		self.root = 1

	def __init__(self, Array):
		self.container_ = Array
		self.container_.insert(0,0)
		self.root = 1
		self.build_heap()

	def heapify_down(self, i):
		left_child_id = i*2
		right_child_id = i*2+1
		if left_child_id >=len(self.container_):
			return
		else:
			priority_id = self.find_priority_child(left_child_id, right_child_id)
			if self.container_[i]>=self.container_[priority_id]:
				self.swap(priority_id, i)
				self.heapify_down(priority_id)
	

	def heapify_up(self, i):
		if i ==self.root:
			return
		else:
			parent_id = i/2
			if self.container_[parent_id]>=self.container_[i]:
				self.swap(parent_id, i)
				self.heapify_up(parent_id)
			
	
	def build_heap(self):
			for i in range(len(self.container_)/2, 0, -1):
				self.heapify_down(i)

			

	def find_priority_child(self, id_left, id_right):
		if id_right<len(self.container_):
			if self.container_[id_left]<self.container_[id_right]:
				return id_left
			else:
				return id_right
		else:
			return id_left
	
	def swap(self, id1, id2):
		temp = self.container_[id1]
		self.container_[id1] = self.container_[id2]
		self.container_[id2]=temp

	def peek(self):
		return self.container_[self.root]

	def remove_min(self):
		if not(len(self.container_)==1):
			self.swap(self.root, len(self.container_)-1)
			self.container_.pop()
			self.heapify_down(self.root)
		
	
	def insert(self, x):
		self.container_.append(x)
		self.heapify_up(len(self.container_)-1)

	def print_heap(self):
		print self.container_[self.root:len(self.container_)]
	


# The bad way.
def heap_sort(list):
	# list[:]=map(lambda x: (-1)*x, list)
	heap = MinHeap(list)
	sorted_list=[]
	while len(heap.container_)!=1:
		sorted_list.append(heap.peek())
		heap.remove_min()
	return sorted_list


def main():
	# A = MinHeap([5,8,13,12,25,2])
	# A.print_heap()
	# A.insert(2)
	# A.print_heap()
	# A.insert(4)
	# A.print_heap()
	# A.insert(10)
	# A.print_heap()
	# A.insert(0)
	# A.print_heap()
	# A.insert(30)
	# A.print_heap()
	# A.insert(45)
	# A.print_heap()
	# A.remove_min()
	# A.remove_min()
	# A.remove_min()
	# A.remove_min()
	# A.print_heap()
	# A = MinHeap([-4,-8,-3,-2,-1,-20,-15,0])
	# A.print_heap()
	# print heap_sort([4,8,3,2,1,20,15,0])
	random_arr = random.sample(range(-10,30), 20)
	print random_arr
	p = sorted(random_arr)
	q = heap_sort(random_arr)
	print p
	print q
	print p==q


if __name__ =="__main__":
	main()
