# n=input()
# m=0
# for i in range(len(n)):
#     m+=1
# for i in range(len(n)):
#     m=str(m)
#     m=int(m)+int(m[i])
#     if m==int(n):
#         print(a)
#         break

N = int(input())
print_num = 0 #결국에 출력할 값(M)을 초기화를 해서 에러가 나지 않게 만들었따.
for i in range(1, N+1):
    # str(i)를 int(i)로 변형한 list를 만든다.
    div_num = list(map(int, str(i)))
    print(div_num)

    sum_num = i + sum(div_num)
    print(sum_num)
    if(sum_num == N):
        print_num = i
        break
print(print_num)
if sum_num != N:
    print('Eii!')
