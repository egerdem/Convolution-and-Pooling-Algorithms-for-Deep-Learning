
# coding: utf-8

# # Convolution Implementation

# Input matrix is not necessarily be a square matrix, you can use w != h sized matrices as well
# Again, I used assertion errors to show size/shape incompatibility

# In[35]:


import numpy as np

input=np.random.randint(15, size=(6, 6))

filter=np.array([[2,0],[1,0]])

print("input = \n", input)
print("filter =\n",filter)


# In[45]:



h = input.shape[0]  # hight of the input matrix
w = input.shape[1]  # width of the input matrix 

stride = 2 
filtersize = filter.shape[0]
ConvRow=[]
p = 2

assert (h-filtersize) % stride == 0, "specified stride can not be applied to your input height, redefine your input/stride or do a padding beforehand "
assert (w-filtersize) % stride == 0, "specified stride can not be applied to your input width, redefine your input/stride or do a padding beforehand "

def convolution(A, f, s, padding=False):
    
    for i in range(0,h-f+1,s):
        for j in range(0,w-f+1,s):

            submatrix = A[np.ix_([i,i+f-1],[j,j+f-1])]
            subrow = submatrix.reshape(-1)  
            #print(a)
            ConvRow.append(np.sum(subrow*filter.reshape(1,filter.size)))
            ConvArray = np.array(ConvRow)
            
    Convolution=ConvArray.reshape(int((h-f)/s+1),int((w-f)/s+1))
    
    return(Convolution)

output = convolution(input, filtersize, stride, padding=False)

print("\nstride = ", stride)
print("\nfilter size = %d x %d" % (filtersize, filtersize))

print("\nPooling Applied Output =\n", output)


