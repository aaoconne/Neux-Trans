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