#내 코드 
n = int(input())
a = list(map(int,input().split()))

print("{} {}".format(min(a),max(a)))
print(min(a), max(a))                 # Both of them are possible.


#인터넷 코드

numbers = int(input())
number_list = list(map(int, input().split()))

max_num = number_list[0]
min_num = number_list[0]
for num in number_list:
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)
# ...뭔소린지..
