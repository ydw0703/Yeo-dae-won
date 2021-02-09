#selfNumber 만드는 함수 생성
def selfnumber(n): #함수명 선언(변수설정)
    a=0
    for x in list(str(n)): #for문 범위를 리스트로 만들었다. #list(str(10))=['1','0'] -list화 할때는 무조건 str으로 넣는다. , [int/str] = [int/'str']
        a=a+int(x)         
    return int(n) + a  #셀프넘버 결과값

a=[]
for i in range(10001):
    k=selfnumber(i)
    a.append(k)

for b in range(1,10001):
    if b in a: #b가 a리스트 안에 있으면
        pass
    else:
        print(b)