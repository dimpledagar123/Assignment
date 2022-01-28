#!/usr/bin/env python
# coding: utf-8

# Solve these questions in a Jupyter notebook. Share the URL of the Jupyter notebook/GitHub.
# 
# 
# 
# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
# 
# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
# 
# Q3. Write a program to check if two strings are a rotation of each other?
# 
# Q4. Write a program to print the first non-repeated character from a string?
# 
# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
# 
# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
# 
# Q7. Write a program to convert prefix expression to infix expression.
# 
# Q8. Write a program to check if all the brackets are closed in a given code snippet.
# 
# Q9. Write a program to reverse a stack.
# 
# Q10. Write a program to find the smallest number using a stack.

# # Answer 1.

# In[1]:


def printPairs(arr, n, sum):
 
    # count = 0
 
    # Consider all possible
    # pairs and check their sums
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep = "")
 
 
# Driver Code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)


# # Answer 2.

# In[3]:


arr = [1, 2, 3, 4, 5]
print("Array is :",arr)
 
res = arr[::-1] #reversing using list slicing
print("Resultant new reversed array:",res)


# # Answer 3.

# In[18]:


def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
 
    # Create a temp string with value str1.str1
    temp = string1 + string1
 
    # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of
    # the second string in temp
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
 
# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"
 
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")


# # Answer 4.

# In[8]:


'''
for ( i=0 to str.length())
hash_map[str[i]]++;

for(i=0 to str.length())
  if(hash_map[str[i]]==1)
  return str[i]

'''

NO_OF_CHARS = 256
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 
# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 
# Driver program to test above function
string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is" , string[index])


# In[19]:


str1 = input(">>>" )
found = None

for i in str1:
    if (str1.count(i) == 1):
        print("the first founded string variable is: ",i)
        found = True
        break

if (found == False):
    print("there is non repeating char in str1")


# # Answer 5.

# In[20]:


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
    
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')


# # Answer 6.

# In[10]:


def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convert postfix to Prefix expression
 
 
def postToPre(post_exp):
 
    s = []
 
    # length of expression
    length = len(post_exp)
 
    # reading from right to left
    for i in range(length):
 
        # check if symbol is operator
        if (isOperator(post_exp[i])):
 
            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            # concat the operands and operator
            temp = post_exp[i] + op2 + op1
 
            # Push string temp back to stack
            s.append(temp)
 
        # if symbol is an operand
        else:
 
            # push the operand to the stack
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
 
# Driver Code
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    # Function call
    print("Prefix : ", postToPre(post_exp))


# # Answer 7.

# In[11]:


def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
# Driver code
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# # Answer 8.

# In[12]:


def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:

            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"

    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# # Answer 9.

# In[13]:


class Stack:

    def __init__(self):
        self.Elements = []

    def push(self, value):
        self.Elements.append(value)
        
    def pop(self):
        return self.Elements.pop()
    
    def empty(self):
        return self.Elements == []

    def show(self):
        for value in reversed(self.Elements):
            print(value)

def BottomInsert(s, value):

    if s.empty():

        s.push(value)

    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)

stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()


# # Answer 10.

# In[15]:


First = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number: '))
    First.append(numbers)
    
print("Smallest number in the list is :  ", min(First))


# In[ ]:




