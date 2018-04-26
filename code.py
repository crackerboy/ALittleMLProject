import csv
import math

X=[]#=[100,150,140,300,500,250,400,200,450,350,460,410,320,220,110,280,330,440,170,380]
Y=[]#=[1000,1150,1100,1500,2000,1400,1650,1230,1600,1650,1800,1680,1640,1300,1200,1440,1490,1820,1230,1600]
Xt=[]
Yt=[]


with open("RealEstate.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        if(row[0]=="MLS" or row[1]!="Santa Maria-Orcutt"):
            continue
        X.append(int(float(row[5])))
        Y.append(int(float(row[2])))

N=len(X)
Nt = int(N/10)

N -= Nt

Xt = X[N:]
X = X[:N]


Yt = Y[N:]
Y = Y[:N]

mnx = min(X)
mxx = max(X)

mny = min(Y)
mxy = max(Y)

X = [(a/(mxx-mnx)) for a in X]
Y = [(a/(mxy-mny)) for a in Y]

alpha = 0.0003

m = 1
n = 0

def calculateMSE():
    mse = 0
    for i in range(N):
        mse += ((Y[i]-(m*X[i]+n))**2)/2
    return math.sqrt(mse)

def calculateErrorT():
    ae = 0
    for i in range(Nt):
        print(Xt[i], Yt[i], m*Xt[i]+n)
        ae += (((Yt[i]-(m*Xt[i]+n))/Yt[i])**2)/Nt
    return math.sqrt(ae)*100

def derM():
    res = 0
    for i in range(N):
        res += -X[i]*(Y[i]-(m*X[i]+n))
    return res

def derN():
    res = 0
    for i in range(N):
        res += -(Y[i]-(m*X[i]+n))
    return res


while abs(derM())>0.00003 and abs(derN())>0.00003:
    newM = m - alpha*derM()
    newN = n - alpha*derN()
    m = newM
    n = newN

m *= (mxy-mny)/(mxx-mnx)
n *= (mxy-mny)

print(calculateErrorT())
