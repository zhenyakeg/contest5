a = list(map(int, input().split()))
N = a[0]
A = a[1]
B = a[2]
C = a[3]
D = a[4]
Num = []
for i in range (1,N+1):
    Num.append(i)
for i in range ((B-A)//2+(B-A)%2):
    Num[A+i-1],Num[B-i-1] = Num[B-i-1],Num[A+i-1]
for i in range ((D-C)//2+(D-C)%2):
    Num[C+i-1],Num[D-i-1] = Num[D-i-1],Num[C+i-1]
print (' '.join(map(str, Num)))