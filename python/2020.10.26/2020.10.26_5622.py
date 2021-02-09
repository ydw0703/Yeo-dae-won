# 1 " "
# 2 ABC 
# 3 DEF
# 4 GHI
# 5 JKL
# 6 MNO
# 7 PQRS
# 8 TUV
# 9 WXYZ
# 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3 #변수.index(i) -> 변수 리스트, 딕셔너리 등 에서 i의 위치값 반환.

print(ret)


# a= [ord("A")ord("C")]


# a = chr(65),chr(66),chr(67)
# a = 2
# print(a)

#chr(54) = 숫자 -> 해당 아스키코드 문자
#ord(a) = 문자 -> 해당 아스키코드 숫자