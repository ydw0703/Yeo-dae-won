# 공백이 나오면 카운트를 한개 올리고 초기화하여 반복한다.
# 단어가 끝날때 까지 반복한다.

# a=input()
# count=0
    
# for i in a[1:len(a)-1]:
#     if i==" ": #for문으로 새 변수를 선언한 다음, if문으로 들어간다. 원래의 나는 while문에서 변수없이 if문을 만들어서 완전하지 못했다.
#         count+=1

#     else:
#         continue
# count=count+1
# print(count) 

#인터넷 코드...
n = input().split() #split함수는 공백을 기준으로 리스트에 원소를 저장합니다.
print(n)
print(len(n))

# 인터넷 코드2
# string = input("")
# words = string.split(" ")
# # 공백이 아닌 경우에만(if)/ words에 넣음(for) # 리스트 조건제시법
# words = [w for w in words if w != ""] 
# print(len(words)) 