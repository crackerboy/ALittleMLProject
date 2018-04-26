import csv
import math
"""
X1=[100,150,140,300,500,250,400,200,450,350,460,410,320,220,110,280,330,440,170,380]
X2=[1,2,2,3,5,3,4,2,4,3,4,4,4,2,2,4,3,5,2,2]
X3=[1,1,2,2,4,4,3,2,3,1,1,2,3,3,2,2,3,6,1,2]
#Y=[1950,2750,2680,4800,7700,4300,6250,3400,6850,5350,6870,6320,5290,3690,2320,4760,5210,7080,2990,5560]
Y=[1900,2780,2640,4830,7670,4320,6250,3428,6842,5300,6892,6400,5330,3672,2313,4760,5250,7020,2995,5555]
"""
X1=[]
X2=[]
X3=[]
Y=[]
X1t=[]
X2t=[]
X3t=[]
Yt=[]

with open("RealEstate.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        if(row[0]=="MLS" or row[1]!="Santa Maria-Orcutt"):
            continue
        X1.append(int(float(row[5])))
        X2.append(int(row[3]))#Bedrooms
        X3.append(int(row[4]))#Bathrooms
        Y.append(int(float(row[2])))

N=len(X1)
Nt = int(N/10)

N -= Nt

X1t = X1[N:]
X1 = X1[:N]

X2t = X2[N:]
X2 = X2[:N]

X3t = X3[N:]
X3 = X3[:N]

Yt = Y[N:]
Y = Y[:N]

mnx1 = min(X1)
mxx1 = max(X1)

mnx2 = min(X2)
mxx2 = max(X2)

mnx3 = min(X3)
mxx3 = max(X3)

mny = min(Y)
mxy = max(Y)

X1 = [(a/(mxx1-mnx1)) for a in X1]
X2 = [(a/(mxx2-mnx2)) for a in X2]
X3 = [(a/(mxx3-mnx3)) for a in X3]
Y = [(a/(mxy-mny)) for a in Y]

alpha = 0.001

m1 = 1
m2 = 0
m3 = 0
n = 0

def calculateMSE():
    mse = 0
    for i in range(N):
        mse += ((Y[i]-(m1*X1[i] + m2*X2[i] + m3*X3[i] + n))**2)/2
    return math.sqrt(mse)

def calculateErrorT():
    ae = 0
    for i in range(Nt):
        print(X1t[i], X2t[i], X3t[i], Yt[i], m1*X1t[i]+m2*X2t[i]+m3*X3t[i]+n)
        ae += (((Yt[i]-(m1*X1t[i] + m2*X2t[i] + m3*X3t[i] + n))/Yt[i])**2)/Nt
    return math.sqrt(ae)*100

def derM1():
    res = 0
    for i in range(N):
        res += -X1[i]*(Y[i]-(m1*X1[i] + m2*X2[i] + m3*X3[i] + n))
    return res

def derM2():
    res = 0
    for i in range(N):
        res += -X2[i]*(Y[i]-(m1*X1[i] + m2*X2[i] + m3*X3[i] + n))
    return res

def derM3():
    res = 0
    for i in range(N):
        res += -X3[i]*(Y[i]-(m1*X1[i] + m2*X2[i] + m3*X3[i] + n))
    return res

def derN():
    res = 0
    for i in range(N):
        res += -(Y[i]-(m1*X1[i] + m2*X2[i] + m3*X3[i] + n))
    return res


while abs(derM1())>0.00001 or abs(derM2())>0.00001 or abs(derM3())>0.00001 or abs(derN())>0.00001:
    print(m1, m2, m3, n, calculateMSE())
    newM1 = m1 - alpha*derM1()
    newM2 = m2 - alpha*derM2()
    newM3 = m3 - alpha*derM3()
    newN = n - alpha*derN()
    m1 = newM1
    m2 = newM2
    m3 = newM3
    n = newN

m1 *= (mxy-mny)/(mxx1-mnx1)
m2 *= (mxy-mny)/(mxx2-mnx2)
m3 *= (mxy-mny)/(mxx3-mnx3)
n *= (mxy-mny)

print(calculateErrorT())
