s1 = int(input("enter the side: "))                
s2 = int(input("enter the side: "))
s3 = int(input("enter the side: "))
if s1 ==s2==s3:
    print("it is an equilateral triangle")
elif(s1==s2 or s2==s3 or s1==s3):
    print("it is an isosceles triangle")
else:
    print("it is a scalene triangle")