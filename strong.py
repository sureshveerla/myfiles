n=int(input("Enter Any Number " ))
temp=n
sum=0
while(temp):
	r=temp%10
	temp=temp//10
	fact=1
	for i in range(1,r+1):
		fact=fact*i
if(sum==n):
	print("Given Number is Strongest Number ")
else:
	print("Given number is Not A Strongest Number ")

	