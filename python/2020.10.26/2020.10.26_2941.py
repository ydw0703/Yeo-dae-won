
cro_spell = ["c=",'c-','dz=','d-','lj','nj','s=','z=']
a=input()
for i in cro_spell:
    a=a.replace(i,'*') # cro_spell에 있는 값을 찾아 *로 바꾼다.
                       # replace로 한 가지 문자로 대체후 길이를 바꾼다.

print(len(a))