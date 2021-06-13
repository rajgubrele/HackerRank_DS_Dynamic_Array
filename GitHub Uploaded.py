#!/usr/bin/env python
# coding: utf-8

# Practice--> Data Structures--> Arrays--> Dynamic Array
# 
# Dynamic Array
# 

# In[ ]:


LA = 0
arr = []
result = []
for i in range(n):
    arr.append([])
for j in queries:
    if j[0]==1:
        idx = ((j[1]^LA)%n)
        arr[idx].append(j[2])
        
    else:
        idx = ((j[1]^LA)%n)
        LA  = arr[idx][j[2]%len(arr[idx])]
        result.append(LA)
return result

