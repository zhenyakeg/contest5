X = []
Y = []
for i in range (8):
    a=list(map(int, input().split()))
    X.append(a[0])
    Y.append(a[1])
def check(X,Y):
    for i in range (8):
        for j in range (8):
            if (X[i] == X[j] or Y[i] == Y[j] or abs(X[i]-X[j]) == abs(Y[i]-Y[j]) ) and i != j:
                return 'YES'
    return 'NO'
print(check(X,Y))