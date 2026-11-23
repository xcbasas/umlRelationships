class Patient:
    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        print(f"Patient Name:  {self.__name}")

    def set_name(self,new_name):
        self.__name = new_name

    def get_bill_amount(self):
        return self.__bill_amount
    
    def set_bill_amount(self, new_bill_amount):
        self.__bill_amount = new_bill_amount

    def calculate_bill(self):
        print(f"Final Bill:  {self.__bill_amount}")

class Senior(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name,bill_amount)

    def calculate_bill(self):
            bill_amount = self.get_bill_amount()
            final_bill_amount = bill_amount - (bill_amount * 20)/100
            self.set_bill_amount(final_bill_amount)
            print(f"Final Bill:  {self.get_bill_amount()}")
    
class PhilHealth(Patient):
    def __init__(self,name,bill_amount):
        super().__init__(name,bill_amount)

    def calculate_bill(self):
        bill_amount = self.get_bill_amount()
        final_bill_amount = bill_amount - (bill_amount * 15)/100
        self.set_bill_amount(final_bill_amount)
        print(f"Final Bill:  {self.get_bill_amount()}")

regular_patient = Patient("Haruhi Fujioka", 15000)
regular_patient.get_name()
print(f"Original Bill:  {regular_patient.get_bill_amount()}")
regular_patient.calculate_bill()
print("")
senior_patient = Senior("Mitsukuni Haninozuka", 15000)
senior_patient.get_name()
print(f"Original Bill:  {senior_patient.get_bill_amount()}")
senior_patient.calculate_bill()
print("")
philhealth_patient = PhilHealth("Hikaru Hitachiin", 15000)
philhealth_patient.get_name()
print(f"Original Bill:  {philhealth_patient.get_bill_amount()}")
philhealth_patient.calculate_bill()