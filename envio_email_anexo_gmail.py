#SMTP

import smtplib
import email.message
from senha_enviar_email import senha_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def enviar_email():
    msg = MIMEMultipart()
    msg['Subject'] = 'Email enviado pelo Python'
    msg['From'] = 'mcanoff16@gmail.com'
    # Separar com ; os e-mails em cópia
    msg['To'] = 'canoffcarmelita@gmail.com'
    msg['Cc'] = 'mcanoff16+copia@gmail.com'
    msg['Bcc'] = ''

    # Usar o formato HTML no corpo do e-mail
    corpo_email = """<p>Boa tarde</p>
    <p>Esse é meu primeiro e-mail usando smtplib.</p>
    <p>Att,</p>
    <p>Mirian</p>
    <img src=''></>"""

    msg.attach(MIMEText(corpo_email, "html"))

    # anexar o corpo de texto e os anexos
    lista_arquivos = os.listdir("anexos")
    for nome_arquivo in lista_arquivos:
        # anexar arquivos
        with open(f"anexos/{nome_arquivo}", "rb") as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))

    # conectar no servidor de email - cada servidor vai ter parâmetros diferentes (configurações smtp)
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    # determinar o formato de criptografia - padão TLS
    servidor.starttls()

    # fazer login no e-mail - para criar a senha -> conf. conta do Google -> senhas de app
    servidor.login(msg['From'], senha_email)
    # enviar o e-mail
    servidor.send_message(msg)
    # fechar a conexão com o servidor
    servidor.quit()
    print("Email enviado.")


try:
    enviar_email()
except Exception as e:
    print("Erro ao enviar o e-mail:", e)

