import pandas as pd
import os

def le_arquivo(nome_arquivo):
  return pd.read_csv(nome_arquivo ,sep = ";")

def grava_arquivo(dados, termo_buscado):
  nome_arquivo = "C:\\Users\\Mateus\\Desktop\\arquivos\\arquivos_teste\\"  + termo_buscado + ".csv"
  return dados.to_csv(nome_arquivo, sep = ';', index = False, header = 'column_names')

def filtra_arquivo(arquivo, termo_buscado, coluna):
  return arquivo.query('@coluna == @termo_buscado')

def verifica_arquivo(arquivo):
  return os.path.isfile(arquivo)


  

  
