x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

if x2==x3 and y1==y3: 
    print(x1,y2)
elif x2==x3 and y1==y2:
    print(x1,y3)
elif x1==x3 and y2==y3:
    print(x2,y1)
elif x1==x3 and y1==y2:
    print(x2,y3)
elif x1==x2 and y2==y3:
    print(x3,y1)
elif x1==x2 and y1==y3:
    print(x3,y2)
