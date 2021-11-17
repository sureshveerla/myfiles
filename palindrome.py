n=int(input("enter any number"))
rev=0
temp=n
while(n>0):
	r=n%10
	rev=rev*10+r
	n=n//10
if(temp==rev):
	print("Given number is Palindrome : ",temp)
else:
	print("Given number is not Palindrome : ",temp)