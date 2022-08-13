import openpyxl
import csv

from processFile import processFile 


obj = processFile()
obj.processFile() 
# to fill in for "Date" portion of excel file 
from datetime import date 

# storing input 
today = date.today()
translator = str(input("Translator: "))
client = str(input("Interpreted For: "))
office = input("Office: ")


        

# opening or creating the file 
with open('Billing.csv', 'w', newline ="") as file:
    myFile = csv.writer(file)
    
    # writing the column headers. different headers on sheet 
    # "Services Provided" included: Medical, Legal, Translation
    myFile.writerow(["Date","Translator","Interpreted For","Office","Name","Address","Appointment Time","Arrival Time Interpreter",  
                     "Arrival Time Patient","End Time","Services Provided","Total Miles","Parking Garage","Paid","Billed","Client"])
    
        
    # TODO: will go in processFile.py 
    if translator != "" :
         myFile.writerow([today,translator])
    else:
         obj.print("Please fill in who the translator was for client: ")
            
    
    
    
    
    

