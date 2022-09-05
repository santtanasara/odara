from Suplier import Suplier
from tkinter import *
from tkinter import ttk, messagebox


class Suplier_Interface:

    def __init__(self, frame):
        self.frame = frame
        self.suplier_name = StringVar()
        self.suplier_website = StringVar()
        self.suplier_window = None

        suplier_registries = Suplier.read()

        table = ttk.Treeview(frame)
        table.place(x=0, y=0, relwidth=1)
        table["columns"] = ("id", "name", "website")
        table.column("#0", width=0, stretch=NO)
        table.column("id", anchor=CENTER, width=8)
        table.column("name", anchor=CENTER, width=8)
        table.column("website", anchor=CENTER, width=8)
        table.heading("#0", text="", anchor=CENTER)
        table.heading("id", text="ID", anchor=CENTER)
        table.heading("name", text="Nome", anchor=CENTER)
        table.heading("website", text="Web Site", anchor=CENTER)

        for i, feed in enumerate(suplier_registries):
            table.insert(parent='',index='end',iid=i,text='', values=feed)


        register_suplier = Button(frame, text="Registrar Novo Fornecedor", bg="yellow", command=self.create_new_suplier)
        register_suplier.place(x=400, y=400)

    def register(self):
        try:
            if self.suplier_name.get() and self.suplier_website.get():
                new_suplier = Suplier(name=self.suplier_name.get(), website=self.suplier_website.get())
                new_suplier.create()
                self.suplier_window.destroy()
                self.__init__(self.frame)

            else:
                messagebox.showwarning(title="Dados incorretos", message="Por favor, insira todos os dados")
                self.suplier_window.force_focus()
        except:
            return

    def create_new_suplier(self):

        self.suplier_window = Toplevel()
        self.suplier_window.attributes('-topmost', 'true')
        Label(self.suplier_window, text="Registro de um novo Fornecedor").grid(row=0, column=0, columnspan=2)

        Label(self.suplier_window, text="Nome do Fornecedor").grid(row=1, column=0)
        Label(self.suplier_window, text="Site do Fornecedor").grid(row=2, column=0)

        self.suplier_name = Entry(self.suplier_window, width=50)
        self.suplier_name.grid(row=1, column=1, padx=30)
        self.suplier_website = Entry(self.suplier_window, width=50)
        self.suplier_website.grid(row=2, column=1, padx=30)

        Button(self.suplier_window, text="Registrar", command=self.register).grid(row=3, column=1)