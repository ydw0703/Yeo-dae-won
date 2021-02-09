#내 코드
# index = 1
# while index < 11:
#     a, b = map(int, input().split())
#     print(a+b)
#     index +=1

# True일 때까지 a,b를 입력받아서 print(a+b)하여라. a,b==0이면 멈추어라.

#인터넷 코드
while True:
    try:
        a, b = map(int, input().split())
        0<a and b<10

        print(a+b)
    except:
        break

# try - exception - else - finally, 개념 예외처리 참조

