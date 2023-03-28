# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:06:45 2020

@author: pkirchen
"""

import numpy as np 

def delk(k,j):
    """
    delk(k,j) returns the kroenecker delta function for k,j. 
    """
    if k==j:
        d=1
    else:
        d=0 
        
    return d
            
def rad_encl_q(f,T,eps):
    """
    rad_encl(f,T,eps) applies the master net flux equation to an enclosure
    to solve for the net flux at each surface (incoming flux >0). 
    N: number of surfaces
    
    Input Parameters
    f: [NxN] matrix of shape factors 
    T: [Nx1] vector of surface temperatures 
    eps: [Nx1] vector of surface emissivities 
    
    Output Parameters 
    q: [Nx1] vector of net flux 
    
    v1: 20200213
    """
       
    N = f.shape[0]
    sig = 5.67e-8 #W/m^2/K^4
    
    # initialize coefficient matrices 
    a = np.zeros(f.shape) 
    cj = np.zeros(f.shape)
    c = np.zeros(N)
    
    for k in range(N):
        for j in range(N):
            a[k,j] = delk(k,j)/eps[j] - f[k,j]*(1-eps[j])/eps[j]
            cj[k,j] = f[k,j]*sig*(T[k]**4 - T[j]**4)
        c[k] = sum(cj[k,:])
    
    # solve 
    q = np.linalg.inv(a).dot(c)
    
    return q
        