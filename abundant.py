n=int(input("Enter Any Number"))
sum=1
for i in range(2,n):
	if(n%i==0):
		sum=sum+i
if(sum>n):
	print(n,"Abundant Number")
else:
	print(n,"Not Abundant Number") 