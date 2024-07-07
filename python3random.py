1)Write a Python function find_duplicates that takes a list of integers as input and returns a list containing only the duplicate integers from the original list. If there are no duplicates, return an empty list.

def find_duplicates(nums):
    # Your code here
    temp=set()
    dup=[]

    for i in nums:
        if i in temp and i not in dup:
            dup.append(i)
        else:
            temp.add(i)
    return dup

# Test cases
print(find_duplicates([1, 2, 3, 4, 5]))               # Output: []
print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))         # Output: [2, 1]
print(find_duplicates([1, 1, 1, 1, 1]))               # Output: [1]
print(find_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]))   # Output: []


2)# find greatest common divisor with the help of recursion
def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

# Example usage:
num1 = 36
num2 = 24
print("GCD of", num1, "and", num2, "is:", gcd_recursive(num1, num2))

# using while method
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 36
num2 = 24
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))

3)
