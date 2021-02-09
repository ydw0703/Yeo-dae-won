#직관적 코딩
# def pibonacci(n):
#     a=0
#     b=1
#     for _ in range(n-1):
#        a=b
#        b=a+b
#        print(a)
       
#        print(b)
#     return b

# n=int(input())
# print(pibonacci(n))

# n = int(input())
# f = [0] * (n + 1)                       # n + 1 만큼 리스트 생성
# def pibo(n):
#     if(f[n]) != 0:                      # f안에 값이 존재한다면
#         return f[n]                     # 재귀함수를 거치지 않고 그대로 출력

#     if n < 2: 
#         f[n] = n
#         return f[n]
#     else: f[n] = pibo(n-1) + pibo(n-2)  # f[n]에 저장
#     return f[n]
# print(pibo(n))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
n = int(input())
print(fibonacci(n))
