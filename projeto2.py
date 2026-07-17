## ORGANIZADOR DE ARQUIVOS DO MEU COMPUTADOR - O segundo projeto é uma automação para organizar arquivos com Python. A ideia desse projeto é que você consiga separar arquivos do mesmo tipo em pastas.
import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
}

for arquivo in lista_arquivos:
    # 01. Arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")