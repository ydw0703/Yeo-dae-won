a = {1:'정재욱',2:'한동호',3:'공대환',4:'윤준식',5:'여대원',6:'김준현',7:'송인혁',8:'안희원',9:'옥영인'}
#정재욱 = 숙주
print('숙주님 참석 하시겠습니까?')
sj = input()   # 참석 or 불참
if sj=='참석':
    for i in a:
        if i==1:
            print("간보기 시작!")
            print(a[i],'님:',a[9],'하면 함~')
        else:
            if a[i]=='옥영인':
                oo=input('옥영인 님, 당신의 선택은?')
                print(oo)
                if oo=='응 안해':
                    for j in a:
                        print("나도 안해~") 
                continue
            print(a[i],'님:', a[i-1],'하면 함~') #i-1=0을 정의하는 a의 딕셔너리 원소가 없으므로 i=1일때는 따로 빼주었다.

# def numerical_diff(f,x):
#     h = 1e-4
#     return(f(x+h)-f(x-h))/(2*h)

# a=numerical_diff(5,2)
# print(a)