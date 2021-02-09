t=int(input()) #테스트 데이터 입력
# 호텔에 방에 채워지는 것은 층>층당번호수
# n의 입력값은 배열 h,w에 자리에서 찾을 수 있다.

for i in range(t):
    # 호텔 층수, 층당 방수, 몇 번째 손님 입력
    h,w,n=map(int,input().split())
    hotel=[]
    for j in range(1,w+1):
        for k in range(1,h+1): 
            hotel.append((j,k))
            # print(hotel)
    n1=hotel[n-1]
    if 1<= n1[0] <=9:
        print(str(n1[1])+"0"+str(n1[0]))
    else:
        print(str(n1[1])+str(n1[0]))