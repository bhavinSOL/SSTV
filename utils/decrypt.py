from cryptography.fernet import Fernet
import base64

def decrypt_image(path, key):
    with open(path, "rb") as f:
        data = f.read()
    cipher = Fernet(base64.urlsafe_b64encode(key.encode().ljust(32)[:32]))
    decrypted = cipher.decrypt(data)
    dec_path = path.replace("_enc", "_dec")
    with open(dec_path, "wb") as f:
        f.write(decrypted)
    return dec_path
