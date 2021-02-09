# a=map(int,input().split())
# a = list(a)
# # print(a)
# for i in range(2100000000):
#     if a[2]*i > a[0]+a[1]*i:
#         print(i)
#         break
#     else:
#         print(-1)
#         break
# C*x > A+B*x => 손익분기점

# iterable 객체 - 반복 가능한 객체
# 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
# int는 안되넹!, Why? -> 숫자는 계속 써도 1개이기 때문에 자체로는 반복될 수 없다.

f_cost,v_cost,price = map(int, input().split())

num_sales = 0

if v_cost < price:
    num_sales = f_cost // (price - v_cost)   
    print (num_sales+1)
    
else:
    print(-1)