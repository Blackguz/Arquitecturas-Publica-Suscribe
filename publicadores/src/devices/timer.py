##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: timer.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define el publicador que enviará mensajes hacia el distribuidor de mensajes
#
#   A continuación se describen los métodos que se implementaron en esta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |       __init__()       |  - self: definición de   |  - constructor de la  |
#           |                        |    la instancia de la    |    clase              |
#           |                        |    clase                 |                       |
#           +------------------------+--------------------------+-----------------------+
#           |          run()         |  - self: definición de   |  - simula la          |
#           |                        |    la instancia de la    |    alarma que         |
#           |                        |    clase                 |    determina el       |
#           |                        |                          |    momento en el que  |
#           |                        |                          |    se debe            |
#           |                        |                          |    administrar algún  |
#           |                        |                          |    medicamento a los  | 
#           |                        |                          |    adultos mayores    |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from time import strftime
from faker import Faker
import random, datetime

class Timer:

    def __init__(self):
        fake = Faker()
        self.id = fake.numerify(text="%%######")
        self.last_modify = int(datetime.datetime.now().strftime("%H"))-1

    def run(self, groups):
        current_hour = int(datetime.datetime.now().strftime("%H"))

        self.medicine = []

        print("current:",current_hour,"last:",self.last_modify)

        if current_hour == self.last_modify:
            return

        for group in groups:
            for prescription in group.schedule:
                if current_hour % prescription.hour == 0:
                    self.medicine.append((prescription.medicine, prescription.dose, prescription.unit))
        self.last_modify = int(datetime.datetime.now().strftime("%H"))
