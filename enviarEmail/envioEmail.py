from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
def Envio(arquivoenviar):
    host = 'smtp.gmail.com'
    port = '587'
    login = 'pythonunit4@gmail.com'
    password = '85356325ll'
    destino = 'dbm@unitfour.com.br'

    #conexão
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login, password)

    #criar email

    corpo = 'Segue em anexo a basesMensal BPC  tratada, para Importação'
    email = MIMEMultipart()
    email['From'] = login
    email['TO'] = destino
    email['Subject'] = 'Email Automatico BPC  - Python'
    email.attach(MIMEText(corpo, 'plain'))
    #ler arquivo
    arquivo = arquivoenviar
    arquivoLido = open(arquivo, 'rb')

    arquivoBase = MIMEBase('application', 'octet-stream')
    arquivoBase.set_payload(arquivoLido.read())
    encoders.encode_base64(arquivoBase)
    #Adicionar cabeçalho no tipo anexo de email
    arquivoBase.add_header('Content-Disposition', f'attachment; filename={arquivo}')
    arquivoLido.close()
    email.attach(arquivoBase)
    server.sendmail(email['From'], email['TO'], email.as_string())
    server.quit()
    print('Arquivo enviado com sucesso')

if __name__ == '__main__':
    Envio('main.py')

