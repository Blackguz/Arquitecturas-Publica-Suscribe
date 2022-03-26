import random

class Prescription():
    def __init__(self, medicine, hour, dose):
        self.medicine = medicine
        self.hour = hour
        self.dose = dose
        self.unit = random.choice(['mg', 'ml'])
