import openpyxl
import csv

from datetime import date 

# TODO: 
#    Rest of cells 
#    Functionality to add more than one billing sheet 
#    Store all items in array, add to list, prompt user for another row to be added
#    Add functionality to read over prior file so new one created each day. Solution: Add date to end of file so they never look the same 
#    Functionaltiy to read over a months worth of files and give monthy look 

# if there is another row to be added for new billing statement, prompt user "Do you need to file another: " 
# if user input = no, write file 
# newRow = False 

# Translator()
# Refers to the employee 
# conditions for Translator  
class Translator:
     def __init__(self, _translator = str(input("Translator: "))):
          self._trans = _translator 
     
     def transCheck(self):
          if self._trans != "":
               return self._trans 
          else:
               print("Please enter a name for Translator: ")

# Client class 
# Refers to the person being Interpreted for
# conditionals for the client                
class Client:
     def __init__(self, client = input("Interpreted For: ")):
          self._client = client 
          
     def clientCheck(self):
          if self._client != "":
               print("Does the client look correct: " + self._client)
               input("y or n: ")
          if input == "y":
               return self._client 
          else:
               self._client == client 
               print(self._client)


# Office()
# Refers to the office employee will be going to 
# conditions based on user response                
class Office:
     def __init__(self, office = input("Office: ")):
          self._office = office 
     
     def officeCheck(self):
          if self._office != "":
               return self._office
          else:
               print("If NA: Y Or N") 
               input("y or n: ")
          if input == "y":
               self._office = "NA"
               return self._office 
          else:
               self._office = office
               return self._office 
          
class Name:
     def __init__(self, name = input("Name: ")):
          self._name = name 
          
     def nameCheck(self):
          if self._name != "":
               print("Does this name look correct? " + self._name)
               input("y or n: ")
               if input == "y":
                    return self._name 
               else: 
                    self._name = name 
                    return self._name 
                    
                    

# driver code 
today = date.today()

# _translator object
# check to make sure input != ""
_translator = Translator()
_translator.transCheck()

# string for if client looks correctly
# client object 
clientString = str 
client = Client()
client.clientCheck()

# boolean check to see if office relevant or not 
# string to make sure user input looks as should 
# office obj 
officeBool = False  
noOfficeString = str 
office = Office()
office.officeCheck()

# name obj 
# string to make sure name looks okay  
nameStr = str 
nameBool = False 
name = Name()
name.nameCheck()


# ''' # storing input 
# name = str(input("Name: "))
# address = input("Address: ")
# appTime = input("Appointment Time: ")
# arrivalTime = input("Arrival Time: ")
# empArrivalTime = input("Arrival Time Interpreter: ")
# clientArrivalaTime = input("Arrival Time of Patient: ")
# endTime = input("End Time: ")
# obj 
# servicesProvided = str(input("Services Provided: " + typeOfService)) 
     
     
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
