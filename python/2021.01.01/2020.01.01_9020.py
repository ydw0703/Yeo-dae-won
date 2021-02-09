def prime_list(n):
    sieve=[True]*n
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i+i,n,i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True]

T = int(input())
for _ in range(T):
    n = int(input())
    li = prime_list(n)
    a=[]
    for i in li:
        for j in li:
            if n == i+j:
                a.append([i,j]) 
                print(a)
    # print(a[0][0],a[0][1])
