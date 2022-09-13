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

        lbl_users = ttk.Label(self, text="Integrantes de Eventos")
        lbl_users.pack(fill=tk.X, padx=15, pady=5)
        self.users = tk.Listbox(self)
        self.users.pack(fill=tk.X, padx=15, pady=5)
        try:
            users = crud.select_all("IntegranteEvento")
        except:
            pass
        for user in users:
            self.users.insert(tk.END, user)

        # create CRUD buttons
        btn_create = ttk.Button(self, text="Criar", command=lambda:CreateIntegranteScr(self))
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:UpdateIntegranteScr(self, self.users.get(self.users.curselection())))
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


class CreateIntegranteScr(tk.Toplevel):
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

        lbl_codigo = ttk.Label(self, text="Código")
        lbl_codigo.pack(fill=tk.X, padx=15, pady=5)
        self.codigo = ttk.Entry(self)
        self.codigo.pack(fill=tk.X, padx=15, pady=5)

        lbl_nome = ttk.Label(self, text="Nome")
        lbl_nome.pack(fill=tk.X, padx=15, pady=5)
        self.nome = ttk.Entry(self)
        self.nome.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_nascimento = ttk.Label(self, text="Data de Nascimento")
        lbl_data_nascimento.pack(fill=tk.X, padx=15, pady=5)
        self.data_nascimento = ttk.Entry(self)
        self.data_nascimento.pack(fill=tk.X, padx=15, pady=5)

        lbl_funcao = ttk.Label(self, text="Função")
        lbl_funcao.pack(fill=tk.X, padx=15, pady=5)
        self.funcao = ttk.Entry(self)
        self.funcao.pack(fill=tk.X, padx=15, pady=5)

        lbl_nome_evento = ttk.Label(self, text="Nome do Evento")
        lbl_nome_evento.pack(fill=tk.X, padx=15, pady=5)
        self.nome_evento = ttk.Entry(self)
        self.nome_evento.pack(fill=tk.X, padx=15, pady=5)

        # create a button to confirm the creation
        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the creation
        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self):
        try:
            # create a new employee
            nome = self.nome.get()
            data_nascimento = self.data_nascimento.get()
            funcao = self.funcao.get()
            codigo = self.codigo.get()
            nome_evento = self.nome_evento.get()

            if nome_evento != "":
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
                crud.create_integrante_evento(codigo, nome, data_nascimento, funcao)
                crud.create_participa(codigo, nome_evento)
                # reload the main screen
                self.master.refresh()
                self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", e)

    def cancel(self):
        self.master.deiconify()
        self.destroy()


class UpdateIntegranteScr(tk.Toplevel):
    def __init__(self, codigo_integrante=None, master=None):
        super().__init__(master=master)
        self.codigo_integrante = codigo_integrante
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

            crud.update_record("IntegranteEvento", table, data, "Codigo", str(self.codigo_integrante))
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