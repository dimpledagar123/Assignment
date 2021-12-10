#!/usr/bin/env python
# coding: utf-8

# Write a Python class to implement pow(x, n)
# 
# 
# 
# Explanation:
# 
# Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
# 
# You must implement it using Class
# 
# 
# 
# Sample Input:
# 
# x: 10
# 
# n: 2
# 
# 
# 
# Sample Output:
# 
# 100
# 
# 

# In[1]:


class solution:
    
   def pow(cls, x, n):
        if x==0 or x==1 or n==1:
            return x 
        val = cls.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(solution().pow(10,2))

