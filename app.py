# Python 3
# pip install pyqt5
# pip install PyQtWebEngine

import sys
import argparse
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

# Args parser
parser = argparse.ArgumentParser(description='Convert webpage to PDF')
parser.add_argument('target', metavar='TARGET_URL', type=str,
                    help='target webpage url')
parser.add_argument('--out', dest='output', metavar='FILENAME', type=str,
                    help='output file name (default: converted.pdf)')

args = parser.parse_args()

# Check output filename from argument
output_file_name = 'converted.pdf'
if args.output:
    output_file_name = \
        args.output if args.output.find('.pdf') != -1 else args.output + '.pdf'

# Create PyQt application
app = QtWidgets.QApplication(sys.argv)

# Create web engine
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)

# Load target URL
loader.page().pdfPrintingFinished.connect(loader.close)
loader.load(QtCore.QUrl(args.target))

def create_pdf():
    """
    Save PDF file after webpage load
    """
    loader.page().printToPdf(output_file_name)

loader.loadFinished.connect(create_pdf)

# Execute PyQt app
app.exec()
