# Email-Sender-Script

Este script en Python permite enviar correos electrónicos de manera sencilla y automatizada, ideal para notificaciones, reportes o recordatorios.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

El **Email-Sender-Script** facilita el envío de correos electrónicos utilizando el servidor SMTP de Gmail (puedes adaptarlo para otros proveedores). Permite personalizar el destinatario, asunto y cuerpo del mensaje.

## Requisitos

- Python 3.x
- Librería `smtplib` (incluida en la biblioteca estándar de Python)
- Librería `ssl` (incluida en la biblioteca estándar de Python)

## Instalación

1. **Clona este repositorio**:

    ```bash
    git clone https://github.com/tu_usuario/Email-Sender-Script.git
    cd Email-Sender-Script
    ```

2. **Instala las dependencias** (si decides usar otras librerías, añade aquí):

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Configura tu correo en `config.py`:

```python
# config.py
EMAIL_ADDRESS = "tu_correo@gmail.com"
EMAIL_PASSWORD = "tu_contraseña"

