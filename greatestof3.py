a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>b and a>c):
	print("a is greater than b,c")
elif(b>a and b>c):
	print("b is greater than a,c")
else:
	print("c is greater than a,b")