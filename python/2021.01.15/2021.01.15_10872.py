def factorial(n):
    a=1
    for i in range(1,n+1):
       a=i*a
    return a

N=factorial(int(input()))
print(N)