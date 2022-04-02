##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: notifier_accelerometer.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Elías Beltrán & Juventino Aguilar & Román Guzmán & Jorge Diaz
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define el suscriptor que recibirá mensajes desde el distribuidor de mensajes
#   y lo notificará a un(a) enfermero(a) sobre posibles caídas de los pacientes
#
#   Este archivo también define el punto de ejecución del Suscriptor
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
#           |       suscribe()       |  - self: definición de   |  - inicializa el      |
#           |                        |    la instancia de la    |    proceso de         |
#           |                        |    clase                 |    monitoreo posibles |
#           |                        |                          |    caídas de los      |
#           |                        |                          |    pacientes          |                                      
#           +------------------------+--------------------------+-----------------------+
#           |        consume()       |  - self: definición de   |  - realiza la         |
#           |                        |    la instancia de la    |    suscripción en el  |
#           |                        |    clase                 |    distribuidor de    |
#           |                        |  - queue: ruta a la que  |    mensajes para      |
#           |                        |    el suscriptor está    |    comenzar a recibir |
#           |                        |    interesado en recibir |    mensajes           |
#           |                        |    mensajes              |                       |
#           |                        |  - callback: accion a    |                       |
#           |                        |    ejecutar al recibir   |                       |
#           |                        |    el mensaje desde el   |                       |
#           |                        |    distribuidor de       |                       |
#           |                        |    mensajes              |                       |
#           +------------------------+--------------------------+-----------------------+
#           |       callback()       |  - self: definición de   |  - envía a través de  |
#           |                        |    la instancia de la    |    telegram           |
#           |                        |    clase                 |    información sobre  |
#           |                        |  - ch: canal de          |    posibles caídas de |
#           |                        |    comunicación entre el |    los pacientes      |
#           |                        |    suscriptor y el       |                       |
#           |                        |    distribuidor de       |                       |
#           |                        |    mensajes [propio de   |                       |
#           |                        |    RabbitMQ]             |                       |
#           |                        |  - method: método de     |                       |
#           |                        |    conexión utilizado en |                       |
#           |                        |    la suscripción        |                       |
#           |                        |    [propio de RabbitMQ]  |                       |
#           |                        |  - properties:           |                       |
#           |                        |    propiedades de la     |                       |
#           |                        |    conexión [propio de   |                       |
#           |                        |    RabbitMQ]             |                       |
#           |                        |  - body: contenido del   |                       |
#           |                        |    mensaje recibido      |                       |
#           +------------------------+--------------------------+-----------------------+
#
#-------------------------------------------------------------------------
import json, time, pika, sys
import telepot

class NotifierAccelerometer:

    def __init__(self):
        self.topic = "notifier_accelerometer"
        self.token =  ""
        self.chat_id =  ""

    def suscribe(self):
        print("Inicio de gestión de acelerometros...")
        print()
        self.consume(queue=self.topic, callback=self.callback)

    def consume(self, queue, callback):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            channel.queue_declare(queue=queue, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(on_message_callback=callback, queue=queue)
            channel.start_consuming()
        except (KeyboardInterrupt, SystemExit):
            channel.close()
            sys.exit("Conexión finalizada...")

    def callback(self, ch, method, properties, body):
        print("enviando notificación de caida...")
        if self.token and self.chat_id:
            data = json.loads(body.decode("utf-8"))
            message = f"[{data['wearable']['date']}]: Ayudar al paciente {data['name']} {data['last_name']} se cayo muy recio ayudenlo por favor."
            bot = telepot.Bot(self.token)
            bot.sendMessage(self.chat_id, message)
        time.sleep(1)
        ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    notifier_accelerometer = NotifierAccelerometer()
    notifier_accelerometer.suscribe()