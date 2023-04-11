import numpy as np
import scipy as sp
from matplotlib import pyplot as plt 

f = open("C:\\Users\\kylek\\Documents\\GitHub\\Fourth-Year\\478\\pCyl_filt.txt",'r')

data = np.loadtxt(f)
crankangle = data[:,0]
pressure = data[:,1]

# plt.plot(crankangle,pressure)
# plt.show()
cv = 0.717
R = 0.287
CR = 10
Vs = 0.55
Vc = np.round(0.55/(CR-1),3)
lc = 148.0
rct = 43.3
rpm = 2000
T = 33.2
nr = 2
volume = Vc*(1+(1/2*(CR-1))*(lc/rct + 1 - np.cos(np.deg2rad(crankangle))-np.sqrt((lc/rct)**2-(np.sin(np.deg2rad(crankangle))**2))))
mdot = 15.45/30 #g/s
cyclesdt = rpm/60/2 #cycle/s
m = mdot/cyclesdt 
LHV = 44
print(m)
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

bmep = T*2*np.pi*nr/Vs/10
fmep = imepgross - bmep
print("Indicated Mean Effective Pressure = ",imepgross)
print("Brake Mean Effective Pressure = ",bmep)
print("Friction Mean Effective Pressure = ",fmep)

indeff = winet/m/LHV/10
meff = bmep/imepnet
beff = indeff*meff
thermeff = 1-1/(CR**(1.4-1))

print("Indicated Efficiency = ",indeff)
print("Mechanical Efficiency = ",meff)
print("Brake Efficiency = ",beff)
print("Thermal Efficiency = ",thermeff)



brakePower = np.pi*rpm*T/30
BSFC = mdot/(brakePower/3.6e6)
print("Brake Specific Fuel Consumption (g/kWh)= ",BSFC)

Qin = m*LHV
print(Qin)
mR = pressure[900]*volume[900]/300
MaxTemp = max(pressure*volume)/mR
print(MaxTemp)