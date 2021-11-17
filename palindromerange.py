min=int(input("Enter Minimum Number"))
max=int(input("Enter Maximum Number"))
for i in range(min,max+1):
	n=i
	rev=0
	while(n>0):
		r=n%10
		rev=rev*10+r
		n=n//10
		if(i==rev):
			print(i,end=' ')