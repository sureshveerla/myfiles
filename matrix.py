matrix=[]
rows=int(input("Enter Number of Rows "))
columns=int(input("Enter Number of Columns "))
for i in range(0,rows):
	l=[]
	for j in range(0,columns):
		x=int(input("Enter"+ str(i+1)+"row"+ str(j+1)+ "element"))
		l.append(x)
	matrix.append(l)
print(matrix)