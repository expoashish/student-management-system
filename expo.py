import os
import platform

global liststd
liststd = ["ashish","rohan","deepak","golu","vivek","ram","shyam"]

def main():		
	print("""
	 >>>>>>>>>>>>>>>>>>>>>>>  Welcome TO Expo Technology  <<<<<<<<<<<<<<<<<<<<<<<
	 Enterr 1=To student's list
	 Enterr 2=To add new student
	 Enterr 3=To search student
	 Enterr 4=To remove student
	 E nterr 5=To edit student

	       """)

	try:
		user_input=int(input("please select an above option : "))
	except ValueError:
		print("\nThat's not true")
	else:
		print("\n ")

	if (user_input==1):
		print("List Students\n")  
		for students in liststd:
			print("=> {}".format(students))	

	elif(user_input==2):
		newstd=input("Enter name of new student : ")
		if (newstd in liststd):
			print("This student is already in the database.")
		else:
			liststd.append(newstd)
			print("New student succeffuly added")
			for students in liststd:
				print("=> {}".format(students))

	elif(user_input==3):
		srstd=input("Enter name of the student : ")
		if (srstd not in liststd):
			print("Student Name is not present in the list ")
		else:
			print("Student Name is present in the list")

	elif(user_input==4):
		rmstd=input("Enter student name for remove : ")
		if (rmstd not in liststd):
			print("This student is not in the list")
		else:
			liststd.remove(rmstd)
			for students in liststd:
				print("=> {}".format(students))

	elif(user_input==5):
		for students in liststd:
				print("=> {}".format(students))
		edsdt=input("Enter to edit student name : ")
		if (edsdt in liststd):
			newstd=input("Enter new student name to change "+edsdt+" : ")
			i=liststd.index(edsdt)
			liststd[i]=newstd
			for students in liststd:
				print("=> {}".format(students))
		else:
			print("Please enter valid name")

	elif(user_input < 1 or user_sinput > 4):
		print("This is not valid number")

# Main functionality to the project
while 1==1:
	main()
	continue_game = input('Do you want continue  y/n:')
	if(continue_game == 'y'):
		os.system('cls')
		pass
	else:
		quit()
