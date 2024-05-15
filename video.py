from pytube import YouTube

pasta = r'D:\Python\Youtube'

url = input('Informe a url: ')

yt = YouTube(url)

resolucao = '1080p'

video = yt.streams.filter(res= resolucao, file_extension= 'mp4').first()

nome = 'teste_video.mp4'

video.download(output_path= pasta, filename= nome)

print('Video baixado com sucesso')