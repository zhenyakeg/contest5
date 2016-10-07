def sequence(k):
    A = [1]
    for a in range(k-1):
        count, number, i, j = [], [], 0, 0
        while i < len(A):
            if A[i] != A[j]:
                count.append(i-j)
                number.append(A[j])
                j = i
            i += 1
        count.append(i-j)
        number.append(A[j])
        A = []
        for b in range(len(count)):
            A.append(count[b])
            A.append(number[b])
    return int(''.join(map(str, A)))
print(sequence(int(input())))