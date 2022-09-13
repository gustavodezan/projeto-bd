from dataclasses import fields
from datetime import datetime
from tkinter import ttk, messagebox
import tkinter as tk
import crud

class EmployeeScr(tk.Toplevel):
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
        lbl_users = ttk.Label(self, text="Usuários")
        lbl_users.pack(fill=tk.X, padx=15, pady=5)
        # read users with and show them in a listbox
        self.users = tk.Listbox(self)
        self.users.pack(fill=tk.X, padx=15, pady=5)
        # read users from database
        users = crud.select_all("Funcionario")
        for user in users:
            self.users.insert(tk.END, user)

        # create CRUD buttons
        btn_create = ttk.Button(self, text="Criar", command=lambda:CreateEmployeeScr(self))
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:UpdateFuncionarioScr(self, self.users.get(self.users.curselection())))
        btn_update.pack(fill=tk.X, padx=15, pady=5)

        btn_delete = ttk.Button(self, text="Deletar", command=lambda:self.delete())
        btn_delete.pack(fill=tk.X, padx=15, pady=5)

        btn_back = ttk.Button(self, text="Voltar", command=self.destroy)
        btn_back.pack(fill=tk.X, padx=15, pady=5)
        
    def confirm(self):
        # open the window according to the option
        option = self.options.get(self.options.curselection())
        if option == "Funcionário":
            CreateEmployeeScr(self.create_window)
        elif option == "Cliente":
            pass
        elif option == "Item":
            pass
        else:
            print("Erro")

    def cancel(self):
        self.create_window.destroy()

    def delete(self):
        # abrir tela de deleção
        print("Abrir tela de deleção")
        pass

    def destroy(self):
        self.master.deiconify()
        super().destroy()
    
    def refresh(self):
        self.destroy()
        self.__init__()


class CreateEmployeeScr(tk.Toplevel):
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

        # Create inputs for:
        lbl_matricula = ttk.Label(self, text="Matricula")
        lbl_matricula.pack(fill=tk.X, padx=15, pady=5)
        self.matricula = ttk.Entry(self)
        self.matricula.pack(fill=tk.X, padx=15, pady=5)

        lbl_cpf = ttk.Label(self, text="CPF")
        lbl_cpf.pack(fill=tk.X, padx=15, pady=5)
        self.cpf = ttk.Entry(self)
        self.cpf.pack(fill=tk.X, padx=15, pady=5)

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

        lbl_endereco = ttk.Label(self, text="Endereço")
        lbl_endereco.pack(fill=tk.X, padx=15, pady=5)
        self.endereco = ttk.Entry(self)
        self.endereco.pack(fill=tk.X, padx=15, pady=5)

        lbl_ala = ttk.Label(self, text="Ala")
        lbl_ala.pack(fill=tk.X, padx=15, pady=5)
        self.ala = ttk.Entry(self)
        self.ala.pack(fill=tk.X, padx=15, pady=5)

        # create a button to confirm the creation
        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm(lbl_matricula, lbl_cpf, lbl_nome, lbl_data_nascimento, lbl_funcao, lbl_endereco))
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the creation
        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self, lbl_matricula, lbl_cpf, lbl_nome, lbl_data_nascimento, lbl_funcao, lbl_endereco):
        # create a new employee
        matricula = self.matricula.get()
        cpf = self.cpf.get()
        nome = self.nome.get()
        data_nascimento = self.data_nascimento.get()
        funcao = self.funcao.get()
        endereco = self.endereco.get()
        ala = self.ala.get()
        if matricula == "":
            lbl_matricula.config(foreground="red")
        if cpf == "":
            lbl_cpf.config(foreground="red")
        if nome == "":
            lbl_nome.config(foreground="red")
        if data_nascimento == "":
            lbl_data_nascimento.config(foreground="red")
        if funcao == "":
            lbl_funcao.config(foreground="red")
        if endereco == "":
            lbl_endereco.config(foreground="red")
        if ala != "" and matricula != "" and cpf != "" and nome != "" and data_nascimento != "" and funcao != "" and endereco != "":
            # create a new employee
            data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
            crud.create_funcionario(matricula, cpf, nome, data_nascimento, datetime.now(), funcao, endereco)
            crud.create_trabalha(matricula, ala)
            # reload the main screen
            self.master.refresh()
            self.destroy()
    
    def cancel(self):
        self.master.deiconify()
        self.destroy()
        

class UpdateFuncionarioScr(tk.Toplevel):
    def __init__(self, codigo_funcionario=None, master=None):
        super().__init__(master=master)
        self.codigo_funcionario = codigo_funcionario
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

            try:
                crud.update_record("Funcionario", table, data, "Codigo", str(self.codigo_funcionario))
            except:
                pass
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