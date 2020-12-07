import pandas as pd
import os

arquivo_completo = "C:\\Users\\Mateus\\Desktop\\arquivos\\arquivos_teste\\contratos.csv"

contrato_input = input("digite o contrato para filtrar: ")
arquivo_filtrado = "C:\\Users\\Mateus\\Desktop\\arquivos\\arquivos_teste\\"  + contrato_input + ".csv"

contratos = pd.read_csv(arquivo_completo ,sep = ";")

filtrado = contratos.query('Contrato == @contrato_input')

arquivo_ja_existe = os.path.isfile(arquivo_filtrado)

if arquivo_ja_existe :
  #filtrado.to_csv(arquivo_filtrado, sep = ';', index = False,mode = 'a' , header = False)
  print("arquivo já criado: ", arquivo_filtrado , "\n filtrar outro contrato")
else:
  if (len(filtrado) > 0):
    filtrado.to_csv(arquivo_filtrado, sep = ';', index = False, header = 'column_names')
    print("Fim. Contrato {} adicionado ao arquivo {}. \n Quantidade encontrada {}: ".format(contrato_input, arquivo_filtrado, len(filtrado)))
  else:
    print("Fim. Não foram encontrados registros para este contrato")
