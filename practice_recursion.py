#Find if string a palindrome
# return True if it's a palindrome and False otherwise

def isPalindrome(string, begin_id, end_id):
	if begin_id>=end_id:#
		return True
	elif string[begin_id]==string[end_id]:
		return isPalindrome(string, begin_id+1, end_id-1)
	else:
		return False

#print isPalindrome('abba', 0, 3)


#having fun with recursion factorial
def Factorial(number):
	if number == 0 or number ==1: #base cases
 		return 1
 	else:
 		return Factorial(number-1)*number #recursion call
#next I will write a binary search
def BinarySearch(array, numb, min_index, max_index):
	k = (min_index+max_index)/2
	if min_index>max_index:
		return -1
	else:
		if numb == array[k]:
			return k
		elif numb< array[k]:
			return BinarySearch(array, numb, min_index, k-1)
		else:
			return BinarySearch(array, numb, k+1, max_index)

# A=[1,2,3,4,5,6,7,21,33,45,99,100,120,1000]
# print BinarySearch(A, 101, 0, len(A)-1)

def FindPeakOneD(array, min_index, max_index):
	k=(min_index+max_index)/2
	if k==min_index and array[k]>array[k+1]:
		return array[k]
	if k==max_index and array[k]>array[k-1]:
		return array[k]
	elif array[k]>array[k-1] and array[k]>array[k+1]:
		return array[k]
	elif array[k]<array[k+1]:
		return FindPeak(array, k+1, max_index)
	elif array[k]<array[k-1]:
		return FindPeak(array, min_index, k-1)
# B = [1,4,5,6,20,17,16]
# print FindPeak(B,0, len(B)-1)


def countSplitMerge(array,p,q,r):
	left_array = array[p:q+1]
	right_array = array[q+1:r+1]
	i=0; j=0; k=p
	inv_count=0
	while i<=q-p and j<=r-q-1:
		if left_array[i]<=right_array[j]:
			array[k] = left_array[i]
			i += 1 
		else:
			array[k] = right_array[j]
			j += 1
			inv_count += q-p-i+1
		k += 1
	while i<=q-p:
		array[k] = left_array[i]
		i += 1
		k += 1
	while j<=r-q-1:
		array[k] = right_array[j]
		j += 1
		k += 1
	return inv_count



def FindInversionSort(array,p,r):
	#First establish a base case when an array has one member
	if r<=p:
		return 0
	else:
		k = (r+p)/2
		left_inv = FindInversionSort(array,p,k)
		right_inv = FindInversionSort(array,k+1,r)
		split_inv = countSplitMerge(array,p,k,r)
		return left_inv+right_inv+split_inv

def pow(a, b):
	#base case
	if b==0:
		return 1
	elif b%2==0:
		return pow(a, b/2)*pow(a, b/2)
	else:
		return pow(a, b/2)*pow(a, b/2)*a

#print pow(3,2)

# Infinitely long stream of integers [1,2,3,4,5,6,7,...]
# Read one integer at a time, and compute the running average of the previous n elements(inclusive). 
# n is given. 
# Write a function to implement this.
# public int readCurrent();

element_queue = []
current_ave = 0#(current_ave*n-element_pop+curr_element)/float(n)

def running_ave(stream, n):
    curr = stream.readCurrent()
    current_ave = curr/float(n)
    if len(element_queue)<n:
        element_queue.append(curr)
    else:
        element_pop=element_queue.pop()
        element_queue.append(curr)
    current_ave = (current_ave*n-element_pop+curr)/float(n)
    return current_ave

# f(w,x) = wTx
# y = sign(wTx)

# Pr_like(feed_data)
# designing the features:
#     1. freq of clicks
#     2. number of word mathch of feed with user's profile or interest








