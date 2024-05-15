from pytube import YouTube

pasta = r'D:\Python\Youtube'
url = input('Informe o link: ')

yt = YouTube(url)

audio = yt.streams.filter(only_audio=True).first()

nome_arquivo = 'Teste.mp3'

audio.download(output_path= pasta, filename= nome_arquivo)

print('Audio baixado com sucesso')