from tkinter import ttk
import tkinter as tk

class EventScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Registros")

        # Show all events
        btn_create = ttk.Button(self, text="Criar", command=lambda:self.create())
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        # create CRUD buttons
        btn_create = ttk.Button(self, text="Criar", command=lambda:self.create())
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:self.update())
        btn_update.pack(fill=tk.X, padx=15, pady=5)

        btn_delete = ttk.Button(self, text="Deletar", command=lambda:self.delete())
        btn_delete.pack(fill=tk.X, padx=15, pady=5)

        btn_back = ttk.Button(self, text="Voltar", command=self.destroy)
        btn_back.pack(fill=tk.X, padx=15, pady=5)

    def create(self):
        # abrir tela de criação
        print("Abrir tela de criação")
        pass

    def read(self):
        # abrir tela de leitura
        print("Abrir tela de leitura")
        pass

    def update(self):
        # abrir tela de atualização
        print("Abrir tela de atualização")
        pass

    def delete(self):
        # abrir tela de deleção
        print("Abrir tela de deleção")
        pass

    def destroy(self):
        self.master.deiconify()
        super().destroy()


if __name__ == "__main__":
    root = tk.Tk()
    EventScr(root)
    root.mainloop()