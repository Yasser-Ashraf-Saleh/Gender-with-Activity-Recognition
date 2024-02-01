import numpy as np
import os
import scipy.io as sio

files=os.listdir('//')
x=[]

for file in files:
    matfile =sio.loadmat(file)
    A=matfile['data1']
    print(A.shape[0])
    #segment=A.shape[0]//5
    i=0
    for start in range (0, A.shape[0],180):
        seg=A[start:start+180, :]
        sio.savemat(file[:11] +str(i) +".mat", {'data1':seg})
        i=i+1
        
        
        
        
