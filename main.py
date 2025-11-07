import tkinter, sys, os, re;
from moviepy.editor import *
from pytubefix import YouTube
from pytubefix.cli import on_progress

def caminho_recursos(caminho_relativo):
    try:
        caminho_arquivos = sys._MEIPASS;
    except Exception:
        caminho_arquivos = os.path.abspath(".");
    return os.path.join(caminho_arquivos, caminho_relativo);

def remover_caracteres_proibidos(title):
    return re.sub(r'[<>:"/\\|?*]', '', title)

app = tkinter.Tk();

app.geometry("500x500");
app.title("Youtube Converter");
app.iconbitmap(caminho_recursos("ícone.ico")); 

def downloadMP3(titulo, caminho):
    try:
        video = VideoFileClip(fr'{caminho}.mp4')
        
        novo_caminho = os.path.join(r"C:\Users\wesley\Music", titulo)
        
        video.audio.write_audiofile(fr'{novo_caminho}.mp3')

        video.close()

        os.remove(fr"{caminho}.mp4")
    except Exception:
        texto = tkinter.Label(app, text="deu algum erro aí lek")
        texto.pack(pady=50)

def downloadedMP4():
    link = label.get()
    
    yt = YouTube(link, on_progress_callback=on_progress)
    
    texto = tkinter.Label(app, text=yt.title)
    texto.pack(pady=30)

    titulo = remover_caracteres_proibidos(yt.title)
    print(titulo)

    ys = yt.streams.get_lowest_resolution()
    ys.download(r"C:\Users\wesley\Music")

    caminho = os.path.join(r"C:\Users\wesley\Music", titulo)

    downloadMP3(titulo, caminho)


label = tkinter.Entry(app, width=30)
label.pack(pady=20, padx=100);

button = tkinter.Button(app, text=f"Clique", command=downloadedMP4);
button.pack(pady=10, padx=100);

app.mainloop();

