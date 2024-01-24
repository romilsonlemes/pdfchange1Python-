import PyPDF2
import os
import time

pdf_file1 = open('arquivosPDF/Frances1.pdf', 'rb')
pdf_file2 = open('arquivosPDF/grammar1.pdf', 'rb')

#Lendo os dados do Binario que sao de PDF
pdf_reader1 = PyPDF2.PdfFileReader(pdf_file1)
pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)
escritor = PyPDF2.PdfFileWriter()

print(f'Total de páginas do pdf_reader1 : {pdf_reader1.numPages}')  # Pega o numero de páginas
print(f'Total de páginas do pdf_reader2 : {pdf_reader2.numPages}')  # Pega o numero de páginas

#Declarando um objeto do tipo Merge
merge = PyPDF2.PdfFileMerger()

pdf_reader1_Page = pdf_reader1.getPage(10)
pdf_reader2_Page = pdf_reader2.getPage(10)

# print(pdf_reader2_Page10)
arqMergeado = 'outputPDF/ArquivoSaidaMergeado.pdf'
os.system(f"rm -rf {arqMergeado}")
time.sleep(5) # Espera em segundos

print(f'Gerando o arquivo Mergeado: {arqMergeado}')

escritor.addPage(pdf_reader1_Page)
escritor.addPage(pdf_reader2_Page)
with open(arqMergeado, 'wb') as arquivo_saida:
    escritor.write(arquivo_saida)


#merge.append(pdf_reader1_Page10, import_bookmarks=False)
"""""
merge.append(pdf_reader2_Page10, import_bookmarks=False)

merge.append(pdf_reader1, import_bookmarks=False)
merge.append(pdf_reader2, import_bookmarks=False)

arqMergeado = 'outputPDF/ArquivoSaidaMergeado3.pdf'
merge.write(arqMergeado)
merge.close()

#Pegar Informaçoes do Arquivo Mergeado
pdf_file_mergeado = open(arqMergeado, 'rb')
pdf_reader_mergeado = PyPDF2.PdfFileReader(pdf_file_mergeado)

print(f'Total de páginas do Mergeado : {pdf_reader_mergeado.numPages}')  # Pega o numero de páginas
"""""