# Office()
# prompts user for the office where appointment took place 
# officeCheck() to check with user if what was input looks correct 

class Office:
     def __init__(self, office = input("Office: ")):
          self._office = office 
     
     def officeCheck(self):
          if self._office != "":
               return self._office
          # else:
          #      print("If NA: Y Or N") 
          #      input("y or n: ")
          if input == "y":
               self._office = "NA"
               return self._office 
          else:
               office = input("Office: ")
               self._office = office
               return self._office 