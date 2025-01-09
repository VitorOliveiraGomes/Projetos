import tkinter as tk
import time

def atualizar_relogio():
    
    hora_atual = time.strftime('%H:%M:%S')
    
    label.config(text=hora_atual)
    
    janela.after(1000, atualizar_relogio)

janela = tk.Tk()
janela.title("Relógio")

label = tk.Label(janela, font=('calibri', 40, 'bold'), background= 'white', foreground= 'black')
label.pack(anchor='center')

atualizar_relogio()

janela.mainloop()