from tkinter import ttk
import tkinter as tk
from telas.tela_eventos import EventScr
from telas.tela_funcionarios import EmployeeScr
from telas.tela_artes import ArtesScr
from telas.tela_visitante import ClienteScr

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
        
        # Botoes
        btn_view_arts = ttk.Button(self, text="Museu", command=lambda:self.ver_museu())
        btn_view_arts.pack(fill=tk.X, padx=15, pady=5)

        btn_view_events = ttk.Button(self, text="Eventos", command=lambda:self.abrir_eventos())
        btn_view_events.pack(fill=tk.X, padx=15, pady=5)

        btn_administer = ttk.Button(self, text="Funcionarios", command=lambda:self.abrir_funcionarios())
        btn_administer.pack(fill=tk.X, padx=15, pady=5)

        btn_visitantes = ttk.Button(self, text="Visitantes", command=lambda:self.abrir_visitantes())
        btn_visitantes.pack(fill=tk.X, padx=15, pady=5)

        btn_logout = ttk.Button(self, text="Sair", command=self.destroy)
        btn_logout.pack(fill=tk.X, padx=15, pady=5)

    def ver_museu(self):
        # abrir tela do museu
        print("Abrir tela do museu")
        ArtesScr(self)
        pass

    def abrir_eventos(self):
        # abrir tela de eventos
        print("Abrir tela de eventos")
        EventScr(self)
        pass

    def abrir_funcionarios(self):
        # abrir tela de registros
        print("Abrir tela de registros")
        EmployeeScr(self)
        pass

    def abrir_visitantes(self):
        # abrir tela de registros
        print("Abrir tela de registros")
        ClienteScr()
        pass

    def destroy(self):
        self.master.deiconify()
        super().destroy()

    def refresh(self):
        self.destroy()
        self.__init__()
