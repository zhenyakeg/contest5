n = int(input())
A = list(map(int,input().split()))
num5 = A.count(5)
num10 = A.count(10)
num50 = A.count(50)
num100 = A.count(100)
num_cur,num_min = 0,0
for i in range (n):
    if A[i] == 5:
        num_cur+=1
    else:
        if A[i]//5-1 >= num_cur:
            num_min += A[i]//5 - 1 - num_cur
            num_cur = 0
        else:
            num_cur -= A[i]//5-1

print(num_min)