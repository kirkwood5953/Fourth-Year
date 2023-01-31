# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:27:37 2020

@author: pkirchen
"""

import numpy as np
import scipy.integrate as sp

def planck_elb(lam,T):
    """
    planck_elb(lam,T) calculates the hemispherical spectral emissive power for
    for a blackbody using the Planck Law
    
    Inputs: 
        lam: wavelength in [m]
        T: temperature in [K]
        
    Output
        E_lb: Hemispherical spectral emissive power [W/m2/um]
    """
    
    h = 6.62607e-34 ## Planck constant [Js]
    kb = 1.38065e-23 ## Boltzmann constant [J/K]
    c0 = 2.9979e8 ## Speed of light in vacuum [m/s]
    n=1 ## index of refraction [-]
    
    E_lb = 2 * np.pi * h * c0**2 / (n**2 * lam**5 * (np.exp(h*c0/(n*kb*lam*T))-1)) 
    

    
    return E_lb

def blackF(lamT):
    """
    blackF(lamT) calculates the hemispherical blackbody emissive power fraction 
    for the wavelength temperature product lamT
    
    Inputs:
        lamT: product of wavelenght and temperature [umK]
        
    Output 
        f_lamT: Emissive power fraction 
    
    Patrick Kirchen 
    v0 20200107
    """
    
    sb = 5.67e-8    # Stefan-Boltzmann constand [W/m2/K]
    
    f_lamT = 1/sb * sp.quad(planck_lt, 0, lamT*1e-6)[0] *1e6
    
    return f_lamT

def planck_lt(lamT):
    """
    planck_lt(lamT) calculates the hemispherical spectral emissive power for 
    a blackbody, given the prodcut lamT (wavelength*Temperature; m*K)
    
    Inputs:
        lamT: product of wavelenght and temperature [mK]
        
    Output 
        E_lbT5: Hemispherical spectral emissive power / T^5 
    
    Patrick Kirchen 
    v0 20200107
    """
    
    h = 6.62607e-34 ## Planck constant [Js]
    kb = 1.38065e-23 ## Boltzmann constant [J/K]
    c0 = 2.9979e8 ## Speed of light in vacuum [m/s]
    n=1 ## index of refraction [-]
    
    ##lam = 1000e-9 ## wavelength [m]
    ##T = 1000 ## Temperature [K]
    
    E_lbT5 = 2 * np.pi * h * c0**2 / (n**2 * (lamT)**5 * (np.exp(h*c0/(n*kb*lamT))-1)) *1e-6
    
##    E_lb =  np.divide(2 * np.pi * h * c0**2, n**2 * np.multiply(np.power(lam,5),(np.exp(h*c0/(n*kb*np.multiply(lam,T)))-1)))*1e-6
    
#    I_lb = E_lb/np.pi
    
    return E_lbT5


def appT(i, lam):
    '''
    appT(i, lam) calculates the apparent blackbody temperature for a specified
    intensity and wavelength 
    
    Inputs:
        i: radiative intensity [W/m2/m]
        lam: wavelength [m]
        
    Output 
        Tapp: apparent blackbody temperature [K]
    
    Patrick Kirchen 
    v0 20200406
    '''
    
    h = 6.62607e-34 ## Planck constant [Js]
    kb = 1.38065e-23 ## Boltzmann constant [J/K]
    c0 = 2.9979e8 ## Speed of light in vacuum [m/s]
    n=1 ## index of refraction [-]
    
    c2 = h*c0/kb
    c1 = h*c0**2
    
    Tapp = c2/(lam*np.log(2*c1/(i*lam**5)+1))
    
    return Tapp
