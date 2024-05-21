a = float(input("enter a number:"))               
b = float(input("enter a number:"))
c = float(input("enter a number:"))
if a>b:
    if a<c:
        median = a
    elif b>c:
        median = b
    else:
        median= c
else:
    if a<b:
        if b<c:
            median = b
        elif a>c:
            median = a
        else:
            median = c

print("the median is:" ,median)