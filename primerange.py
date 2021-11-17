min=int(input("Enter Minimum Value"))
max=int(input("Enter Maximum Value"))
for i in range(min,max+1):
	for j in range(2,i//2+1):
		if(i%j==0):
			break;	
	else:
		print(i,end=" ")