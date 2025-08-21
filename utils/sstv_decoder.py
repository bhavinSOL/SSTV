import shutil

def sstv_to_image(audio_path):
    # Placeholder: in real use, decode SSTV audio to image
    img_path = audio_path.replace(".wav", ".jpg")
    shutil.copy("utils/sample_enc.jpg", img_path)  # simulate decoded image
    return img_path
