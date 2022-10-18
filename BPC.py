from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from zip import descompactar
from tratamentoBase import tratarbase
from enviarEmail.envioEmail import Envio
url = 'https://www.portaltransparencia.gov.br/download-de-dados/bpc'
navegador = Firefox()
navegador.get(url)
sleep(1)
meses = navegador.find_elements(By.CSS_SELECTOR, '#links-meses option')
ultimo = meses[-1].text
if ultimo == 'AGOSTO':
    ultimo = 'AA'
if ultimo == 'JULHO':
    ultimo = 'JJ'
navegador.find_element(By.CSS_SELECTOR, '#links-meses').send_keys(ultimo)
sleep(2)
navegador.find_element(By.CSS_SELECTOR, '#btn').click()
sleep(90)
navegador.quit()

origem = r'C:/Users/leandro.silva/Downloads'
descompactar(origem, '202208_BPC.zip')

tratarbase('202207_BPC.csv', '202208_BPC.csv')

emails = ['leandro.silva@unitfour.com.br',
          'vinicius.spigariol@unitfour.com.br']
for email in emails:
    Envio('basenovosexcluidos.csv', email)
    Envio('basenovosregistros.csv', email)
    Envio('BaseBeneficiosAlterados.csv', email)