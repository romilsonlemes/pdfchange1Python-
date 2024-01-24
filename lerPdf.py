import PyPDF2
import re

#pdf_file = open('arquivosPDF/Frances1.pdf', 'rb')
pdf_file = open('arquivosPDF/grammar1.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

print(f'Total de páginas: {pdf_reader.numPages}')  # Pega o numero de páginas

#Imprimir a pagina 1
pagina1 = pdf_reader.getPage(9)

print(pagina1)
#Imprimir conteúdo da página 01
texto_pagina1 = pagina1.extractText()
texto_pagina1 = re.sub('\n', '', texto_pagina1)
print(texto_pagina1)


