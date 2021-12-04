#!/usr/bin/env python
# coding: utf-8

# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# 
# 
# 
# sample list: [1, 2, 3, 4, 5, 6, 7]
# 
# 
# 
# Triple of list numbers:
# 
# [3, 6, 9, 12, 15, 18, 21]

# In[1]:


nums = (1, 2, 3, 4, 5, 6, 7) 
print("Before Triple list No.: ", nums)


# In[2]:


result = map(lambda x: x + x + x, nums) 
print("\n Afetr Triple list No.:")
print(list(result))

