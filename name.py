# Name()
# Prompts user for name 
# nameCheck(). make sure with user that input looks correct 
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
                    name = input("Name: ") 
                    self._name = name 
                    return self._name 
                    