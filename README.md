# Image Steganography

## Problem Statement
This project aims to securely hide and retrieve secret messages within images using **steganography** and **encryption**. The tool provides a **user-friendly GUI** to facilitate message embedding and extraction with password protection. It ensures **secure communication** by encrypting messages before hiding them in images. Users can decrypt the message only with the correct password, ensuring confidentiality and security.

## Features
- **Encrypt Messages:** Hide a secret message inside an image using a password.
- **Decrypt Messages:** Extract the hidden message from an image using the correct password.
- **Secure Encryption:** Uses AES-based encryption (`cryptography` library) to protect messages.
- **User-Friendly GUI:** A split-screen interface for encryption and decryption.
- **Error Handling:** Provides feedback on incorrect passwords or corrupted images.

## Installation
### Prerequisites
Ensure you have Python installed (>=3.6) and install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage
### Running the GUI
```sh
python main.py
```

### Encrypt a Message
1. Enter your secret message.
2. Enter a password.
3. Select an image to embed the message.
4. Choose an output filename for the encrypted image.
5. Click **Encrypt** to hide the message.

### Decrypt a Message
1. Select an encrypted image.
2. Enter the correct password.
3. Click **Decrypt** to reveal the hidden message.

## Dependencies
- `cryptography`
- `opencv-python`
- `numpy`
- `tkinter`

Install dependencies using:
```sh
pip install -r requirements.txt
```

![Screenshot 2025-02-26 181219](https://github.com/user-attachments/assets/f2d3bcf5-bdee-4a54-aadf-e6fe1cc4c573)
![Screenshot 2025-02-26 181252](https://github.com/user-attachments/assets/9f73cf37-3002-4e07-97d8-4aadbbc538f2)
![Screenshot 2025-02-26 181633](https://github.com/user-attachments/assets/4f4d6292-467b-4b9a-8596-a601987ad4da)
![Screenshot 2025-02-26 181651](https://github.com/user-attachments/assets/6f21a33f-37a8-45e5-967d-16d62e8965a8)



