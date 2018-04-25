X = [2, 4, 8]
Y = [5, 6, 8]
N = 3

alpha = 0.03

m = 1
n = 0

def calculateMSE():
    mse = 0
    for i in range(N):
        mse += (Y[i]-(m*X[i]+n))**2
    return mse

def derM():
    res = 0
    for i in range(N):
        res += -X[i]*(Y[i]-(m*X[i]+n))
    return res/N

def derN():
    res = 0
    for i in range(N):
        res += -(Y[i]-(m*X[i]+n))
    return res/N

print(m, n, calculateMSE())

while calculateMSE()>0.01:
    newM = m - alpha*derM()
    newN = n - alpha*derN()
    m = newM
    n = newN
    print(m, n, calculateMSE())
