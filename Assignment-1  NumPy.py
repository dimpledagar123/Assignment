#!/usr/bin/env python
# coding: utf-8
1. Create a null vector of size 10 but the fifth value which is 1.
2. Create a vector with values ranging from 10 to 49.
3. Create a 3x3 matrix with values ranging from 0 to 8
4. Find indices of non-zero elements from [1,2,0,0,4,0]
5. Create a 10x10 array with random values and find the minimum and maximum values.
6. Create a random vector of size 30 and find the mean value.
# In[1]:


import numpy as np

# NumPy version

np.__version__

# NumPy configuration

np.show_config()


# # Ans 1 : 

# In[2]:


null = np.zeros(10)

null[4] = 1


# # Ans 2:

# In[3]:


np.arange(10,50)


# # Ans 3:

# In[4]:


c = np.arange(0,9)

c.reshape(3,3)


# # Ans :4

# In[8]:


d = np.array([1, 2, 0, 0, 4, 0])

np.nonzero(d)


# # Ans :5

# In[6]:


e = np.random.random((10,10))

# minimum value

np.min(e)

# maximum values

np.max(e)


# # Ans :6

# In[7]:


f = np.random.random((5,6))

# mean values of matrix

np.mean(f)

                                                 Thank You