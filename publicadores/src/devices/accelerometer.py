##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: accelerometer.py
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
#           |                        |    la instancia de la    |    posición del       |
#           |                        |    clase                 |    adulto mayor en un |
#           |                        |                          |    determinado        |
#           |                        |                          |    momento            |
#           +------------------------+--------------------------+-----------------------+
#           |          magnitude     |  - self: definición de   |  - Calcula la         |
#           |                        |    la instancia de la    |    magnitud de los    |
#           |                        |    clase                 |    diferentes puntos  |
#           |                        |                          |    de ubicación       |
#           |                        |                          |    del paciente       |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
from faker import Faker
import random
import math

class Accelerometer:

    def __init__(self):
        fake = Faker()
        self.id = fake.numerify(text="%%######")
        self.force_x = (random.random()*10)*(random.choice([1,-1]))
        self.force_y = (random.random()*10)*(random.choice([1,-1]))
        self.force_z = (random.random()*10)*(random.choice([1,-1]))

    def magnitude(self):
        return math.sqrt(math.pow(self.force_x, 2)+ math.pow(self.force_y, 2) + math.pow(self.force_z, 2))


    def run(self):
        """
        una caída se puede determinar de acuerdo al posicionamiento
        de la persona en un determinado momento
        """
        if self.magnitude() >= 10:
            self.force_x = 0
            self.force_y = 0
            self.force_z = 0
        else:
            self.force_x += (random.choice([1,-1]))
            self.force_y += (random.choice([1,-1]))
            self.force_z += (random.choice([1,-1]))

 
                 