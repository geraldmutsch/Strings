#some examples of string operations

teacher = input("Name of the Teacher?")   #get the name and story it in a string variable
welcome = "Hello " + teacher + "! You are the teacher today"    #creating the welcome message in a new string
print (welcome)                         #print the welcome message on the screen


#work with indices
OneLetter = teacher[4]              #Get the 5th letter of the teachers name
print ("The 5th letter in the teacher's name is " + OneLetter)
print ("The name of the teacher is " + str(len(teacher)) + " characters")    #get the length of a string

#slicing the string
print(teacher[3:])  #returns character 4 -> End
print(teacher[2:4]) #returns characters 3 to 5 (=3 and 4)
print(teacher[:3])  #returns charaters up to 4 (1,2,3)


#looping through a string
letter_number=0                                             #needed for counting
for letter in teacher:
    letter_number=letter_number + 1                         #count up
    print(str(letter_number) + ":" + letter)                #print letter and count

#string library
print(teacher.lower())   #print teacher name in lowercase

if (teacher.find("Gerald") > -1) :  #find if "Gerald" is in the string
    print("Wow, its you!")          #if yes
else:                               #if no
    print("Seems not to be you")

NewTeacher = welcome.replace("Gerald","Bob")    #replace one part with another
print(NewTeacher)

#Now find the first name
FullName = input("Fullname please:")
PlaceOfTheSpace = FullName.find(" ")
print(FullName[:PlaceOfTheSpace])       #print only the first name