n=int(input("Enter Any Number"))
for i in range(1,n+1):
	for j in range(1,n-i+2):
		print(j,end=" ")
	print()