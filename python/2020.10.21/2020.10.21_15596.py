# #내 코드
# def solve(n): #함수선언(인자선언)
#     a = []
#     for i in range(n+1):
#         a.append(i)
#         a1 = sum(a)
#     return a1 함수 적용결과값 리턴

# n=int(input()) #인자값 설정
# print(solve(n)) #함수 사용


#인터넷 코드
# def solve(num_list):
#     result = 0
#     for num in num_list:
#         result += num
#     return result

# def solve(a):
#     ans = sum(a)
#     return ans



# 런타임 에러가 뜨는 상황
# 1. 배열에 할당된 크기를 넘어서 접근했을 때
# 2. 전역 배열의 크기가 메모리 제한을 초과할 때
# 3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
# 4. 0으로 나눌 떄
# 5. 라이브러리에서 예외를 발생시켰을 때
# 6. 재귀 호출이 너무 깊어질 때
# 7. 이미 해제된 메모리를 또 참조할 때  