# IMPAP
from imap_tools import MailBox, AND
from senha_enviar_email import senha_email

usuario = "mcanoff16@gmail.com"
senha = senha_email

# configurar o servidor - meu_email será a caixa de entrada do e-mail?
meu_email = MailBox("imap.gmail.com").login(usuario, senha, '[Gmail]/E-mails enviados')

# verificando as pastas que temos disponíveis no e-mail.

# for pasta in meu_email.folder.list():
#     print(pasta)
# pegar os emais dessa caixa de entrada - o que o comando fetch precisa de alguns critérios de seleção do e-mail (olhar a documentação do IMAP - https://pypi.org/project/imap-tools/#search-criteria)

lista_emails = meu_email.fetch(AND(from_=usuario, to='canoffcarmelita@gmail.com'))

# print(list(lista_emails))

for email in lista_emails:
    # email.attachmenst - lista com os anexos
    if len(email.attachments) > 0:
        print(email.subject)
        print(email.text)
        print(email.html)
        for anexo in email.attachments:
            print(f"Anexo: {anexo.filename}")
