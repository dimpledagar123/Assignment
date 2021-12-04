#!/usr/bin/env python
# coding: utf-8

# Write a Python program to square the elements of a list using map() function.
# 
# 
# 
# Sample List: [4, 5, 2, 9]
# 
# Square the elements of the list:
# 
# [16, 25, 4, 81]

# In[1]:


numbers = [4, 5, 2, 9]
def square(n):
      return n * n
result = map(square, numbers)
print(list(result))

