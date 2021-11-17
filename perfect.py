n=int(input("Enter Any Number = "))
sum=0
for i in range(1,n):
	if(n%i==0):
		sum=sum+i
if(sum==n):
	print("Given Number is Perfect Number ")
else:
	print("Given Number is Not-Perfect Number ")