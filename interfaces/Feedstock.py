from Feedstock import Feedstock
from tkinter import *
from tkinter import ttk

class Feedstock_interface:
    def __init__(self, frame, option, category):
        self.frame = frame
        self.option = option
        self.category = category

        if self.option == "Estoque":
            feedstock_registers = Feedstock.read(category=self.category)

            ## Set Table
            table = ttk.Treeview(frame)
            table.place(x=0, y=0, relwidth=1)
            table["columns"] = ("id", "name", "brand", "measurement_unity", "quantity", "content", "category", "id_purchase")
            table.column("#0", width=0, stretch=NO)
            table.column("id", anchor=CENTER, width=8)
            table.column("name", anchor=CENTER, width=8)
            table.column("brand", anchor=CENTER, width=8)
            table.column("measurement_unity", anchor=CENTER, width=8)
            table.column("quantity", anchor=CENTER, width=8)
            table.column("content", anchor=CENTER, width=8)
            table.column("category", anchor=CENTER, width=8)
            table.column("id_purchase", anchor=CENTER, width=8)
            table.heading("#0", text="", anchor=CENTER)
            table.heading("id", text="ID", anchor=CENTER)
            table.heading("name", text="Nome", anchor=CENTER)
            table.heading("brand", text="Marca", anchor=CENTER)
            table.heading("measurement_unity", text="Unidade de Medida", anchor=CENTER)
            table.heading("quantity", text="Quantidade", anchor=CENTER)
            table.heading("content", text="Conteúdo", anchor=CENTER)
            table.heading("category", text="Categoria", anchor=CENTER)
            table.heading("id_purchase", text="id_purchase", anchor=CENTER)

            # Inserto into table
            for i, feed in enumerate(feedstock_registers):
                table.insert(parent='',index='end',iid=i,text='', values=feed)

            #feedstock_label = Label(frame, text=feedstock_registers, font=("sans seriff", 25), bg="red")
            #feedstock_label.place(x=0, y=0, relwidth=1)
