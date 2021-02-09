def hansoo(num):
    hansu=0 #카운팅 , for문 안으로 넣으면 반복문을 돌때마다 0으로 초기화 된다.
    for i in range(1,num+1):
        if i<=99:
            hansu += 1 #99까지는 등차수열의 관계가 없으므로 모두 포함.
        else:
            nums = list(str(i))
            if int(nums[0]) - int(nums[1]) == int(nums[1]) - int(nums[2]) :
                hansu += 1 #세 자리 부터는 각 자리의 수의 차가 등차수열이면 한수
    
    return hansu #한수 개수 결과값
num=int(input())#숫자입력
print(hansoo(num))

#인터넷 코드
# def Han(n):
#         cnt = 0
#         if (n < 100):
#                 return n
#         else:
#                 for i in range(100,(n+1)):
#                         hund = (i//100)
#                         ten = ((i%100)//10)
#                         one = ((i%100)%10)
 
#                         if ((hund - ten) == (ten - one)):
#                                 cnt += 1
#                 return (99+cnt)
 
# inp = int(input())
# res = Han(inp)
# print(res)