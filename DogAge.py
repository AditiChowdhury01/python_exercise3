n = int(input("enter your dog's  age in human year:"))         
if n<0:
    exit()
elif(n<=2):
    d_age = 2 * 10.5
else:
    d_age = 21 +(n-2)*4
print(d_age)
