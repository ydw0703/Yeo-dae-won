# a=int(input())
# l=[]
# count=0
# for i in range(a):
#     b=input()
#     for j in b:
#         if b[j]==b[j+1]:
#             count+=

# 만약 전에 나왔던 단어가 또 나오면 카운트를 하지 않는다.

# a=int(input())
# count=0
# for i in range(a):
#     word=input()
    # count+= list(word) == sorted(word,key=word.find)
#     print(cnt)


# 인터넷 코드2
result = int(input())
for _ in range(result):
    word = input()
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]): #만약, word의 i-1번째 원소 > word의 i번째 원소이면,
            result -= 1 
            break
print(result)

# 단어에서 두 글자씩을 비교하여 앞 글자가 처음 등장하는 인덱스보다
# 뒷 글자가 처음 등장하는 인덱스가 더 작으면, 뒷 글자는 앞서 이미 등장한 글자가 됩니다.
# 따라서 그룹 단어가 아니므로, 결과에서 1을 제외하고 다음 단어를 검사합니다.
            