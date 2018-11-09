
# coding: utf-8

# In[3]:


def binary_search(input_array, value):
    """Your code goes here."""
#     f=False
    if (len(input_array) == 0):
        f=False
    else:
        midpoint = len(input_array)//2
        if (input_array[midpoint]==value):
#             print("lets compare values ", input_array[midpoint],value)
            f=True
#             print("Inner value of flag ",f)
        else:
            if (value<input_array[midpoint]):
#                 print(input_array[:midpoint])
                return binary_search(input_array[:midpoint],value)
            else:
#                 print(input_array[midpoint+1:])
                return binary_search(input_array[midpoint+1:],value)
        
#     print("Out of loop ", f)
    return f
binary_search([1,3,9,11,15,19,29], 19)

