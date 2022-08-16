# Translator()
# Refers to the employee 
# conditions for Translator  

class Translator:
     def __init__(self, _translator = str(input("Translator: "))):
          self._trans = _translator 
     
     def transCheck(self):
        if self._trans != "":
            print("Is the Translator correct?: " + self._trans)
            input("y or n: ")
            return self._trans 
        if input == "y":
            return self._trans 
        else:
            _translator = str(input("Translator: "))
            self._trans = _translator
            return self._trans 
            