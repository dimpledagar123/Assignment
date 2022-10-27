#!/usr/bin/env python
# coding: utf-8

# #### Given a string str, your task is to write a program which takes a string str as its only input and returns an integer denoting the no of palindromic subsequence (need not necessarily be distinct) which could be formed from the string str.
# 
# Input Format:
# 
# The first and only line of input contains string str.
# 
# Output Format:
# 
# The output will be an integer denoting the no of palindromic subsequence which could be formed from the string str.
# 
# Sample Input :
# 
# abcdef
# 
# Sample Output :
# 
# 6
# 
# Explanation:
# 
# For string 'abcdef' palindromic subsequence are : "a" ,"b", "c" ,"d","e","f"

# In[1]:


import itertools
def number_of_palindromic_subsequence():
    string=input("Enter the string :: ")
    a=[]
    for i in range(1,len(string)+1):
        for j in list(itertools.combinations(string, i)):
            if ''.join(j)==''.join(j)[::-1]:
                a.append(''.join(j))
            else:
                pass
    return print("number of palindromic subsequnce are :: ",len(a))
number_of_palindromic_subsequence()    


# #### You are given a graph and a number x as input. Your task is to print the DFS traversal nodes of the input graph starting from node x. Complete the following function in order to give the required output.
# 
# Input Format:
# 
# The first line of input contains a list containing sets representing a graph. The second line of input contains the number x. 
# 
# Output Format:
# 
# Complete the function in order to return the required output.
# 
# Sample Input 0:
# 
# [[1,0],[2,0],[3,0],[3,2]]
# 
# 3
# 
# Sample Output 0:
# 
# 3 0 2 

# In[5]:


graph= [[int(input("enter the 1st element :: ")), int(input("enter the 2 nd element :: "))] for i in range(int(input("Enter the number of elemnts in the list :: ")))]
#graph=[[1,0],[2,0],[3,0],[3,2]]
visited=set()

# Creating list of all vertex
x=[]
for i in graph:
    x.extend(i)
vertex=list(set(x))

# creating the graph as a dictionary from the user inout nested list
d = {}
for a, b in graph:
    d.setdefault(a, []).append(b)
for v in vertex:
        if v not in d:
            d[v] = []

# user input of root node or starting node
root=int(input("enter the root node"))

# implementing depth-first-search (DFS)
def dfs(visited,graph,root):
    if root not in visited:
        print(root,end=' ')
        visited.add(root)
        for i in set(d[root])-visited:
            dfs(visited,graph,i) 

dfs(visited,graph,root)


# In[ ]:




