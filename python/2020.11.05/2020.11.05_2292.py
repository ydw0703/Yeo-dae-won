#           방의개수(6*x) 
# 1: 1        1
# 2~7: 2      6
# 8~19: 3     12
# 20~37: 4    18
# 38~61: 5    24
# 62~93: 6    30
# 규칙이다.

# a = int(input())

# count=0
# for i in range(a):
#     i=6*i

#     count+=1
# print(count)
    
#인터넷 코드1
N = int(input())
first = 1
plus = 6
room = 1
#1번방에서 안움직일 경우
if N == 1:
    print(1)
#2번방부터의 경우
else:
    while True:
        #방 번호 수
        first = first + plus
        #통과할 방 개수 증가
        room+= 1
        #방 번호가 방 개수인 동안
        if N <= first:
            print(room)
            break
        #방 개수는 6씩 증가
        plus += 6

#인터넷 코드2
N = int(input())
cnt = 1
while N > 1: #while문의 조건에서, 입력값이 최대값이므로 변수가 두 개가 되는 것을 방지하기 위해 입력값에서부터 소멸되는 것을 선택했다.
    N -= (6 * cnt)
    cnt += 1
print(cnt)