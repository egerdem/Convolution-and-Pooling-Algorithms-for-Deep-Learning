
# coding: utf-8

# # Pooling Implementation

# I wrote this question's codes completely on my own. To demonstrate the operation easily, currently it takes a 2D matrix with any shape and applying a pooling operation with a user specified pooling size and the stride. One can easily increase channel and the depth by changing input data size and update the indices at the pooling operation line which is basically done in only one line.
# 
# * Input matrix is not necessarily be a square matrix, you can use w != h sized matrices ass well, as shown below
# * I used assertion errors to show size/shape incompatibility

# In[47]:


import numpy as np
import nbconvert

#define your input data/image matrices
input=np.random.randint(28, size=(4, 7))  

print("input = \n", input)

poolsize=2 


# In[48]:


# N, C, h, w = input.shape  
# one can use the above definition if increase the input size, rather than define the size parameters seperately

h = input.shape[0]  # hight of the input matrix
w = input.shape[1]  # width of the input matrix 

stride = 1 #stride

pooled=[]

assert (h-poolsize) % stride == 0, "specified stride can not be applied to your input height, redefine your input/stride or do a padding beforehand "
assert (w-poolsize) % stride == 0, "specified stride can not be applied to your input width, redefine your input/stride or do a padding beforehand "

def pooling(A, p, s, padding=False):
    
    if not padding:
        print('no padding')
        for i in range(0,h-p+1,s):
            for j in range(0,w-p+1,s):
                
                pooled.append(np.amax(A[np.ix_([i,i+p-1],[j,j+p-1])]))
                pp = np.array(pooled)
        result=pp.reshape(int((h-p)/s+1),int((w-p)/s+1))
    return(result)

output = pooling(input,poolsize,stride)

print("\nPooling Applied Output =\n", output)

