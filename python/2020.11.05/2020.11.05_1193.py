# 분수+분모의 합이 
# 2 이면 1      1
# 3 이면 2~3    2
# 4 이면 4~6    3
# 5 이면 7~10   4
# 6 이면 11~15  5
# x 이면        x-1

X = int(input())
#라인, 라인의 첫번째 수 정의
stage, key_X = 1, 1
# 라인의 첫번째 수 + 라인의 수가 입력값보다 작아질때 까지
while key_X + stage <= X:
    key_X += stage
    stage += 1
#step은 입력값 - 라인의 첫번째 값
step = X - key_X
#분모(x),분자(y)정의
x, y = step + 1, stage - step
# 스테이지가 홀수인 경우와 짝수인 경우.
if stage % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))
