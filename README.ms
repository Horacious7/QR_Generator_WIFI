# QR Code Generator for Wi-Fi

## Description

This Python application generates QR codes for Wi-Fi network credentials using the `qrcode` library and `PyQt5` for the graphical user interface. The generated QR code can be scanned by devices to automatically connect to the specified Wi-Fi network.

## Features

- Input fields for SSID (Wi-Fi network name), encryption type (WPA/WEP), and password.
- Generate a QR code representing the Wi-Fi credentials.
- Display the QR code in the application window.

## Prerequisites

Before running the application, ensure you have the following libraries installed:

- `qrcode`
- `PyQt5`

You can install these libraries using `pip`:

```bash
pip install qrcode[pil] PyQt5
```

## How to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Horacious7/QR_Generator_WIFI.git
   cd qr-code-generator-wifi
   ```

2. **Run the Application**

   Execute the script using Python:

   ```bash
   python qr_code_generator.py
   ```

3. **Using the Application**

   - Open the application.
   - Enter the SSID (name of the Wi-Fi network) in the first input field.
   - Enter the type of encryption (WPA or WEP) in the second input field.
   - Enter the Wi-Fi password in the third input field.
   - Click the "Generate the QR code" button.
   - The QR code will be displayed in the application window and saved as `temporary_qr.png`.

## Code Overview

- **QRCodeGenerator Class**: Defines the main window and layout for the application.
  - `__init__()`: Initializes the UI elements and layout.
  - `generate_qr_code()`: Generates a QR code with the Wi-Fi credentials and displays it in the application window.

- **Main Execution**: Creates an instance of `QApplication`, initializes the `QRCodeGenerator` window, and starts the application event loop.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Contributing

If you have suggestions or improvements, please fork the repository and submit a pull request.

## Contact

For any questions or issues, please contact maierhoratiu7@gmail.com.
