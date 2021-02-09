# for i in range(1):
#     a,b,c = map(int,input().split())
#     if 100 <= a | b | c <=1000:   
#         x = a*b*c
#         print(x)
#         y = str(x)
#         for i in range(10):
#             print(y.count("i"))
#     else:
#         print("not properly access")
#         break

a= int(input())
b= int(input())
c= int(input())

x = a*b*c
# print(x)
y = str(x)

for i in range(10):
    print(y.count(str(i))) #for문 돌릴때 i는 int(숫자)형이다. 하지만 우리가
                           # 찾는것은 숫자의 개수이기 때문에 str으로 변형! 