from ctypes import alignment
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfiles
import crud
from tela_adm import AdmScr

class MainScr(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.logged = False

    def initUI(self):
        self.master.title("Projeto BD - Login")
        self.master.geometry("640x480")
        style = ttk.Style(self.master)
        style.theme_use("clam")


        self.pack(fill=tk.BOTH, expand=True)

        frame1 = ttk.Frame(self)
        frame1.pack(fill=tk.X)

        # Titulo
        lbl_titulo = ttk.Label(frame1, text="MuseuDB", background="grey", width="300", font=("Arial", 15),anchor=tk.CENTER).pack(pady=30)

        # Campo de usuario
        lbl_texto_usuario = ttk.Label(frame1, text="Usuário (Código de identificação)", font=("Arial", 10))
        lbl_texto_usuario.pack(side=tk.TOP, padx=5, pady=5)
        txt_user = tk.Text(frame1,width=40, height=1)
        txt_user.pack(side=tk.TOP, padx=5, pady=5, expand=True)

        # Campo de senha
        lbl_texto_senha = ttk.Label(frame1, text="Senha", font=("Arial", 10))
        lbl_texto_senha.pack(side=tk.TOP, padx=5, pady=5)
        txt_senha = tk.Text(frame1,width=40, height=1)
        txt_senha.pack(side=tk.TOP, padx=5, pady=5, expand=True)

        # Botao de login
        btn_login = ttk.Button(frame1, text="Login", command=lambda: self.login(txt_user.get("1.0", tk.END),txt_senha.get("1.0", tk.END)))
        btn_login.pack(side=tk.TOP, padx=5, pady=5)

        # # Botao de cadastro
        # btn_cadastro = ttk.Button(frame1, text="Cadastrar", command=lambda: self.cadastro())
        # btn_cadastro.pack(side=tk.TOP, padx=5, pady=5)

        # Exit
        btn_exit = ttk.Button(frame1, text="Sair", command=lambda: self.master.destroy())
        btn_exit.pack(side=tk.TOP, padx=5, pady=5)

    def refresh(self):
        self.destroy()
        self.__init__()

    # User: matricula
    # Password: CPF
    def login(self, user, password):
        user = crud.verifica_login(user.strip(), str(password).strip())
        for x in user:
            print(x)
        if len(user) > 0:
            self.logged = True
            # open adm screen
            AdmScr(username=user[0][2])
            #self.master.destroy()

    
# run
root = tk.Tk()
app = MainScr()
root.mainloop()
