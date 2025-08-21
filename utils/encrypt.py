from cryptography.fernet import Fernet
import base64

def encrypt_image(path, key):
    with open(path, "rb") as f:
        data = f.read()
    cipher = Fernet(base64.urlsafe_b64encode(key.encode().ljust(32)[:32]))
    encrypted = cipher.encrypt(data)
    enc_path = path.replace(".", "_enc.")
    with open(enc_path, "wb") as f:
        f.write(encrypted)
    return enc_path
# from pysstv.color import MartinM1
# from PIL import Image
# import numpy as np
# from scipy.io.wavfile import write
#
# img = Image.new("RGB", (320, 256), (255, 255, 255))  # white image
# sstv = MartinM1(img, 44100, bits=8)
# samples = np.array([s for i, s in enumerate(sstv.gen_samples()) if i < 44100 * 60], dtype=np.float32)
# samples = (samples * 32767).astype(np.int16)
# write("test_sstv.wav", 44100, samples)

