import random
from src.prescription import Prescription

class Group():
    def __init__(self, name):
        self.name = name
        self.schedule = []
        medicine = ['Paracetamol', 'Dipirona magnésica', 'Dipirona hioscina', 'Tramadol', 'Antidepresivo', 'Aspirina', 'Antiarritmico', 'Diuretico']
        total = random.randint(1, len(medicine))

        for i in range(total):
            hours = random.choice([4, 6, 8, 12, 24])
            medicine_idx = random.randint(0, len(medicine)-1)
            selected_medicine = medicine.pop(medicine_idx)
            self.schedule.append(Prescription(selected_medicine, hours, random.randint(5, 20)))
