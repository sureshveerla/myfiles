n=int(input("Enter Any Number"))
m=n
sum=0
while(n>0):
	sum+=n%10
	n=n//10
if(m%sum==0):
	print("Harshad Number")
else:
	print("not Harshad Number")