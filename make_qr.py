import qrcode  # Import the package for QR code generation
import qrcode.image.svg  # Import module to save QR code as SVG image


class MakeQR:
    def __init__(self):
        self.url = 'https://www/python.org'
        self.output = 'python.svg'

    def make(self):  # Generate and save the QR code image here
        factory = qrcode.image.svg.SvgImage  # Declared to make in SVG format
        img = qrcode.make(self.url, image_factory=factory)
        img.save(self.output)


if __name__ == "__main__":  # True if this module was executed directly
    app = MakeQR()
    app.make()
