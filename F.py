N=int(input())
A = list(map(int, input().split()))
d = abs(A[1]-A[0])
x_min = 0
y_min = 1
for i in range (len (A)):
    for j in range(len(A)):
        if abs(A[j]-A[i]) <= d and i != j:
            d = abs(A[j]-A[i])
            x_min = j
            y_min = i
if x_min > y_min:
    x_min, y_min = y_min, x_min
print(x_min,y_min)