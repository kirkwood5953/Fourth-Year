import numpy as np
import planck as p
import radiosity as r

a1 = 4*np.pi()*1^2
a2 = np.pi()*0.3^2
h=1

f11 = 0
f12 = .5(1-1/(np.sqrt(1+(.3/h)^2)))
f13 = 1-f12
f21 = a1/a2*f12
f22 = 0
f23 = 1-f21
f31 = 0
f32 = 0
f33 = 1


f = np.array([[f11, f12, f13], [f21, f22, f23], [f31, f32, f33]])
T = np.array([600, 400, 0])
eps  = np.array([0.9, 0.3, 1])

qr = r.rad_encl_q(f,T,eps)

for i in range(qr.size):
    print ('Incident flux on surface {:1} = {:.4} W/m2'.format(i+1,qr[i])) 