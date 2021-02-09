# def draw_star(n):
#     global map

#     if n==3:
#         map[0][:3]=map[2][:3]=[1]*3
#         map[1][:3]=[1,0,1]
#         return
    
#     a=n//3
#     draw_star(n//3)
#     for i in range(3):
#         for j in range(3):
#             if i==1 and j==1:
#                 continue
#             for k in range(a):
#                 # n = 3^i 일때는 가운데를 비워두고 "별"이 찍힌 것처럼 n = 3^i 일때는 가운데를 비워두고 "n = 3^(i-1) 일때의 별 배열"이 찍힙니다.
#                 map[a*i+k][a*j:a(j+1)]=map[k][:a]

# N=int(input())

# map=[[0 for i in range(N)] for i in range(N)]

# draw_star(N)

# for i in map:
#     for j in i:
#         if j:
#             print('*',end='')
#         else: 
#             print(' ',end='')
#     print()

def stars(n):
    matrix=[]
    for i in range(3*len(n)):
        if i//len(n)==1: #몫이 1이면
            matrix.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
        else: #그 외에는
            matrix.append(n[i%len(n)]*3)
    return(list(matrix))

star=['***','* *','***']
n=int(input())
k=0
while n!=3:
    n=int(n//3)
    k+=1
    print(k)

#star list를 함수에 집어넣어서 새로운 star를 만드는 for loop
for i in range(k):
    star = stars(star)
    print(star)
#새로운 star로 i를 찍어내는 for loop
for i in star:
    print(i)

if a is