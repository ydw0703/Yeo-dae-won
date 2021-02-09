# # N,M = map(int,input().split())
# # a,b,c,d,e = map(int,input().split())
# # w=[a,b,c,d,e]
# # w.reverse()
# # print(w)
# # t=0
# # for i in w:
    
# #     if t>M:
# #         continue
# #     elif
# #     t = i+t
# #     print(t)


    


# N, M = map(int, input().split())
# v = list(map(int,input().split()))
# s=list()
# #리스트 길이만큼 반복한다.
# for i in range(len(v)):
#     #리스트 길이에서 1만큼 덜 반복한다.(한 가지를 골랐으니 4개의 경우가 남음)
#     for j in range(i+1,len(v)):
#         #리스트 길이에서 2만큼 덜 반복한다.(두 가지를 골았으니 3개의 경우가 남음)
#         for z in range(j+1,len(v)):
#             #s리스트에 3개의 고른수를 집어넣는다.
        
#             print(s.append(sum([v[i],v[j],v[z]])))         
               
            
# s=[i for i in s if i<=M]
# if len(s)>0:
#     print(max(s))