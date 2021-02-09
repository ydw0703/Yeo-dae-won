#인터넷의 코드

n,x = map(int,input().split())
a=list(map(int,input().split()))

for i in range(n):
    if x>a[i]:
        print(a[i], end = " ")


# AttributeError: module 'random' has no attribute 'range'

# random 모듈이  range라는 함수를 가지고 있지 않다!