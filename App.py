import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Por favor, insira uma URL do vídeo.")
        return

    ydl_opts = {
        'format': 'best',  # Melhor qualidade
        'outtmpl': 'C:/Users/wcfre/Downloads/%(title)s.%(ext)s',  # Caminho e formato do arquivo
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criação da janela principal
root = tk.Tk()
root.title("Downloader de Vídeos do YouTube")

# Criação do campo de entrada para a URL
url_label = tk.Label(root, text="Insira a URL do vídeo:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Criação do botão de download
download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

# Executar a aplicação
root.mainloop()
