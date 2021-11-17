s=input("Enter Name string = ")
for i in range(0,len(s)):
	for j in range(0,i+1):
		print(s[j],end=" ")
	print()