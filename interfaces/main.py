from tkinter import *
from tkinter import ttk
from interfaces.Feedstock import Feedstock_interface

##Variáveis iniciais
category_option = "Sabonete"

def run():
    root = Tk()
    root.title("Odara Nature")
    root.geometry("1000x600")

    def set_category(option):
        global category_option
        global soap_button
        global candle_button

        category_option = option

        if option == "Sabonete":
            soap_button = Button(root, text="Sabonetes", bg= "green",command=lambda: set_category("Sabonete"))
            soap_button.place(x=800, y=35)

            candle_button = Button(root, text="Velas", bg="gray",command=lambda: set_category("Vela"))
            candle_button.place(x=870, y=35)

        elif option == "Vela":
            soap_button = Button(root, text="Sabonetes", bg= "gray",command=lambda: set_category("Sabonete"))
            soap_button.place(x=800, y=35)

            candle_button = Button(root, text="Velas", bg="green",command=lambda: set_category("Vela"))
            candle_button.place(x=870, y=35)

    #===Title===#
    Label(root, text="Odara Nature", bg="#D3D3D3", pady=30, font=("sans seriff", 25)).place(x=0, y=0, relwidth=1)

    soap_button = Button(root, text="Sabonetes", bg="green", command=lambda: set_category("Sabonete"))
    soap_button.place(x=800, y=35)

    candle_button = Button(root, text="Velas", command=lambda: set_category("Vela"))
    candle_button.place(x=870,y=35)

    #===Menu===#
    menu_frame = Frame(root, heigh=50,bg="yellow")
    menu_frame.place(x=0, y=100, relwidth=1)

    feedstock_options = ["Fornecedores", "Estoque"]
    purchases_options = ["Registrar Compra", "Ver Compras"]
    products_options = ["Ver Receitas", "Registrar Nova Produção", "Ver Produções"]

    f_menu_option = StringVar()
    p_menu_option = StringVar()
    prod_menu_option = StringVar()

    main_frame = Frame(root, height=750)
    main_frame.place(x=0, y=135, relwidth=1)

    def f_menu(o):
        Feedstock_interface(main_frame, o, category_option)
        f_menu_option.set("Matérias Primas")

    f_menu_option.set("Matérias Primas")
    p_menu_option.set("Compras")
    prod_menu_option.set("Produtos")

    feedstock_options_menu = OptionMenu(menu_frame, f_menu_option, *feedstock_options, command=f_menu)
    purchases_options_menu = OptionMenu(menu_frame, p_menu_option, *purchases_options)
    products_options_menu = OptionMenu(menu_frame, prod_menu_option, *products_options)

    feedstock_options_menu.config(font=("sans seriff", 12), padx=30, bg="#D3D3D3")
    feedstock_options_menu.grid(row=0, column=0, padx=30)

    purchases_options_menu.config(font=("sans seriff", 12), padx=30, bg="#D3D3D3")
    purchases_options_menu.grid(row=0, column=1, padx=30)

    products_options_menu.config(font=("sans seriff", 12), padx=30, bg="#D3D3D3")
    products_options_menu.grid(row=0, column=2, padx=30)


    root.mainloop()

if __name__ == "__main__":
    run()