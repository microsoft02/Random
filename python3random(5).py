#1) Fibonacci Sequence: Write a Python function to generate the Fibonacci sequence up to a specified number of terms.
def fib_check(val):
    temp=[0,1]

    for i in range(2,val):
        # just remember this formula for fib 
        temp.append(temp[i-1] + temp[i-2])
    return temp

value=int(input('enter:'))
print(fib_check(value))


# 2) Palindrome Check: Write a Python function to check if a given string is a palindrome.
def palin(word):
    # way1
    clean= ''.join(char for char in word if char.isalnum())
    reversi= reversed(clean)

    # way2 
    # reversi=clean[::-1]

    #way3
    # reversi=''
    # for letter in clean:
    #     reversi = letter + reversi

    return "it's palindrome" if clean == reversi else "it's not palindrome"

word=input('enter:')
print(palin(word))

#3) Prime Number Check: Write a Python function to determine whether a given number is prime or not.
def prime_check(val):

    if  val <= 1 : # checking if it's 1
        return 'is unique number and non-prime number'
    
    for num in range(2,int(val ** 0.5) + 1): # ** use to get root but it give answer in float so we take only whole value using int data coversion
        if val % num == 0:
            return 'it is not prime number'

    #if all above don't match then
    return 'it is prime number'

num=int(input('enter:'))
print(num,prime_check(num))


#1) Explain the difference between a tuple and a list in Python.
# ->tuple is collection of similar or different type of datatype. tuple is im-mutable datatype mean the element can't be change once tuple created. tuple is represent by () round bracket.
# eg.
my_tuple=(4,6,2)
# my_tuple[0]=10 # get error when try to change
print(my_tuple) #-> 4,6,2

# ->list it is same as tuple. but list is mutable. so the element can be change after list can be created. list is represent by [] square bracket
# eg.
my_list=[1,3,5]
my_list[0]=10
print(my_list) #->10,3,5


# 2) What is the purpose of the __init__ method in Python classes?
# ->__init__ is use to initialize the instance of class object. __init__ method in Python classes serves as a constructor method. It is automatically called when a new instance of a class is created.
# we give attribute in init method and attribute use to assign the values of object. we pass the parameter to class we we create instance
class Person:
    def __init__(self, name, age):
        self.name = name  #attribute??
        self.age = age

# Creating instances of the Person class
person1 = Person("Alice", 30)  #parameter or argument ??
print(person1.name, person1.age)   #Output: Alice 30


#3) How does Python handle exceptions, and what are some common built-in exceptions?
# in python execption handling done through try, except and finally block. try block is where we write our experimental code you want to monitor for exceptions.
# except block catches and handles exceptions that occur within the corresponding try block. You can have multiple except blocks to handle different types of exceptions differently.
# finally This block is optional. finally block always run.
# eg.
try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always runs, regardless of exceptions.")
