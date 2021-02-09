def prime_list(n):
    sieve=[True]*n   #n개의 True리스트 작성( 소수로 간주 )
    for i in range(2, int(n**0.5)+1):  #n개의 제곱근만큼만 검사해도 충분
        if sieve[i]:  #sieve리스트 내에 있는 것들중  
            for j in range(i+i,n,i):  #i의 배수씩 소수가 아닌수를 False로 치환
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i] ==True]

while True:
    n = int(input())  #수를 받아서
    if n == 0:  #그 수가 0이면 break
        break
    li=prime_list(2*n+1)  #위의 함수에 받은 수를 대입해서 소수를 구함.
    print(len([i for i in li if i>n]))  #만약 받은 수보다 큰 목록이 li에 있다면 리스트에 넣고 소수의 개수를 구한다.
    