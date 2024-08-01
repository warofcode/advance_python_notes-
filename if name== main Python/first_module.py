#!/usr/bin/env python
# coding: utf-8

# In[2]:


def addition(*args):
    total = 0
    for i in args:
        
        total = total+i
        
    return total    
        
    
print(addition(1,5,6,6))   

def string_convertor(string):
    
    return string.upper()


print(string_convertor("i am good"))

print(f"name of module is {__name__}")


# In[ ]:




