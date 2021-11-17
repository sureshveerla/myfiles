s=input("Enter Name String = ")
for i in range(0,len(s)):
	for j in range(0,len(s)-i):
		print(s[j],end=" ")
	print()