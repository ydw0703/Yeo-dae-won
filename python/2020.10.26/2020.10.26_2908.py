# a= list(map(int,input().split())) 
#map객체로는 list안을 들여다 볼 수가 없다. 
#그러므로 list()로 map을 감싸주어야 한다.

# a,b=input().split()
# a1=list(reversed(a))
# b1=list(reversed(b))

# # for i in a:
# #     a[i-1]=a[len(a)-i]

# # for j in b:
# #     b[j-1]=b[len(b)-j]
# print(a1,b1)
# int(a1)
# print(a1)


a, b = input().split()

a = int(a[::-1]) #첨부터끝까지 요소를 -1만큼 증가해서씩 가져온다.
print(a)
b = int(b[::-1])
print(b)

if a > b :
    print(a)
else :
    print(b)