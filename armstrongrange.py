min=int(input("Enter Minimum Number "))
max=int(input("Enter Maximum Number "))
for i  in range(min,max+1):
	n=i
	sum=0
	while(n>0):
		r=n%10
		sum=sum+r**len(str(i))
		n=n//10
	if(i==sum):
		print(i,end=" ")