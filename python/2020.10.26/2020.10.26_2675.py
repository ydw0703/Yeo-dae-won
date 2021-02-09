# s,a =map(int,input().split())
# a1=str(a)
# print(a1)
# # a0 = []
# for i in range(s):
#         b = a1[i]*s
#         print(b,end=' ')
        
#인터넷 코드
# t=int(input())

# for i in range(t):
#     r,s=input().split()
#     r=int(r)
#     s=str(s)
#     for i in range(len(s)): #문자의 길이번 반복하여, 문자의 원소를r번 출력한다.
#         print(r*s[i],end='') #s[i]에서 문자열은 리스트 형태가 아니더라도 [i]번째 원소로 나타낼 수 있다.
#     print()


t = int(input()) 
for i in range(t): # 입력번 돌림
    num, s = input().split() # num,s 변수를 선언하고, 입력값을 split형태로
    text = '' #text는 형식이 없는 빈 공간으로 정의된다. 
    for i in s:
        text += int(num) * i # 문자열도 +=추가 기능이 가능하다.
    print(text)