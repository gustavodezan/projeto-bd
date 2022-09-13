from tkinter import ttk
import tkinter as tk
from tela_eventos import EventScr
from tela_registros import RegisterScr

class AdmScr(tk.Toplevel):
    def __init__(self, username=None, master=None):
        super().__init__(master=master)
        self.username = username
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Logado como: " + self.username)
        
        # create 3 buttons: view arts, view events, registers
        btn_view_arts = ttk.Button(self, text="Ver museu", command=lambda:self.ver_museu())
        btn_view_arts.pack(fill=tk.X, padx=15, pady=5)

        btn_view_events = ttk.Button(self, text="Ver eventos", command=lambda:self.ver_eventos())
        btn_view_events.pack(fill=tk.X, padx=15, pady=5)

        btn_administer = ttk.Button(self, text="Registros", command=lambda:self.ver_registros())
        btn_administer.pack(fill=tk.X, padx=15, pady=5)

        btn_logout = ttk.Button(self, text="Sair", command=self.destroy)
        btn_logout.pack(fill=tk.X, padx=15, pady=5)

    def ver_museu(self):
        # abrir tela do museu
        print("Abrir tela do museu")
        pass

    def ver_eventos(self):
        # abrir tela de eventos
        print("Abrir tela de eventos")
        pass

    def ver_registros(self):
        # abrir tela de registros
        print("Abrir tela de registros")
        RegisterScr(self)
        pass

    def destroy(self):
        self.master.deiconify()
        super().destroy()

    def refresh(self):
        self.destroy()
        self.__init__()
