#!/usr/bin/python

import PyPDF2 as pdfreader


class PdfReader:
    def __init__(self, filename):
        self.filename = filename


    def get_content(self):

        with open(self.filename, 'wb') as pdf_file:

            file_buff = pdf_file
            if file_buff:
                pdf_buff = pdfreader.PdfFileReader(file_buff)
                page_nums = pdf_buff.numPages
                for i in range(page_nums):
                    if i < 6:
                        yield pdf_buff.getPage(i).extractText()
            pdf_file.close()
        finally:
            pdf_file.close()


def unittest():
    pdfreader = PdfReader(pdf_file)
    assert pdfreader.filename == pdf_file
    print "--test 1 passed--"
    assert pdfreader.get_content()
    print "--test 2 passed--"
    for i in pdfreader.get_content():
        print i


if __name__ == "__main__":
    unittest()
