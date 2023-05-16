import tkinter as tk
import sys
from tkinter.scrolledtext import ScrolledText
import tiktok_game as tik

class ConsoleUI:
    def __init__(self, root):
        self.root = root
        self.text = ScrolledText(root)
        self.text.pack(expand=True, fill='both')
        
        # Redirect standard output (console) to interface
        sys.stdout = self
        
    def write(self, msg):
        self.text.insert(tk.END, msg)
        self.text.see(tk.END)
        
    def flush(self):
        pass
    
board  = tik.Board()


def get_value(board):
    valor = entry.get()
    board.addRow(valor)
    entry.delete(0, tk.END)


# Create the main windows
root = tk.Tk()
root.geometry("570x600")
root.title("Tik-Tok game")
root.bind('<Return>', lambda event: get_value(board))




# Create the consle interface
console = ConsoleUI(root)

encabezado = "|    Your guess      |   correct numbers   |   correct positions   | "
console.write(encabezado + "\n")

# Create the text entry
entry = tk.Entry(root)
entry.pack()

# Generate a button for introduce a value
button = tk.Button(root, text="Get Value", command=lambda: get_value(board))
button.pack()


root.mainloop()