n=int(input("Enter Any Number"))
sq=n*n
co=0
while(n>0):
	if(n%10!=sq%10):
		print(n,"is not a Automorphic Number ")
		co=1
		break;
	n=n//10
	sq=sq//10
if(co==0):
	print(n,"is an Automorphic Number ") 