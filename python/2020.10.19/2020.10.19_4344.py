# 내 코드 
c= int(input()) #case 수 입력받기

for i in range(c):
    a=list(map(int,input().split())) #학생 수, 점수 입력받기
    print(a)
    n=a[0] #학생 수 변수선언
    # print(n)
    avr = sum(a[1:])/n # 평균점수 변수선언
    # print(avr)
    count = 0
    for j in a[1:]:
        if j > avr: #평균을 넘는사람 비율 구하기 조건문
            count+=1
    print(str("%0.3f" % round(count / a[0] * 100, 3)) + '%') #비율이므로 갯수/갯수를 나눠줘야지!, '%0.3f' % var 소수 셋째자리까지 나타내라. round는 소수 n+1자리에서 반올림해라.    

#round(var,자릿수)반올림 함수

# 인터넷 코드
# for i in range(int(input())):
#     list_input = list(map(int, input().split(' ')))
#     ave = sum(list_input[1:]) / list_input[0]
#     count = 0
#     for j in list_input[1:]:
#         if j > ave:
#             count += 1
#     print(str(round(count / list_input[0] * 100, 3)) + '%')
