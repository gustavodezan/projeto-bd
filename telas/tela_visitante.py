from dataclasses import fields
from datetime import datetime
from tkinter import ttk, messagebox
import tkinter as tk
import crud

class ClienteScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Registros")

        # White label to show all users
        lbl_users = ttk.Label(self, text="Visitantes")
        lbl_users.pack(fill=tk.X, padx=15, pady=5)
        # read users with and show them in a listbox
        self.users = tk.Listbox(self)
        self.users.pack(fill=tk.X, padx=15, pady=5)
        # read users from database
        users = crud.select_all("Visitante")
        for user in users:
            self.users.insert(tk.END, user)

        # create CRUD buttons
        btn_create = ttk.Button(self, text="Criar", command=lambda:CreateClienteScr(self))
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:UpdateVisitanteScr(self, self.users.get(self.users.curselection())))
        btn_update.pack(fill=tk.X, padx=15, pady=5)

        btn_delete = ttk.Button(self, text="Deletar", command=lambda:self.delete())
        btn_delete.pack(fill=tk.X, padx=15, pady=5)

        btn_back = ttk.Button(self, text="Voltar", command=self.destroy)
        btn_back.pack(fill=tk.X, padx=15, pady=5)
        
    def cancel(self):
        self.create_window.destroy()

    def delete(self):
        # abrir tela de deleção
        crud.delete_record("Visitante", self.users.get(self.users.curselection()))
        pass

    def destroy(self):
        self.master.deiconify()
        super().destroy()
    
    def refresh(self):
        self.destroy()
        self.__init__()


class CreateClienteScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.type = type
        self.fields = fields
        self.initUI()
        self.master.iconify()

    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Criar")

        lbl_cpf = ttk.Label(self, text="CPF")
        lbl_cpf.pack(fill=tk.X, padx=15, pady=5)
        self.cpf = ttk.Entry(self)
        self.cpf.pack(fill=tk.X, padx=15, pady=5)

        lbl_nome = ttk.Label(self, text="Nome")
        lbl_nome.pack(fill=tk.X, padx=15, pady=5)
        self.nome = ttk.Entry(self)
        self.nome.pack(fill=tk.X, padx=15, pady=5)

        lbl_nacionalidade = ttk.Label(self, text="Nacionalidade")
        lbl_nacionalidade.pack(fill=tk.X, padx=15, pady=5)
        self.nacionalidade = ttk.Entry(self)
        self.nacionalidade.pack(fill=tk.X, padx=15, pady=5)

        lbl_tipo_entrada = ttk.Label(self, text="Tipo de entrada")
        lbl_tipo_entrada.pack(fill=tk.X, padx=15, pady=5)
        self.tipo_entrada = ttk.Entry(self)
        self.tipo_entrada.pack(fill=tk.X, padx=15, pady=5)

        lbl_codigo_visita = ttk.Label(self, text="Código da visita")
        lbl_codigo_visita.pack(fill=tk.X, padx=15, pady=5)
        self.codigo_visita = ttk.Entry(self)
        self.codigo_visita.pack(fill=tk.X, padx=15, pady=5)

        # create a button to confirm the creation
        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the creation
        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self):
        # create a new employee
        cpf = self.cpf.get()
        nome = self.nome.get()
        nacionalidade = self.nacionalidade.get()
        tipo_entrada = self.tipo_entrada.get()
        codigo_visita = self.codigo_visita.get()

        if cpf != "" and nome != "" and tipo_entrada != "" and codigo_visita != "":
            crud.create_visitante(cpf, nome, nacionalidade, tipo_entrada)
            crud.create_data_visita(codigo_visita, datetime.now(), cpf)
            # reload the main screen
            self.master.refresh()
            self.destroy()
    
    def cancel(self):
        self.master.deiconify()
        self.destroy()


class UpdateVisitanteScr(tk.Toplevel):
    def __init__(self, codigo_visitante=None, master=None):
        super().__init__(master=master)
        self.codigo_visitante = codigo_visitante
        self.initUI()
        self.master.iconify()

    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Criar")

        # Create inputs:
        lbl_table = ttk.Label(self, text="Insira o dado que quer alterar")
        lbl_table.pack(fill=tk.X, padx=15, pady=5)
        self.table = ttk.Entry(self)
        self.table.pack(fill=tk.X, padx=15, pady=5)

        lbl_data = ttk.Label(self, text="Insira o novo valor")
        lbl_data.pack(fill=tk.X, padx=15, pady=5)
        self.data = ttk.Entry(self)
        self.data.pack(fill=tk.X, padx=15, pady=5)

        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self):
        try:
            table = self.table.get()
            table.lower().capitalize()
            data = self.data.get()

            crud.update_record("Visistante", table, data, "Codigo", str(self.codigo_visitante))
            self.master.refresh()
            self.destroy()
        except Exception as e:
            # show messagebox with error
            messagebox.showerror("Erro", e)

    def cancel(self):
        self.master.deiconify()
        self.destroy()

    def refresh(self):
        self.destroy()
        self.__init__()