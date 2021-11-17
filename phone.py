phone=input("Enter phone number")
if(phone.isdigit()):
	if(len(phone)==8 or len(phone)==10):
		if(phone[0:4]=="6304" or phone[0:4]=="7075"):
			print(phone,"valid jio phone number")
		elif(phone[0:4]=="8374" or phone[0:4]=="9515"):
			print(phone,"valid airtel number")	
		else:
			print("Invalid phone number")
	else:
		print("enter 8 or 10 digit phone number")
else:
	print("enter valid phone number")