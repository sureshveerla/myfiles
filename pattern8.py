rows=int(input("Enter Any Number "))
num=rows
for i in range(rows,0,-1):
	for j in range(0,i):
		print(num,end=" ")
	print("\r")