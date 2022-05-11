import shutil
from pathlib import Path
from zipfile import ZipFile
from datetime import date

def descompactar(caminhoorigem,nomearquivo):
    arquivos = Path(fr'{caminhoorigem}').glob('*.zip')
    destino = Path().absolute()
    for arq in arquivos:
        shutil.move(arq, destino)

    arquivo = ZipFile(f'{nomearquivo}','r')
    arquivo.extractall()
    arquivo.close()

if __name__ == '__main__':
    caminho = r'C:\Users\leand\Downloads'
    descompactar(caminho, '202203_BPC.zip')


#lista = str(date.today()).split('-')
#nomeArq = lista[0:2]
#nomeArq = ''.join(nomeArq)
#print(nomeArq)