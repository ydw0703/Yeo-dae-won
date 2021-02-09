# 부녀회장이 될테야?
# test_case = int(input())
# for i in range(1, test_case+1):
#     k=int(input())
#     n=int(input())
#     ppl=0
#     if k==0:
#         ppl+=1
#     elif n==1:
#         ppl=1
#     else:
#         for j in range(1,n+1):
#             for h in range(k):
#                 ppl = h + j

#안녕님 코드

t=int(input())
array = [[0]*14 for _ in range(15)] # 2차원 배열을 array를 초기화한다.
# 원소 [0]짜리 14개의 일차원 배열에 대해 15번 반복을 하니 14x15의 2차원배열이 생성된다.
print(array)
for i in range(14): # 0층을 만든다.
    array[0][i]=i+1 

for k in range(1,15): # 1층부터 14층까지 인원수에 대해 2차원배열에 값을 만든다.
    for j in range(14):
        array[k][j] = sum(array[k-1][:j+1])

for _ in range(t): # 테스트케이스를 array 배열에 대입한다.
    k=int(input())
    j=int(input())
    print(array[k][j-1]) 

# 지역변수는 같은 문자로 여러번 사용할 수 있다. 
