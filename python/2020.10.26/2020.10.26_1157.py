# a=input()
# b=[]
# for i in a:
#     a1 = a.count(i)
    
#     b.append(a1)
#     b.sort()
#     print(b)
    # if a[i] s
    
# Internet Code
# n=input().upper() #문자를 입력받아 대문자로 변환
# t=[]
# for i in set(n): #중복없는 스펠링의 수만큼 반복해라
#     t.append(n.count(i)) #리스트에 입력받은 문자의 스펠 개수를 세라
#     print(t)
# idx=[i for i, x in enumerate(t) if x==max(t)] #x는 max(t)인 경우에만 enumerate(t)에 x를, i를 넣는다.
# if len(idx)>1:
#     print("?")
# else:
#     print(list(set(n))[t.index(max(t))])
# enumerate 몇번째 반복문인지 알고싶을 때, 인덱스 번호와 컬렉션의 원소를 tuple형태로 변환해줌

#set 특징
# 순서없음, 인덱싱 불가, {}형,
# print(set('abc')) => {'a','c','b'}
# print(set([4,5,1])) => {1,4,5}
# set으로 인덱싱을 하고 싶어? 그렇다면
# list(set(a))[0]
# tuple(set(a))[1] 처럼 하면 돼.
# set함수는 집합끼리 집합논리(& | - )가능

# 인터넷 코드2
# words = input().lower()
# words_list = list(set(words)) 
# print(words_list) #['g', 'a', 's', 'f', 'd']
# word_count = [] #list() 둘다 같은 뜻.


# for i in words_list:
#     count = words.count(i)
#     word_count.append(count)
#     print(word_count)

# if(word_count.count(max(word_count)) >= 2):
#     print('?')
# else:
#     print(words_list[(word_count.index(max(word_count)))].upper())
    
    
words = input().upper()
words_list = list(set(words))
word_count = []


for i in words_list:
    count = words.count(i)
    word_count.append((count, i)) # 개수와 문자를 같이 삽입
    print(word_count)
# word_count 정렬
word_count.sort(reverse=True)
print(len(word_count))

# 만약 가장 많이 사용된 알파벳이 여러개 라면 ? 출력
if len(word_count) >= 2 and word_count[0][0] == word_count[1][0]:
    print("?")
else:
    print(word_count[0][1])