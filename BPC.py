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
meses = navegador.find_elements(By.CSS_SELECTOR,'#links-meses option')
ultimo = meses[-1].text
navegador.find_element(By.CSS_SELECTOR,'#links-meses').send_keys(ultimo)
navegador.find_element(By.CSS_SELECTOR,'#btn').click()
sleep(60)

origem = r'C:\Users\leand\Downloads'
descompactar(origem, '202204_BPC.zip')

tratarbase('202203_BPC.csv', '202204_BPC.csv')

Envio('basenovosexcluidos.csv')
Envio('basenovosregistros.csv')