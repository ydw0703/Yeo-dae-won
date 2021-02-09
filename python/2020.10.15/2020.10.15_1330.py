h, m = map(int,input().split())

if 1<=h<=23 and 45<=m<=59:
    m = m-45
    print(h,m,sep=" ")
elif 1<=h<=23 and 0<=m<=44:
    h -= 1
    m = m-45+60
    print(h,m,sep=" ")
elif  h==0 and 45<=m<=59:
    m = m-45
    print(h,m,sep=" ")
elif h==0 and 0<=m<=44:
    h = h-1+24
    m = m-45+60
    print(h,m,sep=" ")

# 조건에 맞춰서 if문 안에서 변수를 재정의 하고 print를 돌리는 것이 좋다.
# 바로 print문 안에서 변수를 계산하려면 머리가 아픔.