N = int(input())
X = []
Y = []
D = 0
for i in range(N):
    a = list(map(int, input().split()))
    X.append(a[0])
    Y.append(a[1])
def len(x1,x2,y1,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
for i in range (N):
    for j in range (N):
        if len (X[i],X[j],Y[i],Y[j]) >= D:
            D = len (X[i],X[j],Y[i],Y[j])
print(D)