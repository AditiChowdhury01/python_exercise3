print("enter a number or press 0 to exit")                      
count = 0
sum = 0
number =1
while number!=0:
    number = int(input("enter number"))
    sum =sum +number
    count = count+1
#if count==0:
 #   print("enter some number")
else:
    print("the average and sum of the numbers are:",sum/(count-1),sum)