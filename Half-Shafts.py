from math import *

r = 0.25 # m radius of wheels
Twheel = 140 # N-m torque from the motor * drivetrain efficiency 
density = 7850 #kg/m^3
Length =  0.5 # m Length of Half Shaft 
ID = [] 
OD = []
m_shaftless = 300 #Kg 
Tmax = 4.7*140 # N-m peak torque
TEngineBraking = 0 # the value should include the negative sign
Tamp = 0.5*(Tmax-TEngineBraking) 
Tmean = 0.5*(Tmax+TEngineBraking)
Kfs_tor = 1.1
nf = 1.5
Sut = 1294*10**6 # Pa
Se = 0.3*Sut
Sy = 862*10**6 # Pa
Acc = []

# a = (16*r*Twheel)/(density*Length*3.14*(OD**4-ID**4+8*r*r(OD**2-ID**2))+16*r*r*m_shaftless)

# ID = (OD**4 - (16*sqrt(3)*sqrt(OD**2*nf**2*Se**2*Sy**2*Kfs_tor**2*(Sy**2*Tamp**2+Se**2*Tmean**2)))/(3.14*Se**2*Sy**2))**(1/4)


# for j in range(1,500,0.5):
#         j=j/100
#         if j**4 - (16*sqrt(3)*sqrt((j**2)*(nf**2)*(Se**2)*(Sy**2)*(Kfs_tor**2)*((Sy**2)*(Tamp**2)+(Se**2)*(Tmean**2))))/(3.14*(Se**2)*(Sy**2))>0:
#             i = (j**4 - (16*sqrt(3)*sqrt((j**2)*(nf**2)*(Se**2)*(Sy**2)*(Kfs_tor**2)*((Sy**2)*(Tamp**2)+(Se**2)*(Tmean**2))))/(3.14*(Se**2)*(Sy**2)))**(1/4)
#             ID.append(i)
#             OD.append(j)
#             a = (16*r*Twheel)/(density*Length*3.14*((j**4)-(i**4)+8*r*r*((j**2)-(i**2)))+16*r*r*m_shaftless)
#             Acc.append(a)

# print(ID,OD,Acc)

# i = max(Acc)
# j=Acc.index(i)

# print(i,ID[j],OD[j])


j = ((16*sqrt(3)*sqrt((nf**2)*(Se**2)*(Sy**2)*(Kfs_tor**2)*((Sy**2)*(Tamp**2)+(Se**2)*(Tmean**2))))/(3.14*(Se**2)*(Sy**2)))**(1/3)
print(j)
i=0
print((16*r*Twheel)/(density*Length*3.14*((j**4)-(i**4)+8*r*r*((j**2)-(i**2)))+16*r*r*m_shaftless))
print((j**4 - (16*sqrt(3)*sqrt((j**2)*(nf**2)*(Se**2)*(Sy**2)*(Kfs_tor**2)*((Sy**2)*(Tamp**2)+(Se**2)*(Tmean**2))))/(3.14*(Se**2)*(Sy**2)))**(1/4))

            

