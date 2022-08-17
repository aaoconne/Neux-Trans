import array as arr 
import csv
from _translator import Translator 
from client import Client  
from office import Office 
from name import Name 
from datetime import date 

#   TODO: 
#	Rest of cells 
#	Array of everything would be faster.
#	Associate [index] with column. 		
#	Functionality to add more than one billing sheet 
#    	Store all items in array, add to list, prompt user for another row to be added
#    	Add functionality to read over prior file so new one created each day. Solution: Add date to end of file so they never look the same 
#    	Functionaltiy to read over a months worth of files and give monthy look 
# 	if there is another row to be added for new billing statement, prompt user "Do you need to file another: " 
# 	if user input = no, write file 
# 	newRow = False 

# address = input("Address: ")
# appTime = input("Appointment Time: ")
# arrivalTime = input("Arrival Time: ")
# empArrivalTime = input("Arrival Time Interpreter: ")
# clientArrivalaTime = input("Arrival Time of Patient: ")
# endTime = input("End Time: ")
# obj 
# servicesProvided = str(input("Services Provided: " + typeOfService)) 

# driver code 
today = date.today()

# _translator object
# check to make sure input != ""
# creation of _translator object 
# call to transCheck() instance method
_translator = Translator() 
_translator.transCheck()


# client object 
# clientString = str 
# call to clientCheck() instance method 
client = Client()
client.clientCheck()

# string to make sure user input looks as should 
# office obj 
office = Office()
office.officeCheck()

# name obj 
# string to make sure name looks okay  
name = Name()
name.nameCheck()

	
     
# opening or creating the file 
with open('Billing.csv', 'w', newline ="") as file:
    myFile = csv.writer(file)
    
    # writing the column headers. different headers on sheet 
    # "Services Provided" included: Medical, Legal, Translation
    myFile.writerow(["Date","Translator","Interpreted For","Office","Name","Address","Appointment Time","Arrival Time Interpreter",  
                     "Arrival Time Patient","End Time","Services Provided","Total Miles","Parking Garage","Paid","Billed","Client"])
         
    # TODO: will go in processFile.py 
    if _translator != "" :
         myFile.writerow([today,_translator._trans,client._client,office._office,name._name])
    else:
         print("Please fill in who the translator was for client: ")
