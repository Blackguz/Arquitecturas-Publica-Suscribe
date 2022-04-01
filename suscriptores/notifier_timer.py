##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: notifier_timer.py
# Capitulo: Estilo Publica-Suscribe
# Autor(es): Elías Beltrán & Juventino Aguilar & Román Guzmán & Jorge Diaz
# Version: 3.0.0 Marzo 2022
# Descripción:
#
#   Esta clase define el suscriptor que recibirá mensajes desde el distribuidor de mensajes
#   y lo notificará a un(a) enfermero(a) én particular para informarle sobre los horarios de
#   medicación de los pacientes
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
#           |                        |    clase                 |    monitoreo de       |
#           |                        |                          |    horarios de        | 
#           |                        |                          |    medicación         |
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
#           |                        |    la instancia de la    |    telegram los datos |
#           |                        |    clase                 |    de los adultos     |
#           |                        |  - ch: canal de          |    mayores a los que  |
#           |                        |    comunicación entre el |    les toca tomar su  |
#           |                        |    suscriptor y el       |    medicamento        |
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

class NotifierTimer:

    def __init__(self):
        self.topic = "notifier_timer"
        self.token = "5285113669:AAFwwevUAPc2crTsdnDF69OjDynBs-xhykY"
        self.chat_id = "-1001541014221"

    def suscribe(self):
        print("Inicio de gestión de medicamento...")
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
        print("enviando notificación de medicinas...")
        if self.token and self.chat_id:
            data = json.loads(body.decode("utf-8"))
            prescription = ", ".join("{}{} de {}".format(x[1], x[2], x[0]) for x in data['timer']['medicine'])
            message = f"[{data['wearable']['date']}]: Medicar al paciente {data['name']} {data['last_name']} con {prescription}\nSSN: {data['ssn']}, Edad: {data['age']}"
            bot = telepot.Bot(self.token)
            bot.sendMessage(self.chat_id, message)
        time.sleep(1)
        ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    notifier_timer = NotifierTimer()
    notifier_timer.suscribe()
