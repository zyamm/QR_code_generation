import qrcode  # Import the package for QR code generation
import qrcode.image.svg  # Import module to save QR code as SVG image


class MakeQR:
    def __init__(self, output):
        self.url = ''  # The initial value of the URL is empty
        self.output = output

    def run(self):
        url = input('Enter URL : ')
        self.url = url
        self.make()

    def make(self):  # Generate and save the QR code image here
        factory = qrcode.image.svg.SvgImage  # Declared to make in SVG format
        img = qrcode.make(self.url, image_factory=factory)
        img.save(self.output)


if __name__ == "__main__":  # True if this module was executed directly
    import sys
    args = sys.argv  # Get command line arguments
    output = args[
        1]  # From the command-line arguments, put the 1st argument to the variable
    app = MakeQR(output)
    app.run()
