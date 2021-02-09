
###############################PYTHON개념###############################
########################################################################
########################################################################

#  python 은 interpreter 언어(최적화되지않아도 좋으니 프로그램이 그때그때 쉽고빠르게 실행될 수 있도록 만들어놓은) <-> compile 언어(프로그래밍을 최적화 시키고 한 번에 실행시키는 언어)
# introduce your pet


# station = "인천공항"

# print(station, "행 열차가 들어오/n고 있습니다.")

################################## 자료형 ###################################
# print("hello world")

################################### 정수형 ##################################
# print(4)

################################# boolean형 ##################################
#3print(10>38)

################################### 연산자 ###################################
# print(1 !=3) # boolean (1은3과 같지 않다.)
# print(3+4 ==7) # boolean (True == 비교연산자)
# x = 2       # = 대입연산자        
# y = 3
# print(x+y) 

# 간단한 수식
# number = 16
# number += 2
# print(number) #18
# number /= 2
# print(number) #9
# number -=2
# print(number) #7
# number %=2 #2로 나눈 나머지
# number//2 #2로 나눈 몫
# number/2 # 2로 나눔
# print(number)

# print(pow(4, 2)) #4의 제곱
# print(max(5, 12, 66)) #배열에서의 최댓값

# from math import *
# print(sqrt(11))

# from random import *
# print(random()) # 0.0~1.0 사이의 임의의 값 생성.
# print(random()*10)
# print(random()*10)
# print(int(random()*10)) # int형으로 감싸줌으로써 정수로 변환
# print(int(random()*10)) # int형으로 감싸줌으로써 정수로 변환
# print(int(random()*10)) # int형으로 감싸줌으로써 정수로 변환
# print(int(random()*10)) # int형으로 감싸줌으로써 정수로 변환
# print(int(random()*10)) # int형으로 감싸줌으로써 정수로 변환
# print(int(random()*10)) # int형으로 감싸줌으로써 정수로 변환

# print(list(range(1,10,2))) #숫자 범위 나타내기!!

# 위 식을 간략하게 할 수 있다!
# print(randint(1,45))
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월", date, " 일로 선정되었습니다.") 
# print( 
# """
# 나는 레오나르도 디카프리오
# """)  # 위 아래 빈칸 중앙에 내용 출력

############################# Slicing #####################################

# jumin = "990120-1234567"

#print("sex :", jumin[7]) #슬라이싱은 []안에 문자의 순서로 구분한다.
#print("birthday :", jumin[:6])
#print("뒤 7자리(뒤에부터)", jumin[-7:])

# python = "python is amazing"
#target = 'a'
#index = -1
#while True:
#    index = python.find(target, index + 1)
#    if index == -1:
#        break
#    print('a = %d' % index)
# print(python.upper())
# print(python[0].isupper()) #boolean - 0번째 값이 대문자 입니까?
# print(len(python))
# print(python.replace("python", "God"))  
# print(python.index("i"))
# index = python.index("i")
# print(index)
# index = python.index("i")
# print(index)
# print(python.index("Java")) 찾고자 하는 문장이 없을 땐 에러가 뜸.
# print(python.find("Java")) #찾고자 하는 문장이 없을 땐 -1을 출력함.

# print(python.count("n")) #찾고자 하는 문자의 위치가 아닌 갯수 검색.
# print(python.find("i", 0, 17)) #찾고자 하는 문자의 위치 검색.

# %d 정수형, %s 문자형, %c 한 글자만
# \n : 줄바꿈
# \000 : 널문자
# \" : "
# \a : 벨소리
# \v : 수직탭
# print("백문이 불여일견 \n백문이 불여일타")
# print("저는 \"나도코딩\"입니다.") 
# \\ : \ 
# \r: 커서를 맨 앞으로 이동 
# \b : 백스페이스 
# \t : 탭
# my_str = my_str[:my_str.index(".")] 은 my_str에서 "." 전까지의 문자만 추출한다.

# 12389845에서 3까지만 출력하시오.
#a = 12389845
#print(str(a)[:str(a).index("3")])

#############################################################################3
################## list (순서 가지는 객체의 집합) ###############################3
#############################################################################3
# 리스트끼리 사칙연산 가능
# 리스트는 인덱싱, 슬라이싱 가능

# 리스트 정렬
# num_list = [5,2,3,4,1,'a']
# num_list.sort()                   #리스트 요소 정렬

# num_list.reverse()                #리스트 요소 역정렬

# num_list.clear()                  #리스트 모든 요소 제거

# num_list.remove(리스트 요소값)     #리스트 선택 요소 제거
# num_list[0:2] = []
# num_list[2] = []는 [5,2,[],4,1]로 출력. 따라서 del my_list[2]

# mix_list = ["choi", 20, True]     #다양한 자료형 함께 사용 가능

# my_list[2:4] = 'goodbye'          # 리스트 수정

# my_list[2]                        #1차원배열 리스트 인덱싱

# my_list[2][0]                     #2차원배열 리스트 인덱싱

# my_list[::3], my_lsit[::-2]       #리스트 슬라이싱

#리스트의 메서드
# num_list.extend(mix_list)         #다른 리스트에 추가 확장

# num_list.insert(2,'a')            #2번 위치에 'a'를 삽입

# num_list.pop(삭제할 요소 인덱스 값) # default = -1; 맨 마지막 요소를 삭제하고 그 값을 리턴.

########## Practice ############
# subway = [10, 20, 30] #form
# print(subway)
# subway = ["Leo", "Joe", "Helen"]
# print(subway)
# subway.append("Keven") #맨 뒤에 추가

# subway.insert(1, "Jeong") # insert in it where you want to insert
# print(subway)

# print(subway.pop()) # pop it from the behind in turn
# print(subway)

#############################################################################3
################################## Dictionary ###############################3
#############################################################################3
# {}
# key는 immutable한 객체만 사용가능, value는 mutable한 객체도 사용가능.
# (immutable: 변하기 쉬운)
# key중복시 마지막 값으로 선언
# 순서 없음; 인덱스로 접근불가, 키로 접근 가능.

#cabinet = {3:"You", 2:"Cho"}
# print(cabinet)
#print(cabinet[3])
#print(cabinet[5]) #오류가 나고 프로그램이 종료
# print(cabinet.get(5,"Usable")) #오류가 나고 프로그램을 계속 이어나감.
#print(3 in cabinet) # The result is "True"
#print(5 in cabinet) #The result is "False"

#딕셔너리 선언
# 1. e={}; e{'a':5,'b':100} # >>> {'a':5,'b':100} 
# 2. f=dict{}; f(alice=5,bro=10) # >>> {'alice':5,'bro':10} 

#딕셔너리 복사
# 얕은 복사
# 1. b=dict(a)
# 2. b=a.copy()
#    b['alice'].append(5)
# 깊은 복사
# import copy
# b = copy.deepcopy(a)

#여러 값 수정
# a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
# >>> a.update({'bob':99, 'tony':99, 'kim': 30})
# >>> a
# {'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}

#cabinet = {"A-3":"You","B-100":"Cho"}
# print(cabinet["A-3"]) # value indexing(값 찾기)
# print(cabinet["B-100"])
#cabinet["A-3"] = ["b-4"]
# new customer
#cabinet["A-3"] = "sex" #최신 값으로 바뀜
#cabinet["C-20"] = "Ang" #새로 추가함.
#print(cabinet)

# If the customer is Gone, 
# del cabinet["A-3"] # delete the key
# print(cabinet)

# print(cabinet.keys()) #only print dictionary's key
# print(cabinet.values()) #only print dictionart's values
# print(cabinet.items()) #print dictionary's keys and values
# print(cabinet.clear()) #clearing all of dictionary's information

# for문 돌리면 기본적으로 key값이 추출됨
# value값 추출
# for i in a.values():
#    print(i)
# # key,value값 추출
# for i in a.items():
#     print('key={key},value={value}',format(key=key,value=value))

# in of dictionary #dictionary는 키에 한해서 boolean으로 출력

#####################################################################
############################### tuple(튜플) ##########################
#####################################################################
# iterable하다
# 선언
    # t1=()
    # t2=(1,) #요소가 한 개 일때 쉼표를 붙여야 함. 쉼표가 없다면 tuple형이 아닌 int형이 됨.
    # t3=(1,2,3)
    # t4=1,2,3
    # t5=('a','b',('ab','bc'))
# print(t3+t5) #tuple끼리 연산가능.
# 튜플 요소 값을 변경할 수는 없다.
# menu = ("hamburger", "coke")
# print(menu[0]) >>> hamburger

# menu.add("potato") # 불가

# (name, age, hobby)= ("Kim", 20, "Kang")
# print(name, age, hobby)

# a='감자'
# b='고구마'
# a,b=b,a
# print(a) # >>>고구마
# print(b) # >>>감자

# print('a' in ('a','b','c')) # >>>True
# print(5 in (5,'a','b')) # >>>False

#######################################################################
################################# 집합 Set(세트) #######################
#######################################################################
# 수학의 집합과 비슷한 개념
# 중복 안됨, 순서 없음, 인덱스로 접근 불가.
# {}로 감싼다.
# 세트의 원소는 immutable한 값들. # (mutable(변경 가능한; 리스트, 딕셔너리 등)값들은 쓸 수 없다.)
# set()함수를 사용하여 iterable한 객체를 넣으면 변환하여 set형태로 출력한다.

s=set([1,3,4,5,6])
print(s) # >>>{1,3,4,5,6}
#set로 for loop를 돌리면 set의 요소 순서대로 출력되지 않는다.


# my_set = {1,3,2,3,3,4,5,7,8,8,3,3}
# print(my_set) #중복 없음.

# 형식
# java = {"you", "Jeong", "Yang"}
# python = set(["you", "Mo", "Chi"])

# 교집합
# print(java & python)
# print(java.intersection(python)) 

# 합집합
# print(java | python)
# print(java.union(python))

# 차집합
# print(java - python)
# print(java.difference(python))

# 대칭차집합 (합집합 - 교집합)
# print(java ^ python)
# print(java.symmetric_difference(python))

# Boolean형 결과
# a.issubset(b) a는b의 부분집합인가?
# a.issuperset(b) a는b의 전체집합인가?
# a.isdisjoint(b) a와b의 교집합이 있는가?

# 원소 추가
# python.add("Chang")
# print(python)
# 여러개 원소 추가
# python.update('a','b') #여러개의 원소 추가 시, int형은 iterable하지 않으므로 list로 감싸 주어야 한다.[]
# print(python)

# 원소 삭제
# java.remove("Yang") #요소가 없을 시 Error발생
# print(java)
# java.discard(3) #요소가 없어도 Error 발생하지 않음.

# 원소 복사(얕은 복사; 저장되어 있는 주소값id()는 다름.)
# s={1,3,5} or s=set([1,3,5])
# t=s.copy()
# id(s) != id(t)

#########################################################################
############################## 자료구조의 변경 ###########################
#########################################################################
# char, int형은 변수 1개만 담을 수 있는 형태의 1차원 형태 / list, tuple, dictionary등은 변수를 1개 이상 담을 수 있는 2차원 형태(내장함수도 적용 가능) 
# unit = {1:"coffee", 2:"juice", 3:"milk"}
# print(unit, type(unit)) # {}로 출력

# unit = list(unit)
# print(unit, type(unit)) # []로 출력

# unit = tuple(unit)
# print(unit, type(unit)) # ()로 출력

# unit = set(unit)
# print(unit, type(unit)) # {}로 출력

# from random import *
# users = range(1, 21)
# print(set(users), type(users)) #list로 type을 바꾸어 주어야 함. 안 그러면 출력이 안 나옴.
# list(users) -> users의 범위만큼 요소가 만들어짐 #>>> [1,2,3,...,20]
# [users] -> users로 인스턴스화된 값 자체가 요소로 만들어짐 #>>> [range(1,21)]

# users = list(users)
# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) # users안에서 4개의 값을 랜덤 샘플링하여 인덱싱 하라.
# print(winners) #>>> [[0],[1],[2],[3]]; sampel function의 특징

# print("당첨자 발표")
# print("치킨 : {0}".format(winners[0]))
# print("커피 : {0}".format(winners[1:]))
# print("축하합니다.")

##################################### if ##################################
# temp = int(input("how about today's weather?"))
# if 30 <= temp:
#    print("Too hot. Just stay at home.")
# elif 10<= temp < 30:
#    print("Let's go outside!")
# else:
#    print("Stay at home.")

################################# for ###################################
#To get rid of meanless repeating!

#for waiting_no in [0,1,2,3,4]:
#    print("Waiting numbers : {0}".format(waiting_no))

#starbucks = ["iron man", "Torr", "Captine", "Marble"]
#a = starbucks
#for customer in a:
#    print("{0}, coffee is readied.".format(customer)) 

################################ while ####################################
# customer = "Torr"
# index = 5
# while index >= 1:
#     print("{0}, here is your coffee. it's remained {1}times".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("the coffee is discharged")

# customer = "iron man"
# index = 1
# while True:
#     print("{0}, here's your coffee. {1}".format(customer,index))
#     index +=1
#     customer = "iron mang"
#     if customer != "iron man":
#         print("bye")
#     else:
#         print("help yourself")
#     break
# 무한 루프를 끝내기 위해서는 "Ctrl + C" 사용

################################ continue,break ###########################
#  반목문 내에서 사용
# absent = [2,5]
# no_book = [7]
# for student in range(1,10):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("{0}, you die".format(student))
#         break
#     print("{0}, read it.".format(student))

# a=range(1,10)
# print(a)
# a=list(a)
# print(a)


#  즉 continue는 넘어가는 것이고, break는 다음단계부터 중단하는 것이다.

# Quiz4

# from random import *
# cnt = 0 #boarding customer number
# for i in range(1,51):
#      time = randrange(5,51)
#      if 5 <= time <= 15:
#          print("[O] {0}th customer. arrival time{1}".format(i,time))
#          cnt += 1
#      else:
#         print("[ ] {0}th customer. arrival time{1}".format(i,time))
# print("총 탑승 승객 : {0}".format(cnt))

############################# 함수(funtion) ###############################

# def open_account():
#     print("new account is opened.")

# def deposit(balance, money): #deposit
#     print(" input complete. {0}won.".format(balance+money))
#     return balance + money

# def withdraw(balance,money): #withdraw
#     if balance >= money:
#         print(" withdraw complete. {0}won.".format(balance-money))
#     else:
#         print("Invaild input. {0}won".format(balance))
#     return balance-money

# def withdraw_night(balance, money):
#     comission = 100
#     print("withdraw complete. {0}won. commission is {1}won".format(balance-money-comission, comission))

#     return comission, balance - money - comission

# balance = 0 # 1. define balance 2. change balance ~~
# balance = deposit(balance,1000)
# balance = withdraw(balance,500)
# #balance, commission = withdraw_night(balance,600)


############################# 함수 기본 값 ##################################
# def profile(name, age=17, main_lan="python"):
#     print("name : {0}\t age : {1}\t main_lan : {2}".format(name, age, main_lan))


# profile("유재석")
# profile("김태호")

############################## 키워드 값 ###################################

# def profile(name, age, main_lan):
#     print(name, age, main_lan)

# profile(main_lan="유재석",age="파이썬",name=20) #순서를 바꾸어 작성해도 순서를 다시 맞춤./순서를 매개변수 순으로 맞춤.

################################ 가변인자 ##################################

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#    print("name : {0} age : {1}".format(name,age), end = " " ) #end=" "는 줄 안 바꾸고 그대로 출력 가능
#    print(lang1, lang2, lang3, lang4, lang5)
# 원래 가변인자를 알기 전까지는 이런식으로 매개변수를 다 나열해야 했음.

# def profile(name, age, *language):
#     print("name : {0} age : {1}".format(name,age), end=" " )
#     for lang in language:
#         print(lang, end=" ")
#     print() #줄 바꿈
# 하지만 *language처럼 가변인자를 설정해 줌으로써 한 글자만 가지고도 for문으로 여러개의 매개변수를 설정할 수 있음.

# profile("유재석", 20, "python", "java", "C", "C+")
# profile("김태호", 25, "Kotlin", "Swift", "Assembly")

############################ 지역변수, 전역변수 ###############################
# 지역변수 : 함수 내에서만 쓰이는 함수.
# 전역변수 : 프로그램 어디서든 쓰일 수 있는 함수.

# gun = 10

# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun사용, 전역 변수 설정
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ref(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun # return - 지역 변수를 전역 변수로써 사용 가능하게 설정해줌
    
# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ref(gun, 2)
# print("전체 총 : {0}".format(gun))

# import numpy as np
# def std_weight(height,gender):
#     if gender == "남자":
#         return height*height*22
#     elif gender == "여자":
#         return height*height*21
#     else:
#         print("Are you crazy?")
#         return None

# height = 185
# gender = "남자"
# weight = round(std_weight(height/100,gender),2) #round(str, int) - 소수 int째 자리까지 반올림.
# print("키{0}cm 의 {1}의 표준체중은 {2}입니다.".format(height,gender,weight))


########################### 표준 입출력 ################################
# import sys
# print("Python", "Java", sep=" - ", end=" ") # sep - 구분, end=" " - 큰 따옴 표 안에 문자 + 줄 안바꿈.
# print("Coding need creativity")
# print("Python", "Java", file=sys.stdout) #표준 출력 형식
# print("Python", "Java", file=sys.stderr) #표준 에러 형식

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4), sep=":") # .ljust() - 왼쪽정렬, rjsut() - 오른쪽정렬

# # 은행 대기 순번표
# # 001, 002, 003, ..
# for num in range(1,21):
#     print("대기번호:" +str(num).zfill(3)) #zfill(int) - 0을 채운다(int)만큼

# answer = input("input any value : ") #input 함수는 출력이 오직 str이다.(숫자를 str으로 바꿔줄 필요가 없음.)
# print("입력하신 값은" + answer + "입니다.")

############################ 다양한 출력 포멧 ############################
# print("{0: >10}".format(5000)) #          5000
# print("{0: >+10}".format(5000)) #         +5000
# print("{0: >10}".format(-5000)) #         -5000
# print("{0:-<10}".format("안녕")) #안녕----------
# print("{0:,}".format(500000000)) # 500,000,000
# print("{0:+,}".format(500000000)) # +500,000,000
# print("{0:+,}".format(-500000000)) # -500,000,000
# print("{0:^<+30,.2f}".format(-500000000/3)) #+166,666,666.67^^^^^^^^^^^^^^^^ 
#     # 공간 채움, 정렬 기준,  부호, 공간 확보, 콤마, 소수점 순서
# print("{0:f}".format(5/3)) #1.666667
# print("{0:.2f}".format(5/3)) #1.67

############################### pickle ##################################

# pickle : 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장하는 것.
# import pickle
# profile_file =open("profile.pickle", "wb") #pickle을 쓰기 위해서는 항상 "b"(binary) 형태로 써야함.
# profile = {"name":"Park", "Age":"22", "Hobby":["Soccer", "Golf", "Coding"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


#########################################################################
################################## with #################################
#########################################################################

# with를 쓰면 더욱 편하게 파일을 만들고 열고 부를 수 있다.
# with open("study.txt", "w", encoding="utf8") as study_file: # "w" = write, encoding="utf8" = 한국어로 인코딩 하겠습니다.
#     study_file.write("study python hard. its hard to study") # 파일을 씁니다. 따옴표 안에 내용들로

# with open("study.txt", "r", encoding="utf8") as study_file: #study.txt 파일을 read 한다. 한국어로
#     print(study_file.read()) # 프린트 한다. "study_file"파일을. 읽는 형태로.


################################################################################
############################### class&__init__ #################################
################################################################################
# from random import * # random 은 module, numpy 같은것는 라이브러리. ㅡmodule과 library는 의미가 약간 다름.
# Module: 프로그램 내부를 기능별 단위로 분할한 부분
# library: 자주 사용되는 로직(모듈)을 재사용하기 편리하도록 잘 정리한 일련의 코드들의 집합

# class Unit:
#     def __init__(self, name, hp, damage): #__init__파이썬 생성자, 객체가 만들어질때 자동으로 호출되는 부분.
#                  인스턴스(self),인스턴스 변수(name),인스턴스 변수(hp),인스턴스 변수(damage)   # 어떤 클래스로부터 만들어지는 녀석들을 객체라고 한다. 인스턴스가 어떤 이름으로 정의될지 모르기 때문에 self라고 일단 정의하는 것.
#                                           # 객체들은 Unit class의 인스턴스 변수라고 부른다.
                                            # 객체 = 클래스로부터 만들어지는 것 = class안의 인스턴스 변수
                                            # 인스턴스 변수로 인스턴스 인자를 만든다.
#         self.name = name  #멤버 변수 self.name -> 인스턴스변수.name으로 됨
#         self.hp = hp      #멤버 변수
#         self.damage = damage #멤버 변수
#         print("{0} 유닛이 생성되었다.".format(self.name))
#         print("체력 {0} 공격력{1}".format(self.hp, self.damage))

# 마린 = Unit("마린",40,5) # 인스턴스 생성, class에서 만들어진 세 가지를 다 입력해주어야 함.(default값이 있으면 굳이 안써줘도 됨. ex) def __init__(self,name='홍길동',damage,hp)이면 name인자 설정을 안해줘도 디폴트값으로 ㅆㄱㄴ))
# 인스턴스(self->Marine) = Class name(인스턴스 변수/인자(name),인스턴스 변수/인자(hp),인스턴스 변수/인자(damage))


###################################################################################
#  Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

#[코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        #멤버 변수 생성
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


# 매물 정보 표시
    def show_detail(self):
        # show_detail의 self인자와 위 멤버변수를 결합.
        print(self.location, self.house_type, self.deal_type\
            , self.price, self.completion_year) # 위의

        

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

######################### 멤버 변수(클래스멤버 변수,인스턴스 멤버 변수) #############################
# class내에서 정의된 변수고 그 변수를 가지고 우리가 초기화 or 사용이 가능한 변수

# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# 파이썬에서는 어떤 객체에 추가로 어떠한 변수를 외부에서 만들어서 넣을 수 있다.

########################################################################
############################### 메소드 ##################################
########################################################################
# class내에 정의된 함수 = 메소드
# 메소드가 호출 된 오브젝트를 내재적으로 전달한다.
# 클래스 내에 포함 된 데이터에 대해 조작 할 수 있다.(객체(오브젝트) = 클래스의 인스턴스, 클래스는 정의)
# 메소드의 첫 번째 인자는 항상 self

# class 클래스명:
#     def 메서드(인자)

# class Tank(AttackUnit):
#     seize_developed = False #시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self,"탱크",150,1,35)
#         self.seize_mode = False

# #시즈모드 개발함수
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return    #Tank의 시즈모드 개발이 안됬으면 그냥 return하고.

# # 시즈모드가 개발됐다면 두 가지 경우가 있다.        
#          #현재 시즈모드 아닐때 ->시즈모드
#         if self.seize_mode == False:
#             print("{0}: 시즈모드로 전환합니다.".format(self.name))
#             self.damage*=2
#             self.seize_mode = True
#           #현재 시즈모드 일때 ->해제모드
#         else:
#             print("{0}: 시즈모드를 해제합니다.".format(self.name))
#             self.damage/=2
#             self.seize_mode = False

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,'레이스', 80, 20,5)
#         self.clocked = False #clocking mode(해체 상태)

#     def clocking(self):
#         if self.clocked == True: #clocking mode -> unclocked
#             print("{0} : set unclocked mode.".format(self.name))
#             self.clocked = False
#         else: # unclocked -> clocking mode
#             print("{0} : set clocking mode.".format(self.name)
#             self.clocked = True
            

# def game_start():
#     print("[알림]새로운 게임을 시작합니다.")

# def game_over():
#     print("[알림] Player님이 게임에서 퇴장하셨습니다.")
        
# 실제 게임
# game_start()

# 유닛 생성
# m1 = Marine() #인스턴스 생성
# m2 = Marine() #인스턴스 생성
# m3 = Marine() #인스턴스 생성

# t1=Tank() #인스턴스 생성
# t2=Tank() #인스턴스 생성

# w1=Wraith() #인스턴스 생성

# 유닛 일괄 관리
# attack_units = [] #새로운 리스트 생성(=부대지정)
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비(탱크 : 시즈모드, 마린 : 스팀팩, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine): # isinstance 특정 클래스의 인스턴스인지 확인 후 기능 진행가능.
#         unit.stimpack() #메서드 호출
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode() #메서드 호출
#     elif isinstance(unit, Wraith):
#         unit.clocking() #메서드 호출

# 전군 공격
# for unit in attack_units:
#     unit.attack('1시')

# 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음(5~20)

# 게임 종료
# game_over()


############################################# 예외처리 #######################################
# 어떤 에러가 발생했을때 그에 대한 처리를 해주는 과정.
#try문 안에 실행 결과에서 error가 뜨면 exception 함수에서 print를 한다.
# try:
#     print("For Dividing calculator")
#     nums=[]
#     nums.append(int(input(" Put in first number :")))
#     nums.append(int(input(" Put in second number :")))
#     nums.append(int(nums[0]/nums[1]))
#     print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))

# except ValueError: #에러명
#     print(" Error! You put the wrong values.")
# except ZeroDivisionError as err:
#     print(err)
# 그 외의 나머지 에러 처리를 하고 싶을 때
# except:
#     print("invalid Error occured")
#      print(err)
# except후 별도의 조작이 없다면 프로그램이 중단됨.

#  else:                # 에러가 없을 시 출력
#      print("no err") 

# finally:              # 에러의 여부 상관없이 출력
#     print("end")

# 오류 회피하기
# try:
#     print(5/0)
#     print(c)
# except NameError as e:
#     print(e)
# except ZeroDivisionError as e:
#     pass
# as a result of running, it is going to the next step without any task

# 오류 발생 시키기
# try:
#     age = int(input())
#     if age < 0:
#         raise NotImplementedError #오류 발생시키기
#     print(age)
# except NotImplementedError:
#     print('NotImplementedError')


#################################################################################################
############################# 사용자 정의 예외처리 & 에러 발생시키기 ###############################
#################################################################################################

# # 새로운 예외처리를 정의해준다.
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg=msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("For Dividing calculator")
#     # nums=[]
#     # nums.append(int(input(" Put in first number :")))
#     # nums.append(int(input(" Put in second number :")))
#     # nums.append(int(nums[0]/nums[1]))
#     num1 = int(input(" Put in the first number :"))
#     num2 = int(input(" Put in the second number :"))
#     # if 문에서 위에서 만든 예외처리에 조건을 걸어둔다.
#     if num1 >= 10 or num2 >= 10:
#         # raise는 에러를 직접 발생시킴.
#         raise BigNumberError("입력값 : {0},{1}".format(num1, num2))
#     print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError: #에러명
#     print(" Error! You put the wrong value.")
# except ZeroDivisionError as err:
#     print(err)
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# # 그 외의 나머지 에러 처리를 하고 싶을 때
# except:
#     print("invalid Error occured")
#     print(err)
# # try구문에 상관없이 무조건 실행되는 함수 finally
# finally:
#     print("Thank you for using calculator")

# 컴파일 = 코딩한 내용을 객체화 시키는 작업
# 링킹 = 객체들을 서로 연결 시키는 작업
# 디버깅 = '벌레를 없앤다는 뜻', 오류나 에러를 확인하는 작업
# 빌드 = 컴파일 - 링킹 - 디버깅 - 실행을 처리하는 과정

############################ 연습문제 #######################################
# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때 ValueError 로 처리
#     출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#     치킨 소진시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
#     출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
#############################################################################
############################## 메소드 오버라이딩 ##############################
#############################################################################
# 부모 클래스의 메소드를 자식 클래스에서 재정의 하는 것.

# class.mro() 상속 관계를 확인할 수 있는 메서드
# 출력 [<class 'library.class>,<class 'library.class'>,<class 'object'>]

# 세줄문자: 텍스트의 한 줄이 끝남을 표시하는 문자 또는 문자열
# (개행 문자, 줄바꿈 문자, EOL과 같은 뜻)

import seaborn as sns
sns.pairplot(data,diag_kind='kde' = 커널밀도추정곡선,
                diag_kind = 'hist' = 히스토그램
            hue='speices',
            palette = '색상')

import pandas as pd
pd.DataFrame(data) = 데이터 프레임으로 만들어줌
pd.describe() = 연산 가능한 숫자를 가진 컬럼을 추출 -> 기본통계량을 산출


what is Object Oriented Programming?(객체 지향 프로그래밍)
문제를 여러 개의 객체 단위로 나눠 작업하는 방식.

클래스를 이용해 함수(처리부분)와 변수(데이터 부분)를
하나로 묶어 객체(인스턴스)를 생성해 사용한다는 점이다.

    객체: 실제 존재하는 모든 사물 또는 개념
    클래스: 객체를 정의해 놓은 것
    인스턴스: 객체와 비슷. 클래스로부터 객체를 만드는 과정을 
            '클래스의 인스턴스화'라고 부름

            객체 - 핸드폰 
            클래스 - 핸드폰 설계도
            인스턴스화 - 핸드폰 설계도로부터 핸드폰을 만드는 과정

from scklearn import datasets
import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.25, random_state=321)
parameter
array: 분할시킬 데이터를 입력
test_size: 테스트 데이터셋의 비율이나 갯수
trian_size: 학습 데이터셋의 비율이나 갯수
random_state: 데이터 분할시 셔플이 이루어지는데 이를 위한 시드값
shuffle:셔플여부 설정

from sklearn.feature_selection import SelectKBest, f_classif

SelectKBest: k highest점수에 따라 특징을 선택한다.
parameter
score_func: callable
k: int or "all",optional, default=10

머신러닝 라이브러리
데이터 전처리, 세부조정, 모델 평가, 분류 알고리즘 등 간편한 API 제공
API가 잘 되어있음.



dic1.keys() = 키 추출
dic1.values() = 값 추출
dic1.items() = 키, 값 모두 추출

DataFrame 정렬 : DataFrame.sort_values()
Tuple 정렬 : sorted(tuple, key) method
List 정렬 : sorted(list), or list.sort()

from tqdm import tqdm_notebook
즉석에서 progress_bar를 생성해주고, 
함수나 반복문의 TTC(time To Completion)를 예측하는 파이썬 패키지

python_zip_funtion
같은 인덱스를 가진 두 리스트를 딕셔너리처럼 묶어주고 싶을 때 사용할 수 있다.

import numpy as np
np.nan = 결측치가 ' '와 같은 빈 공간일 때 pandas라이브러리가 인식할 수 없다.
        따라서 np.nan으로 결측치라는 의미를 인식할 수 있게 바꿔준다.

np.percentile(data,[25,75]) # data의 1분위 3분위 값.

# 1	StandardScaler	기본 스케일. 평균과 표준편차 사용
# 2	MinMaxScaler	최대/최소값이 각각 1, 0이 되도록 스케일링
# 3	MaxAbsScaler	최대절대값과 0이 각각 1, 0이 되도록 스케일링
# 4	RobustScaler	중앙값(median)과 IQR(interquartile range) 사용. 아웃라이어의 영향을 최소화

# 인스턴스란(객체의 일종?)
#   클래스 안의 구분지을 수 있는 변수들, 메소드 밖, 클래스 안에 선언된 변수.
# 메서드란
#   함수같은 개념, 함수는 함수지만 클래스 안에서 정의되어 클래스의 인스턴스에만 적용될 수 있는 함수를 메소드라고 부릅니다.
# 하이퍼 파라미터란
#   함수 안에 수동 설정 값.
# 파라미터란(=매개변수)
#   데이터로부터 나온 설정 값. def function(a,b): 에서 a,b같은..
           

a=10 #a -> 매개변수(Parameter): 메서드나 생성자에 넘겨주는 변수
     #10 -> 전달인자(Argument): 파라미터를 넘겨준 값.
b=11
sum(a,b)



class Singer:                      # 클래스(singer)를 정의하겠느니라…
        def sing(self):                # 노래하기 메서드(sing),매개변수(self)
                return "Lalala~"
    
taeji = Singer()                   # 태지(인스턴스변수)를 만들어랏!
taeji.sing()                       # 노래 한 곡 부탁해요~
'Lalala~'


from 모듈 import 함수 #때에 따라서 변한다. 모듈을 패키지라고 생각하면 from 패키지 import모듈이 되는 것.

# 바인딩이란
#   실제 데이터가 존재하는 위치를 가리키고 있는 것.

# 파이썬의 변수는 실제 데이터가 저장되는 공간자체가 아니라, 데이터가 메모리상에서 위치하는 주솟값이 저장되는 공간이다.

# 변수의 초기화란
#   변수 선언 후 그 변수에 처음으로 어떠한 값을 저장하는 것.


# 가상환경이란
#   자신이 원하는 Python환경 구축을 위해 필요한 모듈만 담아놓은 바구니
#   각 가상환경은 독립적으로 관리.
#   각 모듈은 다른 모듈에 대한 의존성이 다르다.(Tensorflow는 Python 64비트에서만 동작, 키움증권 opemapi는 32비트에서만 동작 등.)
#   각 프로젝트 별로 별개의 가상환경을 만들어놓고 사용하는 것을 추천.
#   아나콘다 가상환경 -> anaconda prompt에 가서 구축(32,64)
#   파이참에서의 연결은 구축한 가상환경이나 직접 설치한 파이썬 버전을 settings에서 연결 

# DLL file이란
#   Dynamic Link Library(동적 링크)
#   실행 파일에서 해당 라이브러리 사용 시에만, 라이브러리 파일을 참조하여 기능을 호출
#   함수의 위치정보만 갖고 그 함수를 호출할 수 있게 함.
#   장점
#       1) 더 적은 리소스 사용
#           한 코드를 여러 프로그램이 동시에 사용 -> 메모리 절약.
#           SLL과는 다르게 필요한 라이브러리만 사용 -> 디스크 공간 절약
#           운영 체제, 프로그램이 더 빠르게 로드,실행
#        2) 모듈식 아키텍쳐 활용
#            여러 언어 버전이 필요한 큰 프로그램이나 모듈식 아키텍처 프로그램 개발 가능.
#        3) 손쉬운 배포, 설치
#            DLL내 함수를 수정, 재배포시 프로그램을 DLL과 다시 연결하지 않아도 된다.
#        4) 프로그래머들의 분담 작업 용이, 재사용성이 뛰어남.
#            코드의 양이 적어지므로 디버깅도 용이해진다.
#       ex) 윈도우 시스템 라이브러리, 프로세스의 동적 속성 등의 많은 라이브러리를 묶어서 저장해놓은 파일!

# 오버로딩
#   같은 이름의 메서드에서 다른 파라미터를 사용하는 것.
#   장점
#       하나의 이름으로만 기억하면 됨. -> 효율성, 오류 가능성 적음
#       메서드의 이름을 절약할 수 있다.
#       같은 기능을 하겠구나?
# 오버라이딩
#   상위 클래스가 가지고 있는 메소드를 하위 클래스가 재정의 해서 사용 하는 것.
#   장점
#       같은이름으로 구현부를 변경하여 내용을 수정하여 프로그램 리소스(길이)를 줄여준다.

#배치파일이란?
    cmd에서 두 줄 이상의 명령은 실행하지 못한다.
    이것을 보완해줄 파일 = 배치파일
    
파이썬 라이브러리는 각 파이썬실행폴더 site-packages에 있는 pip폴더안에 들어있다구~
