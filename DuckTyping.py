#############################################################
# Duck Typing : Concept where Type of OBJECT is determined  #
# ````````````  by its behavior not by it's class .         #
#############################################################
class InkJetPrinter :
    def printDocument(self,document):
        print("InkJEtPrinter Printing :",document)


class LaserPrinter : 
    def printDocument(self,document):
        print("LaserPrinter Printing :",document)
       

class PDFWriter :
    def printDocument(self,document):
        print(f"saving {document} as PDF")

def StartPrinting(Device):
    Device.printDocument("Marvellous Notes")

def main():
    StartPrinting(InkJetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())


main()