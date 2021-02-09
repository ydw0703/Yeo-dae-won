# a,b,v=map(int,input().split())
# h=a-b
# count=1
# while True:
#     count += 1
#     if a*count - b(count-1) >= v:
#         break
# print(count)
# 시간초과가 될 확률이 높다. (코딩이 길어진다)

a,b,v = map(int,input().split())
k = (v-b)/(a-b)

print(int(k) if k == int(k) else int(k)+1)	#삼항연산자