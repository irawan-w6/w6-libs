from W6Libs.PyPDF2 import PdfFileReader


def pdf2txt(path):
    # creating a pdf reader object
    pdf_reader = PdfFileReader(path, 'rb')

    # extracting text from page
    pdftext = ""
    for page in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page)
        pdftext += page_obj.extract_text()
    return pdftext
