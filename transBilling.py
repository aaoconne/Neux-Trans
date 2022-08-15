import openpyxl
import csv

# to fill in for "Date" portion of excel file 
from datetime import date 

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
               print("Does the client look correct: " + self.client)
               input(clientString = "y" or "n")
          if clientString == "y":
               return self._client 
               print(self._client)
          else:
               self._client == client 
               print(self.client)


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
               str(input(noOfficeString = "Y OR N: "))
          if noOfficeString == "Y":
               noOffice = True 
               self._office = "NA"
               return self._office 
          else:
               self._office = office
               return self._office 

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

# boolean check to see if office relevant or not 
# string to make sure user input looks as should 
# office obj 
noOffice = False  
noOfficeString = str 
office = Office()


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
         myFile.writerow([today,_translator._trans,client._client,office._office])
    else:
         print("Please fill in who the translator was for client: ")
