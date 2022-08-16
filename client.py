# Client()
# prompts user for who was being billed (client side)
# check to see if user answered prompt
# if their input looks correct, continue processing 
    # else prompt user for correct client info 
    
class Client:
     def __init__(self, client = input("Interpreted For: ")):
          self._client = client
          
     def clientCheck(self):
        if self._client != "":
               print("Does the client look correct: " + self._client)
               input("y or n: ")
               return self._client 
        if input == "y":
            return self._client 
        else:
            client  = input("Interpreted For: ")
            self._client = client
            return self._client 
