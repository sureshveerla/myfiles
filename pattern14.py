s=input("Enter Any String = ")
for i in range(0,len(s)):
	for j in range(i-len(s),0):
		print(s[j],end=" ")
	print()