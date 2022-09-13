from dataclasses import fields
from datetime import datetime
from tkinter import Entry, messagebox
import tkinter.ttk as ttk
import tkinter as tk
import crud

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

        # White label to show all users
        lbl_events = ttk.Label(self, text="Eventos")
        lbl_events.pack(fill=tk.X, padx=15, pady=5)
        # read events with and show them in a listbox
        self.events = tk.Listbox(self)
        self.events.pack(fill=tk.X, padx=15, pady=5)
        # read events from database
        events = crud.select_all("Evento")
        events.sort(key=lambda x:x[2], reverse=True)

        labels = ["Nome", "CodigoAla", "DataInicio", "DataFim", "Descricao", "Instituicao"]
        events.insert(0, labels)

        for event in events:
            self.events.insert(tk.END, event)

        # create CRUD buttons
        btn_create = ttk.Button(self, text="Criar", command=lambda:CreateEventScr(self))
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:self.update())
        btn_update.pack(fill=tk.X, padx=15, pady=5)

        btn_delete = ttk.Button(self, text="Deletar", command=lambda:self.delete())
        btn_delete.pack(fill=tk.X, padx=15, pady=5)

        btn_back = ttk.Button(self, text="Voltar", command=self.destroy)
        btn_back.pack(fill=tk.X, padx=15, pady=5)
        
    def cancel(self):
        self.create_window.destroy()

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
    
    def refresh(self):
        self.destroy()
        self.__init__()


class CreateEventScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.initUI()
        self.master.iconify()

    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Criar")

        # Create inputs:
        lbl_nome = ttk.Label(self, text="Nome")
        lbl_nome.pack(fill=tk.X, padx=15, pady=5)
        self.nome = tk.StringVar()
        txt_nome = ttk.Entry(self, textvariable=self.nome)
        txt_nome.pack(fill=tk.X, padx=15, pady=5)

        lbl_codigo_ala = ttk.Label(self, text="CodigoAla")
        lbl_codigo_ala.pack(fill=tk.X, padx=15, pady=5)
        self.codigo_ala = tk.StringVar()
        txt_codigo_ala = ttk.Entry(self, textvariable=self.codigo_ala)
        txt_codigo_ala.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_inicio = ttk.Label(self, text="DataInicio")
        lbl_data_inicio.pack(fill=tk.X, padx=15, pady=5)
        self.data_inicio = tk.StringVar()
        txt_data_inicio = ttk.Entry(self, textvariable=self.data_inicio)
        txt_data_inicio.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_fim = ttk.Label(self, text="DataFim")
        lbl_data_fim.pack(fill=tk.X, padx=15, pady=5)
        self.data_fim = tk.StringVar()
        txt_data_fim = ttk.Entry(self, textvariable=self.data_fim)
        txt_data_fim.pack(fill=tk.X, padx=15, pady=5)

        lbl_descricao = ttk.Label(self, text="Descricao")
        lbl_descricao.pack(fill=tk.X, padx=15, pady=5)
        self.descricao = tk.StringVar()
        txt_descricao = ttk.Entry(self, textvariable=self.descricao)
        txt_descricao.pack(fill=tk.X, padx=15, pady=5)

        lbl_instituicao = ttk.Label(self, text="Instituicao")
        lbl_instituicao.pack(fill=tk.X, padx=15, pady=5)
        self.instituicao = tk.StringVar()
        txt_instituicao = ttk.Entry(self, textvariable=self.instituicao)
        txt_instituicao.pack(fill=tk.X, padx=15, pady=5)


        # create a button to confirm the creation
        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the creation
        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self):
        try:
            nome = self.nome.get()
            codigo_ala = self.codigo_ala.get()
            data_inicio = self.data_inicio.get()
            data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
            data_fim = self.data_fim.get()
            data_fim = datetime.strptime(data_fim, "%d/%m/%Y")
            descricao = self.descricao.get()
            instituicao = self.instituicao.get()
            crud.insert("Evento", nome, codigo_ala, data_inicio, data_fim, descricao, instituicao)
            self.master.refresh()
            self.destroy()
        except Exception as e:
            # show messagebox with error
            messagebox.showerror("Erro", e)

    def cancel(self):
        self.master.deiconify()
        self.destroy()
        

if __name__ == "__main__":
    root = tk.Tk()
    EventScr(root)
    root.mainloop()