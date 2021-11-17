#sun of digits of Given number
n=int(input("Enter Any Number"))
sum=0
while(n!=0):
	r=n%10
	sum=sum+r
	n=n//10
print("sum of digits=",sum)