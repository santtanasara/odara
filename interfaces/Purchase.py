from tkinter import *
from tkinter import ttk, messagebox
from Purchases import Purchases
from Suplier import Suplier
from Config import Config

class Purchase_Interface:
    def __init__(self, frame, option, category_option):
        self.frame = frame
        self.option = option
        self.category_option = category_option
        self.new_purchase_window = None
        self.product_name = StringVar()
        self.brand_name = StringVar()
        self.measurement_unity = StringVar()
        self.content = DoubleVar()
        self.suplier_option = StringVar()
        self.suplier_option.set("Fornecedores")
        self.registered_supliers = {sup[1]: sup[0] for sup in Suplier.read()} #k = name: v = id
        self.supliers_list = list(self.registered_supliers.keys())
        self.price = StringVar()
        self.quantity = StringVar()
        self.expiration_date = StringVar()
        self.new_purchase_category = StringVar()
        self.new_purchase_category.set("Categoria")
        self.registered_categories = self.get_categories()


        if self.option == 'Registrar Compra':
            self.new_purchase_window = Toplevel()
            self.new_purchase_window.attributes('-topmost', 'true')

            Label(self.new_purchase_window, text="Registro de um a nova Compra").grid(row=0, column=0,
                                                                                      columnspan=4, pady=30)

            #Product Name
            Label(self.new_purchase_window, text="Nome do Produto").grid(row=1, column=0)
            self.product_name = Entry(self.new_purchase_window, width=50)
            self.product_name.grid(row=1, column=1, padx=30)

            #Brand Name
            Label(self.new_purchase_window, text="Marca do Produto").grid(row=1, column=2)
            self.brand_name = Entry(self.new_purchase_window, width=50)
            self.brand_name.grid(row=1, column=3, padx=30)

            #Measurement unity
            Label(self.new_purchase_window, text="Unidade de Medida").grid(row=2, column=0)
            self.measurement_unity = Entry(self.new_purchase_window, width=50)
            self.measurement_unity.grid(row=2, column=1, padx=30)

            #Content
            Label(self.new_purchase_window, text="Conteúdo (Apenas Números)").grid(row=2, column=2)
            self.content = Entry(self.new_purchase_window, width=50)
            self.content.grid(row=2, column=3, padx=30)

            #Suplier
            Label(self.new_purchase_window, text="Fornecedor").grid(row=3, column=0)
            suplier_option_menu = OptionMenu(self.new_purchase_window, self.suplier_option, *self.supliers_list)
            suplier_option_menu.grid(row=3, column=1, padx=30)

            #Price
            Label(self.new_purchase_window, text="Preço Total").grid(row=4, column=0)
            self.price = Entry(self.new_purchase_window, width=50)
            self.price.grid(row=4, column=1, padx=30)

            #Quantity
            Label(self.new_purchase_window, text="Quantidade").grid(row=4, column=2)
            self.quantity = Entry(self.new_purchase_window, width=50)
            self.quantity.grid(row=4, column=3, padx=30)

            #Expiration Date
            Label(self.new_purchase_window, text="Data de Validade (YYYY-MM-DD)").grid(row=5, column=0)
            self.expiration_date = Entry(self.new_purchase_window, width=50)
            self.expiration_date.grid(row=5, column=1, padx=30)

            #Category
            Label(self.new_purchase_window, text="Categoria").grid(row=5, column=2)
            purchase_category_menu = OptionMenu(self.new_purchase_window, self.new_purchase_category,
                                                *self.registered_categories)
            purchase_category_menu.grid(row=5, column=3, padx=30)


            Button(self.new_purchase_window, text="Registrar", command=self.register_new_purchase).grid(row=6, column=0,
                                                                                                   columnspan=4, pady=20)

        elif self.option == "Ver Compras":
            purchases, columns = Purchases.read(category=self.category_option)
            purchases_list = []
            for row in purchases:
                purchases_list.append(dict(zip(columns, row)))
            print(purchases_list)

            table = ttk.Treeview(frame)
            table.place(x=0, y=0, relwidth=1)
            table["columns"] = ("Fornecedor", "Produto", "Marca", "Unidade de Medida", "Conteúdo",
                                "Preço Total", "Preço da Unidade", "Quantidade",
                                "Data de Validade", "Data da Compra")
            table.column("#0", width=0, stretch=NO)
            table.column("Fornecedor", anchor=CENTER, width=8)
            table.column("Produto", anchor=CENTER, width=8)
            table.column("Marca", anchor=CENTER, width=8)
            table.column("Unidade de Medida", anchor=CENTER, width=8)
            table.column("Conteúdo", anchor=CENTER, width=8)
            table.column("Preço Total", anchor=CENTER, width=8)
            table.column("Preço da Unidade", anchor=CENTER, width=8)
            table.column("Quantidade", anchor=CENTER, width=8)
            table.column("Data de Validade", anchor=CENTER, width=8)
            table.column("Data da Compra", anchor=CENTER, width=8)
            table.heading("#0", text="", anchor=CENTER)
            table.heading("Fornecedor", text="Fornecedor", anchor=CENTER)
            table.heading("Produto", text="Produto", anchor=CENTER)
            table.heading("Marca", text="Marca", anchor=CENTER)
            table.heading("Unidade de Medida", text="Unidade de Medida", anchor=CENTER)
            table.heading("Conteúdo", text="Conteúdo", anchor=CENTER)
            table.heading("Preço Total", text="Preço Total", anchor=CENTER)
            table.heading("Preço da Unidade", text="Preço da Unidade", anchor=CENTER)
            table.heading("Quantidade", text="Quantidade", anchor=CENTER)
            table.heading("Data de Validade", text="Data de Validade", anchor=CENTER)
            table.heading("Data da Compra", text="Data da Compra", anchor=CENTER)

            for i, pur in enumerate(purchases_list):
                table.insert(parent='', index='end', iid=i, text='', values=[pur["name"], pur["f_name"], pur["brand"],
                                                                             pur["measurement_unity"], pur["content"],
                                                                             pur["price"],
                                                                             pur["unity_price"], pur["quantity"],
                                                                             pur["expiration_date"], pur["buying_date"]])
    def get_categories(self):
        config = Config()
        conn, cursor = config.get_client_sqlite()
        cursor.execute("""
            SELECT * FROM category
        """)

        result = cursor.fetchall()
        config.disconnect_sqlite()
        return [i[0] for i in result]


    def register_new_purchase(self):
        try:
            if not self.product_name.get() or not self.brand_name.get() or not self.measurement_unity.get() \
                    or not self.content.get() or not self.price.get() or not self.quantity.get():
                messagebox.showwarning("Formulário Inválido", "Por favor insira todos os valores.")
                return

            feedstock = {
                "name": self.product_name.get(),
                "brand": self.brand_name.get(),
                "measurement_unity": self.measurement_unity.get(),
                "content": float(self.content.get())
            }

            price_cleaned = self.price.get()
            price_cleaned = float(price_cleaned.replace("R", "").replace("r", "").replace("$", "").replace(",", "."))

            unity_price = price_cleaned / int(self.quantity.get())

            new_purchase = Purchases(feedstock, self.registered_supliers[self.suplier_option.get()],
                                     price_cleaned, int(self.quantity.get()), unity_price,
                                     self.expiration_date.get(), self.new_purchase_category.get())

            if new_purchase.create():
                messagebox.showinfo("Sucesso", "Compra inserida com sucesso")
                self.__init__(self.frame, "Ver Compras", self.category_option)
                self.__init__(self.frame, self.option, self.category_option)
            else:
                messagebox.showerror("Erro", "Não foi possível inserir nova compra. Contate o suporte")
                return

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao tentar inserir nova compra... Erro: {str(e)}")
            return

