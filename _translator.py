# Translator()
# Refers to the employee 
# conditions for Translator  

class Translator:
    def __init__(self, _translator = str(input("Translator: "))):
          self._trans = _translator 
     
    def transCheck(self):
        if self._trans != "":
        #TODO: check should be done after row data filled. 
            # print("Is the Translator correct?: " + self._trans)
            # input("y or n: ")
            return self._trans 
        if input == "y":
            return self._trans 
        else:
            _translator = str(input("Translator: "))
            self._trans = _translator
            return self._trans 
        

# _translatorCell = list of multiple rows from user 
# append() to add the next one to the list 
# _translatorCell = []        
# for _translator in Translator():
# 	if _translator != "":
#         	_transCell = _translator
# _translatorCell.append(_transCell)



# define infinte loop when translator input > 1 

            