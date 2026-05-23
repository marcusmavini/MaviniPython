import customtkinter as ctk
ctk.set_appearance_mode("Dark") # Janela em DarkMode
ctk.set_default_color_theme("blue")

class MinhaLista(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Minha Lista")
        self.geometry("400x600")

        self.estoque = {
            'Detergente':0,
            'Interfolha':0
        }

root = MinhaLista()
root.mainloop()