from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from datetime import date
from datetime import timedelta
import locale
def Envio(arquivoenviar,destino):
    locale.setlocale(locale.LC_ALL, '')
    mes = date.today()
    mes = mes - timedelta(days=30)
    mes = mes.strftime('%B de %Y')
    host = 'smtp.office365.com'
    port = '587'
    login = 'rpa_unit4@outlook.com'
    password = 'RPA123456'
    #conexão
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login, password)
    #criar email
    corpo = f'Segue em anexo a base mensal de {mes}, BPC  tratada, para Importação'
    email = MIMEMultipart()
    email['From'] = login
    email['TO'] = destino
    email['Subject'] = f'Email Automatico BPC {mes}  - Python'
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
    emails = ['leandro.silva@unitfour.com.br',
          'paulo.melo@unitfour.com.br',
          'vinicius.spigariol@unitfour.com.br']
    for email in emails:
        Envio('basenovosexcluidos.csv', email)
        Envio('basenovosregistros.csv', email)
