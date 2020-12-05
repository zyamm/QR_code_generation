# QR_code_generation
This is the command line application to generate QR code.


When you enter the URL, a QR code image with any file name will be generated in the executed directory.
Output uses SVG format.
Using a third party package 'qrcode'.


Assumed operating environment:
  Works with Python 3.6 and above
  OS does not matter
  Modern browser that can display SVG


When running on the command line, type:　
$ python make_qr.py (command line argument)

Enter the name of the output image file in ().
Example:
$ python make_qr.py python.svg
