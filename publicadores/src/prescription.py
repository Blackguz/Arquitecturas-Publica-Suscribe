##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: prescription.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Elías Beltrán & Juventino Aguilar & Román Guzmán & Jorge Diaz
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define una prescripcion, la cual contiene información de la medicina,
#   el horario y la dosis que debe consumir el paciente
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
#           |                        |  - medicine: el nombre   |                       |
#           |                        |    de la medicina        |                       |
#           |                        |    recetada en la        |                       |
#           |                        |    prescripcion          |                       |
#           |                        |                          |                       |
#           |                        |  - hour: el intervalo de |                       |
#           |                        |    horas que deben pasar |                       |
#           |                        |    para suministrar la   |                       |
#           |                        |    medicina              |                       |
#           |                        |                          |                       |
#           |                        |  - dose: la cantidad de  |                       |
#           |                        |    medicina recetada     |                       |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import random

class Prescription():
    def __init__(self, medicine, hour, dose):
        self.medicine = medicine
        self.hour = hour
        self.dose = dose
        self.unit = random.choice(['mg', 'ml'])
