##############################################################################################

# Next I will write an inplace heap sort algorithm as described in MIT ocw
def find_priority_child(id_left, id_right, list, length):
	if id_right<length:
		if list[id_left]<list[id_right]:
			return id_left
		else:
			return id_right
	else:
		return id_left

def swap(id1, id2, list):
	temp = list[id1]
	list[id1] = list[id2]
	list[id2]=temp

def heapify_down(i, list, length):
	left_child_id = i*2+1
	right_child_id = i*2+2
	if left_child_id >=length:
		return
	else:
		priority_id = find_priority_child(left_child_id, right_child_id, list, length)
		if list[i]>=list[priority_id]:
			swap(priority_id, i, list)
			heapify_down(priority_id, list, length)

def in_place_heap_sort(list):
	length = len(list)
	list[:] = [-1*x for x in list]
	for i in range((length-1)/2, -1,-1):
		heapify_down(i, list, length)
	while length>0:
		swap(0, length-1, list)
		length-=1
		heapify_down(0, list, length)
	return [-1*x for x in list]


def main():
	random_arr = random.sample(range(-10,30), 20)
	print random_arr
	p = sorted(random_arr)
	q = in_place_heap_sort(random_arr)
	print p
	print q
	print p==q


if __name__ =="__main__":
	main()