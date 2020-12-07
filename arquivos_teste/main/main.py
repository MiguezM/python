import filtra as ft

print("OK, it's all gonna be fine")

arquivo_completo = "C:\\Users\\Mateus\\Desktop\\arquivos\\arquivos_teste\\contratos.csv"

arquivo = ft.le_arquivo(arquivo_completo)
contrato_input = input("digite o contrato para filtrar: ")
arquivo_filtrado = ft.filtra_arquivo(arquivo, "Contrato", contrato_input)

if (ft.verifica_arquivo("C:\\Users\\Mateus\\Desktop\\arquivos\\arquivos_teste\\"  + contrato_input + ".csv")):
    print("arquivo já criado: ", arquivo_filtrado, "\n filtrar outro contrato")
else:
  if (len(filtrado) > 0):
    filtrado.to_csv(arquivo_filtrado, sep = ';', index = False, header = 'column_names')
    print("Fim. Contrato {} adicionado ao arquivo {}. \n Quantidade encontrada {}: ".format(contrato_input, arquivo_filtrado, len(filtrado)))
  else:
    print("Fim. Não foram encontrados registros para este contrato")
