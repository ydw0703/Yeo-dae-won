# a = input()
# for i in range(1,27):
    
#     if x in a:
#         print(a.find(a[i]))
#     else:
#         print(-1) 
    
# print()

# #아스키 코드 활용
# print(*map(input().find(chr,range(97,123))),sep=" ")

#인터넷 코드 1
S = input()
check = [-1]*26 #길이 26 리스트를 이렇게도 만들 수 있음!
 
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')
    
#인터넷 코드 2
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위
# # 아스키코드는 문자를 숫자화 시켜서 반복문이나 조건문에 넣을때 좋을듯.
# for x in alphabet :
#     print(word.find(chr(x))) 