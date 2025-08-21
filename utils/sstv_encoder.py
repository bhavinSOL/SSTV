# import shutil
#
# def image_to_sstv(image_path):
#     # Placeholder: in real use, you'd convert to actual SSTV audio
#     audio_path = image_path.replace(".png", ".wav").replace(".jpg", ".wav")
#     shutil.copy("utils/sample.wav", audio_path)  # simulate SSTV
#     return audio_path



# from pysstv.color import MartinM1
# from PIL import Image
# import numpy as np
# from scipy.io.wavfile import write
#
# def image_to_sstv(image_path):
#     image = Image.open(image_path).convert('RGB').resize((320, 256))
#     sstv = MartinM1(image, 44100, bits=8)
#
#     # Proper float handling and scaling
#     samples = np.array([sample for sample in sstv.gen_samples()], dtype=np.float32)
#     samples = (samples * 32767).astype(np.int16)
#
#     audio_path = image_path.rsplit(".", 1)[0] + "_sstv.wav"
#     write(audio_path, 44100, samples)
#     return audio_path
from pysstv.color import MartinM1
from PIL import Image
import numpy as np
from scipy.io.wavfile import write

def image_to_sstv(image_path):
    image = Image.open(image_path).convert('RGB').resize((320, 256))
    sstv = MartinM1(image, 44100, bits=8)

    samples = np.array([s for i, s in enumerate(sstv.gen_samples()) if i < 44100 * 60], dtype=np.float32)
    samples = (samples * 32767).astype(np.int16)

    audio_path = image_path.rsplit(".", 1)[0] + "_sstv.wav"
    write(audio_path, 44100, samples)
    return audio_path



