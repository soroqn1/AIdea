import tkinter as tk
import time
from tkinter import PhotoImage  

window = tk.Tk()
window.title("AI COMPANION")
window.geometry("640x480")
window.visible = True

button = tk.Button(window, text="Показать/Скрыть", command="")
button.pack(pady=20)

window.attributes('-alpha', 0.8)  # Установить начальную прозрачность фона окна

window.mainloop()