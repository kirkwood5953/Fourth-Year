# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:57:24 2020

@author: pkirchen
"""

import numpy as np

def posnP(r1,z):
    '''
    Generate random position for polar coordinate system with max radius r
    position is returned as cartersion coords as x,y
    '''
    
    r = np.random.random(2)
    
    phi_p = 2*np.pi*r[0] # rad
    rad_p = r1 * np.sqrt(r[1])  # m
    
    x = rad_p*np.cos(phi_p)  # m 
    y = rad_p*np.sin(phi_p)  # m
    
    return np.array([x, y, z])




def posnX(lx,ly,lz):
    '''
    Generate a random position for cartesion surface with dimensions lx by ly
    Returns: x, y
    '''
    r = np.random.random(3)
    x = lx*r[0]
    y = ly*r[1]
    z = lz*r[2]
    
    return np.array([x, y,z])




def dirn():
    '''
    Define emission direction 
    dirn() returns unit vector components ux, uy, uz
    '''
    
    r=np.random.random(2)
    
    
    theta_d = np.arcsin(np.sqrt(r[0])) # rad
    phi_d = 2*np.pi*r[1] # rad
    
    # Generate vector
    ux = np.sin(theta_d)*np.cos(phi_d)
    uy = np.sin(theta_d)*np.sin(phi_d)
    uz = np.cos(theta_d)
    
    return np.array([ux, uy, uz])