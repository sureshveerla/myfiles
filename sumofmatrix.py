matrix=[]
rows=int(input("Enter No.of Rows " ))
columns=int(input("Enter No.of columns " ))
for i in range(0,rows):
	l=[]
	for j in range(0,columns):
		x=int(input("Enter"+str(i+1)+"rows"+str(j+1)+"columns"))
		l.append(x)
	matrix.append(l)
print(matrix)




sum=0
for i in range(0,rows):
	for j in range(0,columns):
		sum=sum+matrix[i][j]
print(" sum ",sum)