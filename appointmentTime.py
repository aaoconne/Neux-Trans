class AppointmentTime():
    def __init__(self, apptTime = input("Appointment Time: ")):
          self._apptTime = apptTime 
          
    def apptTimeCheck(self):
        if self._apptTime != "":
            print("Does the appointment time look correct? " + self._apptTime)
            input("Y or N?")
        if input == "y" or "Y":  
            return self._apptTime  
        else:
            apptTime = input("Appointment Time: ")
            self._apptTime = apptTime  
            return self._apptTime 