from cryptography.fernet import Fernet
import cv2
import numpy as np
import base64
import hashlib

def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_message(message: str, password: str) -> bytes:
    key = generate_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

def embed_message(image_path: str, message: str, password: str, output_path: str):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or invalid.")
    encrypted_message = encrypt_message(message, password)
    encrypted_message = base64.b64encode(encrypted_message).decode()
    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message)
    binary_message += '00000000'  # Delimiter to mark end of message
    max_bytes = image.size // 8
    if len(binary_message) > max_bytes:
        raise ValueError("Message too large to hide in image.")
    data_index = 0
    for row in image:
        for pixel in row:
            for i in range(3):
                if data_index < len(binary_message):
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])
                    data_index += 1
    cv2.imwrite(output_path, image)
    print("Message hidden successfully.")