from PyPDF2 import PdfFileReader, PdfFileWriter


class PaginasPdf:
    def __init__(self, pdf_file):
        self.doc = PdfFileReader(pdf_file)
        self.page = -1

    def __len__(self):
        return self.doc.getNumPages()

    def __iter__(self):
        return self

    def __next__(self):
        self.page += 1
        if self.page >= len(self):
            raise StopIteration
        return self.doc.getPage(self.page)

pdf_file_name = "./do-santos/do01062016-Meio Ambiente.pdf"
string_to_find = ["Gadig","Leone "]



if __name__ == "__main__":
    with open(pdf_file_name, "rb") as diario_oficial:
        found = False
        print("Iniciando a pesquisa no pdf {}".format(pdf_file_name))
        for num, page in enumerate(PaginasPdf(diario_oficial)):
            content = page.extractText()
            for s in string_to_find:
                index = content.find(s)
                if index > 0:
                    found = True
                    print("Encontrado o texto {} na página {}".format(s, num+1))
                    output = PdfFileWriter()
                    output.addPage(page)
                    filename = "do_found_{}_pag{}.pdf".format(s, num+1)
                    with open(filename, "wb") as out_f:
                        output.write(out_f)
        print("Pesquisa finalizada.")
        if found:
            print("Foram encontrados resultados. Verificar PDFs gerados.")
        else:
            print("Não foi encontrado nenhuma ocorrência")
