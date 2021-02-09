#덩치 문제

#인터넷 소스
t = int(input())
# making list 'a' 
a = []
for i in range(t):
    a.append(input().split()) # input value : height,weight
    print(a)
a_len = len(a)

seq = []
for i in range(a_len):
    cnt = 1
    print(i)
    for j in range(a_len):
        print(j)
        #이중 for문으로 한개씩 비교하면서 조건을 만족하면, count를 1씩 추가했다.
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            cnt += 1
    d=seq.append(cnt)
    print(d)
for i in seq:
    print(i, end='')


