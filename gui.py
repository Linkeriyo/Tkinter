import pickle
import tkinter
from tkinter import ttk, messagebox


class Contact:

    def __init__(self, tlf, surname, nombre):
        self.tlf = tlf
        self.surname = surname
        self.name = nombre


if __name__ == '__main__':
    contactList = []

    window = tkinter.Tk()
    window.geometry("625x300")
    window.title("Contactos")

    lbNombre = tkinter.Label(window, text="Nombre")
    lbNombre.grid(row=1, column=0)

    nameField = tkinter.Entry(window)
    nameField.grid(row=1, column=1)

    lbTelefono = tkinter.Label(window, text="Telefono")
    lbTelefono.grid(row=2, column=0)

    tlfField = tkinter.Entry(window)
    tlfField.grid(row=2, column=1)

    lbApellido1 = tkinter.Label(window, text="Apellidos")
    lbApellido1.grid(row=1, column=2)

    surnameField = tkinter.Entry(window)
    surnameField.grid(row=1, column=3)

    table = ttk.Treeview()
    table.grid(row=0, column=0, columnspan=4, ipadx=100)

    table["columns"] = ("1", "2", "3")

    table.column("#0", width=0)
    table.column("1", width=100, minwidth=100)
    table.column("2", width=100, minwidth=100)
    table.column("3", width=100, minwidth=100)
    table.heading("1", text="Telefono")
    table.heading("2", text="Apellidos")
    table.heading("3", text="Nombre")

    fichero1 = open("ContactsData", "ab+")
    fichero1.seek(0)
    try:
        contactList = pickle.load(fichero1)
    except:
        print("El fichero esta vacio")
    finally:
        fichero1.close()
    for i in range(0, len(contactList)):
        a: Contact = contactList[i]
        table.insert("", i, i, text="", values=(a.tlf, a.surname, a.name))


    def add():
        surname = surnameField.get()
        name = nameField.get()
        telephone = tlfField.get()
        a: Contact = Contact(telephone, surname, name)
        aux: Contact = Contact("null", "null", "null")

        if name != "" and telephone != "" and surname != "":

            for i in range(0, len(contactList)):
                if contactList[i].tlf == telephone:
                    aux: Contact = contactList[i]

            if aux.tlf != telephone or len(contactList) == 0:

                for i in table.get_children():
                    table.delete(i)

                contactList.append(a)

                for i in range(0, len(contactList)):
                    a: Contact = contactList[i]
                    table.insert("", i, i, text="", values=(a.tlf, a.surname, a.name))
            else:
                messagebox.showinfo(title="Error", message="Ya existe ese telefono para un contacto")

        else:
            messagebox.showinfo(title="Error", message="Has dejado en blanco alguno de los datos")


    addButton = tkinter.Button(window, text="Añadir", command=add)
    addButton.grid(row=3, column=0)


    def modify():
        surname = surnameField.get()
        name = nameField.get()
        telephone = tlfField.get()
        aux: Contact = Contact("null", "null", "null")

        if name != "" and telephone != "" and surname != "":

            for i in range(0, len(contactList)):
                if contactList[i].tlf == telephone:
                    contactList[i].surname = surname
                    contactList[i].name = name
                    contactList[i].tlf = telephone
                    aux: Contact = contactList[i]

            if aux.tlf == telephone:

                for i in table.get_children():
                    table.delete(i)

                for i in range(0, len(contactList)):
                    a: Contact = contactList[i]
                    table.insert("", i, i, text="", values=(a.tlf, a.surname, a.name))
            else:
                messagebox.showinfo(title="Error", message="No se encontro el contacto con ese telefono")

        else:
            messagebox.showinfo(title="Error", message="Has dejado en blanco alguno de los datos")


    btModificar = tkinter.Button(window, text="Modificar", command=modify)
    btModificar.grid(row=3, column=1)


    def remove():
        try:
            item = table.selection()[0]
            telephone = table.item(item, option="values")[0]

            for i in range(len(contactList) - 1, -1, -1):
                a: Contact = contactList[i]
                if a.tlf == telephone:
                    contactList.remove(a)

            table.delete(item)
        except:
            messagebox.showinfo("Info", "No has seleccionado ningún contacto")


    btBorrar = tkinter.Button(window, text="Eliminar", command=remove)
    btBorrar.grid(row=3, column=2)


    def on_closing():
        file = open("ContactsData", "wb")
        pickle.dump(contactList, file)
        file.close()
        window.destroy()


    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
