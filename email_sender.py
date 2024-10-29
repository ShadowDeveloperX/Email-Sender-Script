import smtplib
import ssl
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(to_email, subject, body):
    """
    Envía un correo electrónico.
    
    :param to_email: Dirección de correo del destinatario
    :param subject: Asunto del correo
    :param body: Cuerpo del correo
    """
    port = 465  # Para SSL
    smtp_server = "smtp.gmail.com"

    # Crea el mensaje
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Crea una conexión segura con el servidor
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Inicia sesión en el servidor
            server.sendmail(EMAIL_ADDRESS, to_email, message)  # Envía el correo
        print(f"Correo enviado a {to_email} con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
