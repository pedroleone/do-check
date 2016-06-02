from PyPDF2 import PdfFileReader, PdfFileWriter

string_to_find = ["Gadig","Leone "]
pdf_file_name = "do.pdf"

with open(pdf_file_name, "rb") as do:
    pages_found = []
    pdfDoc = PdfFileReader(do)
    found = False
    print("Iniciando a pesquisa no pdf {}".format(pdf_file_name))
    for i in range(0, pdfDoc.getNumPages()):
        content = pdfDoc.getPage(i).extractText()
        for s in string_to_find:
            index = content.find(s)
            if index > 0:
                found = True
                print("Encontrado o texto {} na página {}".format(s, i+1))
                output = PdfFileWriter()
                output.addPage(pdfDoc.getPage(i))
                filename = "do_found_{}_pag{}.pdf".format(s, i+1)
                with open(filename, "wb") as out_f:
                    output.write(out_f)
    print("Pesquisa finalizada.")
    if found:
        print("Foram encontrados resultados. Verificar PDFs gerados.")
    else:
        print("Não foi encontrado nenhuma ocorrência")
