# address where service will be provided

class Address():
    def __init__(self, address = input("Address: ")):
          self._address = address 
          
    def addressCheck(self):
        if self._address != "":
            print("Does address of service look correct? " + self._address)
            input("Y or N?")
        if input == "y" or "Y":  
            return self._address  
        else:
            address = input("Address: ")
            self._address = address 
            return self._address

                  
              
            