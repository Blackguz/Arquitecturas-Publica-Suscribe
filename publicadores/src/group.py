##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: group.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Elías Beltrán & Juventino Aguilar & Román Guzmán & Jorge Diaz
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define un grupo de prescripciones que se deben recetar a todos los
#   pacientes que forman parte del grupo
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
#           |                        |                          |                       |
#           |                        |  - name: nombre del      |                       |
#           |                        |    grupo                 |                       |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import random
from src.prescription import Prescription

class Group():
    def __init__(self, name):
        self.name = name
        self.schedule = []
        medicine = ['Paracetamol', 'Dipirona magnésica', 'Dipirona hioscina', 'Tramadol', 'Antidepresivo', 'Aspirina', 'Antiarritmico', 'Diuretico']
        total = random.randint(1, len(medicine))

        for i in range(total):
            hours = random.choice([1, 4, 6, 8, 12, 24])
            medicine_idx = random.randint(0, len(medicine)-1)
            selected_medicine = medicine.pop(medicine_idx)
            self.schedule.append(Prescription(selected_medicine, hours, random.randint(5, 20)))
