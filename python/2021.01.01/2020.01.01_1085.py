x,y,w,h = map(int,input().split())
1<=x<=w-1
1<=y<=h-1

if x >= w//2 and y >= h//2:
    if w-x>=h-y:
        print(h-y)
    else:
        print(w-x)
elif x < w//2 and y >= h//2:
    if x >= h-y:
        print(h-y)
    else:
        print(x)
elif x < w//2 and y < h//2:
    if x >= y:
        print(y)
    else:
        print(x)
elif x >= w//2 and y < h//2:
    if w-x >= y:
        print(y)
    else:
        print(w-x)   

x, y, w, h = list(map(int, input().split()))
print(min([x, y, w - x, h - y]))       