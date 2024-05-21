
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")         
month = input("enter month's name:").lower()
if month=="february":
    print("no.of days are:29/29days")
elif month in ( "january","march","may","july","august","october","december"):
    print("no. of days : 31days")
elif month in ("april","june","september","november"):
    print("no. of days are : 30days")

else:
    print("wrong month entered")