n = int(input())
a = 3
b = 5 
for i in range(1,1000):
    for j in range(1,1000):
        if n//(3*i +5*j)==0:
            print(i+j)
            break
        else:
            print(-1)
            break

#만약 3x와 5y = 11이 되는 x,y가 있다면 x,y의 합을 출력
#없다면 -1을 출력.

inp = int(input())
Box = 0
while True:
    #5로 나눠지면 박스에 5kg를 담는다.
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    #그렇지 않다면, 총kg에서 3kg를 빼고(3kg를 한 개 담고) 박스 카운트를 센다.
    inp = inp-3
    Box += 1
    #나누어지지 않는다면 "-1"을 출력한다.
    if inp < 0:
        print("-1")
        break

# whats the problem?
# 문제를 쪼개서 알고리즘으로 생각하지 못했다.
