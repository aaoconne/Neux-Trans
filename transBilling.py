import array as arr 
import csv
from _translator import Translator 
from client import Client  
from office import Office 
from name import Name 
from address import Address 
from appointmentTime import AppointmentTime
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
 
bMoreRecs = False  

# driver code 
currentDate = date.today()

# _translator obj 
_translator = Translator() 
_translator.transCheck()
 
 # client obj 
client = Client()
client.clientCheck()

office = Office()
office.officeCheck()

# name obj 
# can probably be discarded but for right now, think of as person providing treatment 
name = Name()
name.nameCheck()

address = Address()
address.addressCheck()

apptTime = AppointmentTime()
apptTime.apptTimeCheck() 



# opening or creating the file 
def main(): 
     with open('Billing.csv', 'w', newline ="") as file:
          myFile = csv.writer(file)
    
          # writing the column headers. different headers on sheet 
          # "Services Provided" included: Medical, Legal, Translation
          myFile.writerow(["Date","Translator","Interpreted For","Office","Name","Address","Appointment Time","Arrival Time Interpreter",  
                     "Arrival Time Patient","End Time","Services Provided","Total Miles","Parking Garage","Paid","Billed","Client"])
         
          # TODO: change this to check for boolean  
          #if _translator != "" :
          while bMoreRecs: 
               myFile.writerow([currentDate, _translator._trans ,client._client, office._office, name._name, address._address, apptTime._apptTime])
               moreRecsStr = input("Would you like to bill another client? Y or N: ")
               if moreRecsStr.contains("N" or "n"):
                    break
               else: 
                    continue 
               
if __name__ == "__main__":
     main() 
