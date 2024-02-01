# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:01:01 2020

@author: ahmed
"""

import scipy.io
import os
import numpy as np
import pandas as pd
import statsmodels
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



'''reading files'''

path = "//"

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.mat' in file:
            files.append((file))

f = scipy.io.loadmat(files[0])['data1']
###############################################

ident=input("choose mode between 'gender','acts', or 'all' : ")            


def processFile(matfile,order, ident):

        file = scipy.io.loadmat(matfile)
        new=(file['data1'])[:,[10,11,12]]#file is a dictionary. The actual data is the value of the 'data1' key , aceleration on right hand
        

        global x_r
        global y_r
        global z_r
        
        global x_w
        global y_w
        global z_w
               
        global x_c
        global y_c
        global z_c       
        
        global x_b
        global y_b
        global z_b   
        
        
        global sss
        
        if ident == "gender":
            
            if 'M' in matfile :
                print("M")
                x_M.append(new[:,0].tolist())
                y_M.append(new[:,1].tolist())
                z_M.append(new[:,2].tolist())
                        
                         
            else:
                print("F")
                x_F.append(new[:,0].tolist())
                y_F.append(new[:,1].tolist())
                z_F.append(new[:,2].tolist())

 
        elif ident == "acts":
            if 'run' in matfile:
                print('run')
                # processFile(file,0)
                x_r.append(new[:,0].tolist())
                y_r.append(new[:,1].tolist())
                z_r.append(new[:,2].tolist())
                    
            elif 'wal' in matfile:
                print('walk')                
                # processFile(file,2)
                x_w.append(new[:,0].tolist())
                y_w.append(new[:,1].tolist())
                z_w.append(new[:,2].tolist())
                
            elif 'bye' in matfile:
                print('bye')                
                # processFile(file,4)
                x_b.append(new[:,0].tolist())
                y_b.append(new[:,1].tolist())
                z_b.append(new[:,2].tolist())            
            
            elif 'cla' in matfile:
                print('clapping')                
                # processFile(file,6)
                x_c.append(new[:,0].tolist())
                y_c.append(new[:,1].tolist())
                z_c.append(new[:,2].tolist())
                
                
        elif ident == "all":
            if 'M' in matfile :
                if 'run' in matfile:
                    print('m run')
                    # processFile(file,0)
                    x_r.append(new[:,0].tolist())
                    y_r.append(new[:,1].tolist())
                    z_r.append(new[:,2].tolist())
                        
                elif 'wal' in matfile:
                    print('m walk')                
                    # processFile(file,2)
                    x_w.append(new[:,0].tolist())
                    y_w.append(new[:,1].tolist())
                    z_w.append(new[:,2].tolist())
                    
                elif 'bye' in matfile:
                    print('m bye')                
                    # processFile(file,4)
                    x_b.append(new[:,0].tolist())
                    y_b.append(new[:,1].tolist())
                    z_b.append(new[:,2].tolist())            
                
                elif 'cla' in matfile:
                    print('m clapping')                
                    # processFile(file,6)
                    x_c.append(new[:,0].tolist())
                    y_c.append(new[:,1].tolist())
                    z_c.append(new[:,2].tolist())
                         
            else:
                if 'run' in matfile:
                    print('f run')
                    # processFile(matfile,1)
                    x_r_f.append(new[:,0].tolist())
                    y_r_f.append(new[:,1].tolist())
                    z_r_f.append(new[:,2].tolist())
                        
                elif 'wal' in matfile:
                    print('f walk')
                    # processFile(file,3)
                    x_w_f.append(new[:,0].tolist())
                    y_w_f.append(new[:,1].tolist())
                    z_w_f.append(new[:,2].tolist())
                    
                elif 'bye' in matfile:
                    print('f bye')                
                    # processFile(file,5)
                    x_b_f.append(new[:,0].tolist())
                    y_b_f.append(new[:,1].tolist())
                    z_b_f.append(new[:,2].tolist())           
                    
                elif 'cla' in matfile:
               
                    x_c_f.append(new[:,0].tolist())
                    y_c_f.append(new[:,1].tolist())
                    z_c_f.append(new[:,2].tolist())
        
        
        return 0


''' activities with gender plotting '''
x_r=[]
y_r=[]
z_r=[]

x_w=[]
y_w=[]
z_w=[]


x_c=[]
y_c=[]
z_c=[]


x_b=[]
y_b=[]
z_b=[]

x_r_f=[]
y_r_f=[]
z_r_f=[]

x_w_f=[]
y_w_f=[]
z_w_f=[]


x_c_f=[]
y_c_f=[]
z_c_f=[]


x_b_f=[]
y_b_f=[]
z_b_f=[]

''' gender plotting '''
x_M=[]
y_M=[]
z_M=[]


x_F=[]
y_F=[]
z_F=[]

def get_data():    
    for file in files:
        processFile(file,1,ident)
        

get_data()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


if ident == "acts":
    ax.scatter(x_r[:5], y_r[:5], z_r[:5], c='r', marker='o')
    ax.scatter(x_b[:5], y_b[:5], z_b[:5], c='b', marker='^')
    ax.scatter(x_w[:5], y_w[:5], z_w[:5], c='black', marker="*")
    ax.scatter(x_c[:5], y_c[:5], z_c[:5], c='y', marker="s")

elif ident == "gender":
    ax.scatter(x_M[1250:1256], y_M[1250:1256], z_M[1250:1256], c='r', marker='o')
    ax.scatter(x_F[1250:1256], y_F[1250:1256], z_F[1250:1256], c='b', marker="d")
    
elif ident == "all":
    ax.scatter(x_r[:5], y_r[:5], z_r[:5], c='r', marker='.')
    ax.scatter(x_b[:5], y_b[:5], z_b[:5], c='b', marker='^')
    ax.scatter(x_w[:5], y_w[:5], z_w[:5], c='g', marker=">")
    ax.scatter(x_c[:5], y_c[:5], z_c[:5], c='y', marker="P")
    ax.scatter(x_r_f[:5], y_r_f[:5], z_r_f[:5], c="k", marker="o")
    ax.scatter(x_b_f[:5], y_b_f[:5], z_b_f[:5], c="orange", marker="v")
    ax.scatter(x_w_f[:5], y_w_f[:5], z_w_f[:5], c='lightblue', marker="s")
    ax.scatter(x_c_f[:5], y_c_f[:5], z_c_f[:5], c='brown', marker="X")



ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


