

# 인터넷 코드
n = num = int(input())
count = 0
while True:
    ten = n // 10
    one = n % 10
    total = ten + one
    
    n = int(str(n % 10) + str(total % 10))
    count += 1
    print(n)
    if num == n:
        break
print(count)


