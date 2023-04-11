import numpy as np
import scipy as sp
from matplotlib import pyplot as plt 
import os
import pandas as pd

#function for solving for data from files
def cylindercalcs(file,i):
    #opens file for reading
    f = open("C:\\Users\\kylek\\Documents\\GitHub\\Fourth-Year\\478\\pressuredata\\" + file,'r')
    #reads data from file
    results = np.array([])
    data = np.loadtxt(f)
    crankangle = data[:,0]
    pressure = data[:,1]

    #engine parameters
    cv = 0.717
    R = 0.287
    CR = 10
    Vs = 0.55
    Vc = np.round(0.55/(CR-1),3)
    lc = 148.0 #connecting rod length
    rct = 43.3 #crank throw radius
    rpm = 2000
    T = [3.9,7.8,10.4,12.8,15.2,20.9,27.2,33.2,38.8] #Brake Torque
    mdot = [5.60,6.50,7.34,8.20,9.09,11.13,13.5,15.45,17.49] #g/s
    injectiontime = [3355,4115,4670,5209,5738,6938,8260,9549,10821] #us
    nr = 2
    volume = Vc*(1+(1/2*(CR-1))*(lc/rct + 1 - np.cos(np.deg2rad(crankangle))-np.sqrt((lc/rct)**2-(np.sin(np.deg2rad(crankangle))**2))))

    
    m = mdot[i]/30*injectiontime[i]*1e-6
    LHV = 44.7
   
    dPdt = np.diff(pressure)/np.diff(crankangle)
    dVdt = np.diff(volume)/np.diff(crankangle)
    # print(max(volume))
    # print(min(volume))

    Qnet = cv/R*volume[0:3599]*dPdt+pressure[0:3599]*dVdt*(cv/R +1)
    # plt.plot(crankangle[0:3599],Qnet)
    # plt.show()
    # plt.plot(volume,pressure)
    # plt.show()

    winet = np.trapz(pressure,volume)
    imepnet = winet/Vs

    wigross = np.trapz(pressure[900:2700],volume[900:2700])
    imepgross = wigross/Vs

    bmep = T[i]*2*np.pi*nr/Vs/100
    fmep = imepgross - bmep
    pmep = imepgross -imepnet
    #adds values to results calc
    results=np.append(results,imepgross)
    results=np.append(results,fmep)
    results=np.append(results,bmep)
    results=np.append(results,pmep)


    indeff = winet/m/LHV/10
    meff = bmep/imepnet
    beff = indeff*meff
    thermeff = 1-1/(CR**(1.4-1))

    results=np.append(results,indeff)
    results=np.append(results,meff)
    results=np.append(results,beff)
    #NOT NEEDED FOR A)
    # print("Thermal Efficiency = ",thermeff)



    brakePower = np.pi*rpm*T[i]/30
    BSFC = m/(brakePower/3.6e6)
    results=np.append(results,BSFC)
    
    return  results

i = 0
finaldata = np.zeros((9,8))
#gets the data for each file in folder
for file in os.listdir("C:\\Users\\kylek\\Documents\\GitHub\\Fourth-Year\\478\\pressuredata"):
    finaldata[i] = cylindercalcs(file,i)
    i += 1
finaldata = np.round(finaldata,2)
#Seperates data into plotable values
table = finaldata
df = pd.DataFrame(table, columns = ['pig', 'pf', 'pb', 'pp','ni','nm','nb','BSFC'], 
                  index=['pin28', 'pin36', 'pin40', 'pin45','pin49','pin60','pin70','pin80', 'pin'])
print(df)

pig = finaldata[:,0]
pf = finaldata[:,1]
pb = finaldata[:,2]
pp = finaldata[:,3]
ni = finaldata[:,4]
nm = finaldata[:,5]
nb = finaldata[:,6]
BSFC = finaldata[:,7]

#plotting
plt.plot(pb, pig, label = 'pig')
plt.plot(pb, pf, label = 'pf')
plt.plot(pb, pp, label = 'pp')
plt.legend(loc = 'upper left')
plt.xlabel('Pb (Pa)')
plt.ylabel('Effective Pressure (Pa)')
plt.show()

plt.plot(pb, ni, label = 'ni')
plt.plot(pb, nm, label = 'nm')
plt.plot(pb, nb, label = 'nb')
plt.legend(loc = 'upper left')
plt.xlabel('Pb (Pa)')
plt.ylabel('Efficiency (%)')
plt.show()

plt.plot(pb, BSFC, label = 'BSFC')
plt.legend(loc = 'upper left')
plt.xlabel('Pb (Pa)')
plt.ylabel('Brake Specific Fuel Consumption (g/KW/h)')
plt.show()
