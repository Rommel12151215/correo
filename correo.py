import smtplib

def enviar_correo():
   servidor = smtplib.SMTP('smtp.gmail.com', 587)
   servidor.starttls()
   servidor.login("tu_correo@gmail.com", "tu_contraseña")
   mensaje = "Hola, este es un correo enviado desde Python"
   servidor.sendmail("tu_correo@gmail.com", "correo_destino@gmail.com", mensaje)
   servidor.quit()

enviar_correo()
