import os
import logging

def excluir():
    arquivo_excel = r'C:\Users\weslei.jesus\Documents\Downloads\IMAGENS PARA APAGAR.txt'
    caminho_arq = r'Z:\UNILIDER\Trade\TRADE UNILIDER\2022\3-Comunicação\3.7 - E-COMMERCE\IMAGENS\Final'
    old = os.listdir(caminho_arq)

    with open(arquivo_excel, 'r', encoding='UTF-8') as  file_ex:
        print(file_ex)
        
        for linha in file_ex:
            linha = linha.replace('\n', '')
            try:

                os.remove(caminho_arq + '\\' + linha)
                print('Arqivo excluido')
                logging.info('Arqivo excluido')
            except Exception as erro:
                logging.warning(erro)
                continue

if __name__ == "__main__":
    log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'# Configuracao de logs
    logging.basicConfig(filename='excluir_arq.log',
                        filemode='a',
                        level=logging.INFO,
                        format=log_format,
                        encoding='UTF-8')
    excluir()