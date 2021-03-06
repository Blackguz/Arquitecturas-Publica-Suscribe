# Arquitectura Publica-Suscribe

## Sistema de Monitoreo de Adultos Mayores (SMAM)

Existe un asilo llamado Divina Providencia en el que viven un grupo de adultos mayores, parte del personal que trabaja en el asilo, entre otras tareas, se dedica a atender las necesidades de los adultos mayores y a monitorear su estado de salud.

La fundación Catalina Huffmann, que es una fundación altruista en la región, decidió, a manera de donación, desarrollarle al asilo un sistema de cómputo para realizar las actividades de monitoreo del estado de salud de los adultos mayores de forma (semi-)automática. Para ello, la fundación utilizó un conjunto de dispositivos “wearables” que portan cada uno de los adultos mayores. Mediante el envío de información sobre ritmo cardiaco, presión arterial y temperatura, estos dispositivos “wearables” permiten monitorear en tiempo real a cada uno de los adultos mayores y de esta forma ser más eficientes en la prevención de incidencias. Así como monitorear los horarios de medicación, y notificar sobre posibles caídas de los adultos mayores.

### Diagrama de Contexto

En la siguiente figura se muestra el diseño de la propuesta de solución del departamento de desarrollo para el SMAM.

![Vista de contenedores del SMAM](docs/context-view.png)

### Diagrama de Secuencia

En el siguiente diagrama se muestra como se comportará el sistema en tiempo de ejecución, el como los mensajes de los publicadores legan hasta los suscriptores

![Diagrama de secuencia](docs/sequence-diagram.png)

### Diagrama de Contenedores

En el siguiente diagrama se muestra con mayor detalle la estructura interna del distribuidor de mensajes y su relación con publicadores y suscriptores.

![Vista de contenedores](docs/container-view.png)

### Diagrama de Secuencia 2
En el siguiente diagrama se muestra el comportamiento o el flujo de datos de los publicadores y los sucriptores al momento de encolar, transmitir y mostrar alertas mediante el sistema.

![Diagrama de secuencia 2](docs/sequence-diagram-2.png)

## Estructura del proyecto

Este repositorio contiene los siguientes directorios y archivos:

```bash
    ├── docs                                # carpeta de documentación
    │  ├── context-view.png                 # vista del contexto del sistema
    │  ├── smam.drawio                      # archivo editable de daiagramas del sistema 
    ├── publicadores                        # publicadores del sistema
    |  ├── src                              # código fuente de los publicadores
    │     ├── devices                       # archivos de definición de dispositivos
    │        ├── accelerometer.py           # simulador del dispositivo de hardware acelerómetro
    │        ├── timer.py                   # simulador del dispositivo de hardware cronómetro
    │        ├── xiaomi_my_band.py          # simulador de dispositivo de hardware Xiaomi
    │     ├── helpers                       # archivos auxiliares del sistema
    │        ├── __init__.py                # indica la definición de módulo python
    │        ├── publicador.py              # archivo auxiliar de comunicación con el distribuidor de mensajes 
    │     ├── __init__.py                   # indica la definición de módulo python
    |     ├── group.py                      # representación de los grupos de medicación
    │     ├── patient.py                    # representación de un adulto mayor en el sistema
    |     ├── prescription.py               # representación de una receta médica
    |  ├── main.py                          # archivo principal de ejecución de publicadores
    ├── suscriptores                        # suscriptores del sistema
    │  ├── monitor_wearable.py              # suscriptor que muestra en pantalla los signos vitales de los adultos mayores
    |  ├── monitor_accelerometer.py         # suscriptor que muestra en pantalla las posibles caídas de los adultos mayores
    |  ├── monitor_timer.py                 # suscriptor que muestra en pantalla un aviso cuando un adulto mayor requiere medicamento
    │  ├── notifier_wearable.py             # suscriptor que notifica a un(a) enfermero(a) en particular sobre los signos vitales de los adultos mayores
    |  ├── notifier_accelerometer.py        # suscriptor que notifica a un(a) enfermero(a) en particular sobre posibles caídas de los adultos mayores
    |  ├── notifier_timer.py                # suscriptor que notifica a un(a) enfermero(a) en particular cuando un adulto mayor requiere medicamento
    │  ├── record_wearable.py               # suscriptor que actualiza el expediente de un adulto mayor en particular
    ├── .gitignore                          # exclusiones de git
    ├── README.md                           # este archivo
    ├── requirements.txt                    # dependencias del sistema
```


## Prerrequisitos
- Clonar el repositorio:
   ```shell
   $ git clone https://github.com/Blackguz/Arquitecturas-Publica-Suscribe.git
   $ cd Arquitecturas-Publica-Suscribe
   ```
- Contar con python 3.8 o superior y pip3 (las pruebas fueron realizadas con la versión 3.8). Se recomienda utilizar [pyenv](https://github.com/pyenv/pyenv) como manejador de versiones de python; una vez instalado se pueden seguir los siguientes comandos para instalar la versión deseada de python, esto hay que realizarlo en la raíz del repositorio:
   ```shell
   $ pyenv install 3.8
   $ pyenv local 3.8
   ```

- Crear un ambiente virtual para manejar las dependencias ejecutando:
   ```shell
   $ python3 -m venv venv
   ```

   en Windows:
   ```shell
   $ python3 -m venv venv
   ```

   si no funciona el comando anterior, ejecutar el siguiente:
   ```shell
   $ py -3 -m venv venv
   ```

   Esto creará una carpeta llamada "venv" que representa nuestro ambiente virtual y donde instalaremos todas las dependencias.

- Activamos el ambiente virtual:
   ```shell
   $ source venv/bin/activate
   ```

   o en Windows:
   ```shell
   $ venv\Scripts\activate
   ```

- Instalamos las dependencias del sistema ejecutando:
   ```shell
   (venv)$ pip3 install -r requirements.txt 
   ```

   Los paquetes que se instalarán son los siguientes:

   Paquete | Versión | Descripción
   --------|---------|------------
   pika   | 1.1.0   | Implementación del protocolo AMQP 0-9-1 y que incuye la extensión de RabbitMQ
   Faker  | 13.3.0  | Generador de datos falsos
   telepot| 12.7    | Api de Telegram

   *__Nota__: También puedes instalar estos prerrequisitos manualmente ejecutando los siguientes comandos:*   
   > pip3 install pika== 1.1.0
   > pip3 install Faker==13.3.0
   > pip3 install telepot==12.7

- Instalamos RabbitMQ. La manera recomendada para implementar una instancia de RabbitMQ es utilizando [Docker](https://www.docker.com/), para instalarlo puedes seguir las instrucciones para cada sistema operativo haciendo clic [aquí](https://docs.docker.com/install/). Una vez instalado docker podemos ejecutar el siguiente comando:

    ```shell
    $ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
    ```

    Este comando correrá un contenedor de docker con la imagen de RabbitMQ, el cual seguirá corriendo hasta que sea detenido explícitamente.

## Ejecución

Sigue las siguientes instrucciones para ejecutar los diferentes componentes del sistema.

> **Nota:** Cada componente debe ser ejecutado en una terminal independiente

### Publicador

- Entramos a la carpeta `publicadores`:
   ```shell
   (venv)$ cd publicadores
   ```

- Ejecutamos el archivo `main.py`:
   ```shell
   (venv)$ python main.py
   ```

### Suscriptores

**Notificador de alertas del wearable**

- Entramos a la carpeta `suscriptores`:
   ```shell
   (venv)$ cd suscriptores
   ```

- Ejecutamos el archivo `notifier_wearable.py`:
   ```shell
   (venv)$ python notifier_wearable.py
   ```

**Notificador de alertas del temporizador**

- Entramos a la carpeta `suscriptores`:
   ```shell
   (venv)$ cd suscriptores
   ```

- Ejecutamos el archivo `notifier_timer.py`:
   ```shell
   (venv)$ python notifier_timer.py
   ```
**Notificador de alertas del acelerómetro**

- Entramos a la carpeta `suscriptores`:
   ```shell
   (venv)$ cd suscriptores
   ```

- Ejecutamos el archivo `notifier_accelerometer.py`:
   ```shell
   (venv)$ python notifier_accelerometer.py
   ```

**Log**

- Entramos a la carpeta `suscriptores`:
   ```shell
   (venv)$ cd suscriptores
   ```

- Ejecutamos el archivo `record_wearable.py`:
   ```shell
   (venv)$ python record_wearable.py
   ```

**Monitor del wearable**

- Entramos a la carpeta `suscriptores`:
   ```shell
   (venv)$ cd suscriptores
   ```

- Ejecutamos el archivo `monitor_wearable.py`:
   ```shell
   (venv)$ python monitor_wearable.py
   ```
**Monitor del temporizador**

- Entramos a la carpeta `suscriptores`:
   ```shell
   (venv)$ cd suscriptores
   ```

- Ejecutamos el archivo `monitor_timer.py`:
   ```shell
   (venv)$ python monitor_timer.py
   ```
**Monitor del acelerómetro**

- Entramos a la carpeta `suscriptores`:
   ```shell
   (venv)$ cd suscriptores
   ```

- Ejecutamos el archivo `monitor_accelerometer.py`:
   ```shell
   (venv)$ python monitor_accelerometer.py
   ```


## Versión

2.2.0 - Marzo 2022

## Autores

* **Perla Velasco**
* **Yonathan Martínez**
* **Sergio Salazar**
* **Jorge Solis**
* **Elías Emiliano Beltrán González**
* **Juventino Aguilar Correa**
* **Román Guzmán Valles**
* **Jorge Luis Díaz Serna**
