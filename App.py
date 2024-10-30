import yt_dlp

# URL do vídeo que você deseja baixar
url = 'https://www.youtube.com/watch?v=ryP3W5e7m5Y'  # Substitua pelo link do vídeo

ydl_opts = {
    'format': 'best',  # Melhores qualidade
    'outtmpl': 'C:/Users/wcfre/Downloads/%(title)s.%(ext)s',  # Caminho e formato do arquivo
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
