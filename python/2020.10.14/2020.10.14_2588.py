a=int(input())
b=input()

a1 = a*int(b[2])
a2 = a*int(b[1])
a3 = a*int(b[0])
a4 = a*int(b)
print(a1,a2,a3,a4, sep="\n")

# 곱셈연산에서 위의 숫자와 밑의 한 자리씩 곱하여 최종적으로 더하는
# 연산방법이므로 a는 숫자형, b는 문자형으로 입력을 받아 곱셈 연산을
# 할 때에는 b를 숫자형으로 바꿔주기만 하면 된다.