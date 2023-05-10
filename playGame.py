import tkinter as tk
import sys
from tkinter.scrolledtext import ScrolledText
import tiktok_game as tik

class ConsoleUI:
    def __init__(self, root):
        self.root = root
        self.text = ScrolledText(root)
        self.text.pack(expand=True, fill='both')
        
        # Redirigir la salida estándar a la interfaz
        sys.stdout = self
        
    def write(self, msg):
        # Agregar el mensaje a la interfaz
        self.text.insert(tk.END, msg)
        self.text.see(tk.END)  # Desplazarse automáticamente hacia abajo
        
    def flush(self):
        # Método necesario para redirigir la salida estándar
        pass
    
board  = tik.Board()


def obtener_valor(board):
    valor = entry.get()
    board.addRow(valor)
    entry.delete(0, tk.END)


# Crear la ventana principal
root = tk.Tk()
root.geometry("570x600")
root.title("Tik-Tok game")
root.bind('<Return>', lambda event: obtener_valor(board))




# Crear la interfaz de la consola
console = ConsoleUI(root)

encabezado = "|    Your guess      |   correct numbers   |   correct positions   | "
console.write(encabezado + "\n")

# Crear la entrada de texto
entry = tk.Entry(root)
entry.pack()

# Crear el botón para obtener el valor
button = tk.Button(root, text="Obtener valor", command=lambda: obtener_valor(board))
button.pack()

# Mostrar la ventana
root.mainloop()