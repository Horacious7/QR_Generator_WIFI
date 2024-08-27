import sys
import qrcode
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Generator for Wi-Fi")
        self.layout = QVBoxLayout()
        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.qr_label)

        self.ssid_input = QLineEdit()
        self.ssid_input.setPlaceholderText("Enter the SSID (name of the Wi-Fi network)")
        self.layout.addWidget(self.ssid_input)

        self.encryption_input = QLineEdit()
        self.encryption_input.setPlaceholderText("Enter the type of encryption (WPA/WEP)")
        self.layout.addWidget(self.encryption_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter the password of the Wi-Fi network")
        self.layout.addWidget(self.password_input)

        self.generate_button = QPushButton("Generate the QR code")
        self.generate_button.clicked.connect(self.generate_qr_code)
        self.layout.addWidget(self.generate_button)

        self.setLayout(self.layout)

    def generate_qr_code(self):
        ssid = self.ssid_input.text()
        encryption = self.encryption_input.text()
        password = self.password_input.text()

        if ssid and encryption and password:
            wifi_string = f"WIFI:S:{ssid};T:{encryption};P:{password};;"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=13,
                border=4,
            )
            qr.add_data(wifi_string)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            img.save("temporary_qr.png")

            pixmap = QPixmap("temporary_qr.png")
            self.qr_label.setPixmap(pixmap)
            self.qr_label.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeGenerator()
    window.show()
    sys.exit(app.exec_())
