n=int(input("Enter any number = "))
a=0
count=0
a=n//2
for i in range(2,a+1):
	if(n%i == 0):
		print("Given number is not a Prime")
		count = 1
		break
if(count==0):
		print("Given number is Prime")