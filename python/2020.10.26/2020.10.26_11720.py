a = int(input())
b=list(input())
b1=list(map(int,b)) # list문자열을 int형으로 변환해준다.
print(b1)
print(sum(b1)) #sum함수는 반복적으로 더해주는 것이 아니라 한 번에 다 더해준다.

#인터넷 코드
string_count = int(input())
string = list(input())

#반복문으로 리스트 더하기 기능
res = 0 #증가요소를 for문 밖에서 정의해 주어야 한다.
for i in range(string_count):
    res += int(string[i])
print(res)