from google.colab import drive
drive.mount('/content/drive')

from pydub import AudioSegment
from IPython.display import Audio, display

maindir = "/content/drive/MyDrive/TTS_2/sounds/"

text = "she is a good girl"

combined = AudioSegment.empty()
res = text.split()

files = []
file = open("/content/drive/MyDrive/TTS_2/audio_text.txt","r")

for words in file:
  sounds=words
  for ss in res:
    if ss in sounds:
      xx = AudioSegment.from_wav(maindir + ss + '.wav')
      files.extend(xx)
    else:
      pass

for fname in files:
  combined += fname

for i, ele in enumerate(files):
  f_name = '/content/drive/MyDrive/TTS_2/gen/' + "{0}.wav".format(i)

combined.export(f_name, format="wav")
display(Audio(f_name, autoplay=True))
