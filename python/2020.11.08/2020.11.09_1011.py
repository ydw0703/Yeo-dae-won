# T=int(input())
# x=int(input())
# y=int(input())

# n^ 2
# sum(1,n) + 뒤에서부터 sum()
# if 뒤에서부터 sum()의 원소가 n보다 커지면 다시 1을 더한다. 


# 백엔드 지식
# 호스팅 VS 클라우드
# 웹 호스팅: 1개 물리서버 자원 많은 사용자들이 나눠 씀.
# VPS호스팅: 1개 물리서버 자원 몇몇의 사용자들이 나눠 씀. (Virtual Private Server)
# 서버호스팅: 1개 물리서버 자원을 한 명의 사용자가 씀.
# 클라우드: 가상의 물리서버를 몇몇의 사용자들이 독립적으로 사용. 서버 물리자원 자유롭게 추가 가능.

import math
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    diff = int(y - x)
    if diff <= 3:
        print(diff)
    else:
        n = int(math.sqrt(diff)) #소수점 아래를 버림으로써 정수만 남겨둠.
        if diff == n ** 2:
            print(2*n-1)
        elif n ** 2 < diff <= n ** 2 + n:
            print(2*n)
        else:
            print(2*n+1)
