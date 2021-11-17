year=int(input("Enter Year"))
if(year%4==0 or year%100==0 or year%400==0):
	print("year is leap year",year)
else:
	print("year is non-leap year",year)