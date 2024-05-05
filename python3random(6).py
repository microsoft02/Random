#1) Word Count: Write a Python function that takes a string as input and returns the count of each word in the string.
def count_word(words):
    temp={}
    word=words.split() # this is need we need to count word not single character. if count character comment out this
    for char in word:
        temp[char]=temp.get(char,0)+1
    return temp

word=input('enter word:')
print(count_word(word))


#2) Factorial Calculation: Write a Python function to calculate the factorial of a given number.
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n - 1)

val=int(input('enter value:'))
print(fact(val))


#3) List Manipulation: Write a Python function that takes a list of integers as input and returns a new list with only the even numbers from the original list.
def find_even(element):
    temp=[]
    for num in element:
        if num % 2 == 0:
            temp.append(num)
            
    # temp=sorted(temp) # if want to get sort asceding way
    return temp  

my_list=[6,1,3,4,2,5,8,7]
print('old list:',my_list)
print('new list:', find_even(my_list))


#1)Explain the difference between a shallow copy and a deep copy in Python.
# -> shallow copy: shallow copy is create copy the outmost layer of object not the nested element. but copies the references to the nested objects.
#  the memory adress or id is same of new copy.
# eg.
import copy

list1 = [1, 2, [5, 6], 4]
list2 = copy.copy(list1) # Shallow Copy
list1[2][0] = 3
print('Shallow Copy:')
print('list1:', list1)  # Output: [1, 2, [3, 6], 4]
print('list2:', list2)  # Output: [1, 2, [3, 6], 4]

# -> deep copy: A deep copy creates a completely new object with its own copy of the nested objects. the memory address or id of new copy is different.
list3 = copy.deepcopy(list1) # Deep Copy
list1[2][1] = 7
print('Deep Copy:')
print('list1:', list1)  # Output: [1, 2, [3, 7], 4]
print('list3:', list3)  # Output: [1, 2, [3, 6], 4]


#2)
