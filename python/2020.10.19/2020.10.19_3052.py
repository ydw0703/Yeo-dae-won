b=[]
for i in range(10):
    a= int(input())
    0<=a<=1000
    # c= b.append(a%42) #변수선언을 하는순간 type이 초기화된다.
    # print(c)          #그러면 c는 Nonetype으로 출력됨. 
    b.append(a%42)

b=set(b)
# print(b)
print(len(b)) #변수.함수() , 함수(변수)