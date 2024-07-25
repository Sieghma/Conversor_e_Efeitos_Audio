from pydub import AudioSegment
from pyo import *

# Função para converter MP3 para WAV
def converter_mp3_para_wav(arquivo_mp3, arquivo_wav):
    audio = AudioSegment.from_mp3(arquivo_mp3)
    audio.export(arquivo_wav, format="wav")

# Converte o arquivo MP3 para WAV
converter_mp3_para_wav("musica.mp3", "musica.wav")

# Inicializa o servidor de áudio
s = Server().boot()

# Carrega o arquivo de áudio WAV
file = SfPlayer("musica/audio.wav", loop=True).out()

# Adiciona um efeito de delay
delay = Delay(file, delay=0.5, feedback=0.5).out()

# Adiciona um efeito de reverb
reverb = Freeverb(delay, size=0.8, damp=0.5).out()

# Inicia o servidor e abre a GUI
s.start()
s.gui(locals())