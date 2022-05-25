from enviarEmail.envioEmail import Envio
emails = ['leandro.silva@unitfour.com.br','paulo.melo@unitfour.com.br','vinicius.spigariol@unitfour.com.br']
for email in emails:
    Envio('basenovosregistros.csv', email)