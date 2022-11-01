#!/usr/bin/env python
# coding: utf-8
Python - 01

Q2. You will be given a list. You have to print a list whose 1st element should be largest and 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.

Input Format:

The first line will have space-separated elements of the list.

Output Format:

Print the required list.

Sample Input 0:

1 2 3 4 5 6

Sample Output 0:

6 1 5 2 4 3
# In[1]:


list1 = [1,2,3,4,5,6]
def S_D(list1):
    largest = list1[0]
    lowest = list1[0]
    largest2 = None
    lowest2 = None
    for item in list1[1:]:    
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 is None or largest2 < item:
            largest2 = item
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 is None or lowest2 > item:
            lowest2 = item
             
    print("Largest element is:", largest)
    print("Smallest element is:", lowest)
    print("Second Largest element is:", largest2)
    print("Second Smallest element is:", lowest2)
 
 
S_D(list1)

2.Find nth fibonacci number. If it starts with 0,1,1,2.....

Also, Print Incorrect Input if n is less than or equal to 0.

Input Format:

Call the function with n

Output Format:

Print the nth fibonacci number

Sample Input 0:

4

Sample Output 0:

2

Sample Input 1:

 0

Sample Output 1:

Incorrect input


# In[5]:


n = int(input('Enter : '))
fibo_nums = [0,1]
i=1
if(n==1 or n==2):
    print(n,'th Prime Number is :',fibo_nums[n-1])
    print('Fibonacci Series :', fibo_nums)
elif(n>2):
    while (True):
        fib = fibo_nums[i-1]+fibo_nums[i]
        fibo_nums.append(fib)
        if(len(fibo_nums)==n):
            break
        else:
            i+=1
    print(n,'th Fibonacci Number is :', fibo_nums[n-1])
    print('Fibonacci Series is :', fibo_nums)
else:
    print('Incorrect input')


# In[ ]:




