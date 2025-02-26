from cryptography.fernet import Fernet
import cv2
import base64
import hashlib

def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def extract_message(image_path: str, password: str):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or invalid.")
    binary_message = ""
    for row in image:
        for pixel in row:
            for i in range(3):
                binary_message += str(pixel[i] & 1)
    byte_chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    extracted_chars = []
    for byte in byte_chunks:
        if byte == "00000000":  # Stop reading at delimiter
            break
        extracted_chars.append(chr(int(byte, 2)))
    extracted_message = ''.join(extracted_chars)
    try:
        extracted_message = base64.b64decode(extracted_message).decode()
        key = generate_key(password)
        cipher = Fernet(key)
        decrypted_message = cipher.decrypt(extracted_message.encode()).decode()
        return decrypted_message
    except Exception:
        return "Decryption failed. Incorrect password or corrupted image."
