n, m = map(int, input().split())
l = []
mini = []

# x*x판을 만들어 놓기.
for _ in range(n):
    l.append(input())

# 본 Loop
for a in range(n - 7):
    for i in range(m - 7): # 8*8이라면 1번씩만 돌고, 9*9라면 2*2=4번 도는 식.
        idx1 = 0 # 바꿔야 할 체스판 색의 개수를 수치화
        idx2 = 0 # 바꿔야 할 체스판 색의 개수를 수치화
        for b in range(a, a + 8):
            for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0: # 홀수행의 홀수열/짝수행의 짝수열인 경우.
                    if l[b][j] != 'W': idx1 += 1   
                    if l[b][j] != 'B': idx2 += 1
                else : # 홀수행의 짝수열, 짝수행의 홀수열인 경우.
                    if l[b][j] != 'B': idx1 += 1 
                    if l[b][j] != 'W': idx2 += 1
        mini.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        mini.append(idx2) 
print(min(mini))