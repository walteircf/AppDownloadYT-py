import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import threading


# Função para baixar o vídeo
def download_video():
    url = url_entry.get()
    download_folder = folder_path.get()

    if not url or not download_folder:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida e selecione uma pasta.")
        return

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
    }

    try:
        status_label.config(text="Baixando...", fg="blue")

        # Usando thread para evitar congelamento da interface durante o download
        def download():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            status_label.config(text="Download concluído!", fg="green")
            messagebox.showinfo("Sucesso", "Download concluído!")

        threading.Thread(target=download).start()

    except Exception as e:
        status_label.config(text="Erro no download", fg="red")
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


# Função para selecionar a pasta de download
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)


# Configuração da janela principal
root = tk.Tk()
root.title("Download de Vídeos do YouTube")
root.geometry("500x300")
root.resizable(False, False)

# Configuração de fontes e estilos
title_font = ("Arial", 14, "bold")
label_font = ("Arial", 10)
entry_font = ("Arial", 10)
button_font = ("Arial", 10, "bold")

# Título
title_label = tk.Label(root, text="Baixar Vídeos do YouTube", font=title_font, fg="darkblue")
title_label.pack(pady=10)

# Entrada para URL
url_label = tk.Label(root, text="URL do Vídeo:", font=label_font)
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50, font=entry_font)
url_entry.pack(pady=5)

# Seletor de pasta para download
folder_label = tk.Label(root, text="Pasta para salvar:", font=label_font)
folder_label.pack(pady=5)
folder_path = tk.StringVar()
folder_entry = tk.Entry(root, textvariable=folder_path, width=40, font=entry_font, state="readonly")
folder_entry.pack(side=tk.LEFT, padx=5)
folder_button = tk.Button(root, text="Selecionar Pasta", command=select_folder, font=button_font, fg="white",
                          bg="darkgreen")
folder_button.pack(side=tk.LEFT, padx=5)

# Botão de download
download_button = tk.Button(root, text="Baixar", command=download_video, font=button_font, fg="white", bg="darkblue")
download_button.pack(pady=20)

# Status de download
status_label = tk.Label(root, text="", font=label_font)
status_label.pack()

# Inicia a interface gráfica
root.mainloop()
