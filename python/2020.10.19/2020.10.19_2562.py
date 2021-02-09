
s = []
for i in range(1,10):
    a = int(input())
    s.append(a)

print(max(s))
print(s.index(max(s)))
#for문을 1부터 시작하므로 +1필요없음.

#인터넷 코드

num_list = []
for i in range(9):
   num_list.append(int(input()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)
#for문을 0부터 시작하므로 +1을 해준다.
#index: list에서 원소를 찾는 함수.