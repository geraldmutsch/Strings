#some examples of string operations
teacher = input("Name of the Teacher?")   #get the name and story it in a string variable
welcome = "Hello " + teacher + "! You are the teacher today"    #creating the welcome message in a new string
print (welcome)                         #print the welcome message on the screen

#work with indices
OneLetter = teacher[4]              #Get the 5th letter of the teachers name
print ("The 5th letter in the teacher's name is " + OneLetter)
print ("The name of the teacher is " + str(len(teacher)) + " characters")    #get the length of a string

