# n=int(input())
# a=[]
# for i in range(n):
#     if i==0:
#         a.append('666')
#     else:
#         a.append(str(i)+'666')
# print(a)
# print(a[n-1])

n = int(input())

name = 666
cnt=0
while(True):
    #만약 '666'이 name에 있다면 실행한다.
    if "666" in str(name) : 
        cnt+=1
        print(cnt)
        #cnt는 666이 들어갈 때 한번씩 카운트 된다.
        if cnt == n :
            print(name)
            break
    #if문과 상관없이 계속 증가한다. break를 if문 안에 걸어줌으로써 조건 충족을 하면 While loop를 빠져나온다.
    name+=1