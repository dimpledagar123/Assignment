#!/usr/bin/env python
# coding: utf-8

# 
# Python Candidates - Question 1
# 
# You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.
# 
# For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']
# 
# Input Format:
# 
# At first-line it will have an integer (number of elements inside a list). In the second line, it will have a string.
# 
# Output Format:
# 
# A single line containing a sorted list.
# 
# 

# In[11]:


def test(l):
    l1=[]
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j][-2]<l[j+1][-2]:
                pass
            else:
                l1=l[j]
                l[j]=l[j+1]
                l[j+1]=l1
    return l
n=int(input())
s=input()
t=s.split()
m=t[:n]
print(m)
test(m)


# In[ ]:




