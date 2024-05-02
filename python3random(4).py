#1) Write a Python function to check if a string is a palindrome.
def palindrome(word):
	clean_Word =  ''.join(char for char in word if char.isalnum())

	# way 1 - slicing    
	reversed_Word = clean_Word[::-1]
	
	# way 2 - reverse method
	# reversed_Word = reversed(clean_Word)
		
	# way 3 - for loop
	# reversed_Word = ''
	# for char in clean_Word:
	# 	reversed_Word= char + reversed_Word 
	# 	print(reversed_Word)

	return 'it is palindrome' if reversed_Word == clean_Word else 'it is not palindrome'

string= input('enter word:')
print(string, palindrome(string))


#2) Implement a Python function to calculate the factorial of a given number recursively.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
	
num=int(input('enter the value'))
print(num,'factorial answer:',factorial(num))


#3) Create a Python program to find the largest and smallest elements in a list.
def finder(num):
    if not num: # just check before if that list is empty or not
        return None, None

    # way 1
    temp=sorted(num)
    lowest=temp[0]
    highest= temp[-1]
    

    # way 2
    # lowest = highest = num[0]
    # for n in num:
    #     if n < lowest:
    #         lowest = n
    #     elif n > highest:
    #         highest = n

    return lowest, highest

temp_list=[4,3,1,5,2]
lowest, highest = finder(temp_list)

if lowest is not None and highest is not None: # if it not none than get value
    print('the lowest',lowest,'and highest:', highest)
else:
    print('list is empty')


#1) What is the difference between a list and a tuple in Python?
# -> list is collection of similar or different type of datatype. list is mutable so the elements in the list can be changed after the list is created. list represent by square bracket []. 
# eg. 
list1=[1,2,3,4]
print(list1)
# -> tuple is same as lit but it is im-mutable so element can not be change later. tuple represent by round bracket ().
# eg.
tuple1=(1,2,3,4)
print(tuple1)


#2) Explain the concept of list comprehension in Python with an example.
# -> list comprehension is compact syntax to create list. it generate new list by iterate over existing iterable like list, tuple or string.
# eg.
word='hello'
character =[char for char in word] # need in square bracket
print(character)


#3) How does Python's garbage collection work, and why is it important?
# -> it work in two way 1) reference counting  2) cyclic garbage collection
  # 1) reference counting -> simple and efficient technique called reference counting it count the reference of each object. when object count become 0(zero). python deallocate the memory.
  # 2) cycalic garbage collection -> reference counting good but can't count reference in cyclic refernce(like continueous track of counting) .so you ahve to seperate the cyclic garbage
  #  collection that scan the all object and collect reference of object.

# why it is important
  #1) Memory Management-> It automatically manages memory, free the resources when they are no longer needed.
  #2) Optimization-> By getting memory back from unused objects,garbage collection helps optimize memory usage and improves overall performance by making more memory available for allocation to new objects.

