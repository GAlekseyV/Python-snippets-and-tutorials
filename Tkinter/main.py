import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.db = db
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="add.gif")
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('id', 'description', 'costs', 'total'),
                                 height=15, show='headings')
        self.tree.column('id', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)
        self.tree.heading('id', text='id')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('costs', text='Статья дохода/расхода')
        self.tree.heading('total', text='Сумма')
        self.tree.pack()

        self.view_records()

    def open_dialog(self):
        Child()

    def records(self, description, costs, total):
        self.db.insert_data(description, costs, total)
        self.view_records()

    def view_records(self):
        self.db.cursor.execute(
            '''SELECT * FROM finance'''
        )
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить доходы/расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.label_description = tk.Label(self, text='Наименование')
        self.label_description.place(x=50, y=50)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.label_total = tk.Label(self, text='Сумма:')
        self.label_total.place(x=50, y=110)
        self.entry_total = ttk.Entry(self)
        self.entry_total.place(x=200, y=110)

        self.label_select = tk.Label(self, text='Статья расхода/дохода')
        self.label_select.place(x=50, y=80)
        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel.place(x=300, y=170)

        self.btn_add = ttk.Button(self, text='Добавить')
        self.btn_add.place(x=220, y=170)

        self.btn_add.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                        self.entry_total.get(),
                                                                        self.combobox.get()))

        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.connection = sqlite3.connect('finance.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs text, total real)'''
        )
        self.connection.commit()

    def insert_data(self, description, costs, total):
        self.cursor.execute(
            '''INSERT INTO finance (description, costs, total) VALUES (?, ?, ?)''', (description, costs, total)
        )
        self.connection.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Домашние финансы")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
