n=input("enter any number")
m=int(n)
sum=0
while(m>0):
	r=m%10
	sum=sum+r**len(n)
	m=m//10
if(int(n)==sum):
	print(len(n),"digit is armstrong number ")
else:	
	print("not an armstrong number ")
	