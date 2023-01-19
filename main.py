import hashlib
import os
import SQLlib
import re
from tkinter import *
from tkinter import ttk
#глобальные переменные
maxorder_id = 0
users = {}  # Простое демо хранилище
maxorder = 0
maxusernum = 0
emailcook = ' '
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#глобальные переменные

def check(email):
    if (re.fullmatch(regex, email)):
        return 1

    else:
        return 0


def login():
    root.destroy()
    root1 = Tk()
    root1.title('Логинимся')
    def inpute():
        a = str(email.get())

        if(check(a) == 0):
            rooterr = Tk()
            rooterr.title('Ошибка')
            Label(rooterr, text="Почта не валидна").pack()
            rooterr.mainloop()

        b = str(passw.get())
        has = SQLlib.createPasswHash(b)
        global emailcook
        emailcook = a

        global maxorder_id
        maxorder_id = SQLlib.maxOrdId()

        print(maxorder_id)



        answ = SQLlib.loginUser(a, has)
        if (answ == [(True,)]):
            print('You admin')
            root1.destroy()
            admin()

        elif (answ == [(False,)]):
            print('hello user')
            root1.destroy()
            user()
        else:
            print('не верно что-то')

    Label(root1, text="Введите почту").pack()
    email = Entry(root1, width=50)
    email.pack()

    Label(root1, text="Введите пароль").pack()
    passw = Entry(root1, width=50, show="*")
    passw.pack()

    b1 = Button(root1, text="войти", command=inpute)
    b1.pack()
    root1.mainloop()






def registration():
    root.destroy()
    root0 = Tk()
    root0.title('Панель регистрации')

    def inpute2():
        a = str(name.get())
        b = str(lastname.get())
        c = str(passw.get())
        d = str(age.get())
        e = str(email.get())

        if (check(e) == 0):
            rooterr = Tk()
            rooterr.title('Ошибка')
            Label(rooterr, text="Почта не валидна").pack()
            rooterr.mainloop()

        has = SQLlib.createPasswHash(c)
        SQLlib.regustrationUser(a, b, has, d, e)

        global maxusernum
        maxusernum = SQLlib.numusercheck(e)
        global maxorder
        maxorder = SQLlib.maxOrd()
        print(maxusernum)
        print(maxorder)
        if (maxorder != maxusernum):
            SQLlib.createnewbasket(maxorder, maxusernum)

        root0.destroy()



    Label(root0, text="Введите имя").pack()
    name = Entry(root0, width=50)
    name.pack()
    Label(root0, text="Введите фамилию").pack()
    lastname = Entry(root0, width=50)
    lastname.pack()
    Label(root0, text="Введите пароль").pack()
    passw = Entry(root0, width=50, show="*")
    passw.pack()
    Label(root0, text="Введите возраст").pack()
    age = Entry(root0, width=50)
    age.pack()
    Label(root0, text="Введите email").pack()
    email = Entry(root0, width=50)
    email.pack()

    b1 = Button(root0, text="зарегистрироваться", command=inpute2)
    b1.pack()

    root0.mainloop()


def admin():
    def change():
        if var.get() == 0:
            root.destroy()
            showData()
        elif var.get() == 1:
            root.destroy()
            inserttable()
        elif var.get() == 2:
            root.destroy()
            edittable()
        elif var.get() == 3:
            root.destroy()
            deleteDatTabl()
        elif var.get() == 4:
            root.destroy()
            AllInfoBooks()

    root = Tk()
    root.title('Панель управления')
    var = IntVar()
    var.set(0)
    rad1 = Radiobutton(text="Показать данные таблицы",
                      variable=var, value=0)
    rad2 = Radiobutton(text="Вставить данные в таблицу",
                        variable=var, value=1)
    rad3 = Radiobutton(text="Редактировать данные в таблице",
                       variable=var, value=2)
    rad4 = Radiobutton(text="Удалить данные из таблицы",
                       variable=var, value=3)
    rad5 = Radiobutton(text="Вся информация о книгах",
                       variable=var, value=4)
    button = Button(text="Далее",
                    command=change)

    rad1.pack()
    rad2.pack()
    rad3.pack()
    rad4.pack()
    rad5.pack()
    button.pack()


    root.mainloop()



def AllInfoBooks():
    root101 = Tk()
    root101.title("Книги")
    root101.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableBooksAllInfo()

    # определяем столбцы
    columns = (
    "id_book", "namebook", "price_one_copy", "release_date", "circulation", "author", "published", "literaturetype")

    one = ttk.Treeview(root101, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("id_book", text="id книги", anchor=W)
    one.heading("namebook", text="Название", anchor=W)
    one.heading("price_one_copy", text="Цена одного экз", anchor=W)
    one.heading("release_date", text="Дата релиза", anchor=W)
    one.heading("circulation", text="кол-во", anchor=W)
    one.heading("author", text="автор", anchor=W)
    one.heading("published", text="Издательство", anchor=W)
    one.heading("literaturetype", text="тип дитературы", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=150)
    one.column("#3", stretch=NO, width=100)
    one.column("#4", stretch=NO, width=100)
    one.column("#5", stretch=NO, width=100)
    one.column("#6", stretch=NO, width=100)
    one.column("#7", stretch=NO, width=100)
    one.column("#8", stretch=NO, width=100)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root101.mainloop()



def showData():


    def change():
        if var.get() == 0:
            accountBooks()
        elif var.get() == 1:
            authors()
        elif var.get() == 2:
            basket()
        elif var.get() == 3:
            books()
        elif var.get() == 4:
            orderlines()
        elif var.get() == 5:
            publishhouse()
        elif var.get() == 6:
            typeofliterature()
        elif var.get() == 7:
            useradm()

    root6 = Tk()
    root6.title('Выбор таблицы')
    var = IntVar()
    var.set(0)
    rad1 = Radiobutton(text="Показать таблицу количество книг",
                      variable=var, value=0)
    rad2 = Radiobutton(text="Показать таблицу авторы",
                        variable=var, value=1)
    rad3 = Radiobutton(text="Показать таблицу корзина",
                       variable=var, value=2)
    rad4 = Radiobutton(text="Показать таблицу книги",
                       variable=var, value=3)
    rad5 = Radiobutton(text="Показать таблицу строка заказа",
                       variable=var, value=4)
    rad6 = Radiobutton(text="Показать таблицу издательства",
                       variable=var, value=5)
    rad7 = Radiobutton(text="Показать таблицу тип литературы",
                       variable=var, value=6)
    rad8 = Radiobutton(text="Показать таблицу пользователи",
                       variable=var, value=7)
    button = Button(text="Далее",
                    command=change)

    rad1.pack()
    rad2.pack()
    rad3.pack()
    rad4.pack()
    rad5.pack()
    rad6.pack()
    rad7.pack()
    rad8.pack()
    button.pack()


    root6.mainloop()




def accountBooks():
    root7 = Tk()
    root7.title("Учет книг")
    root7.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableAccountBooks()

    # определяем столбцы
    columns = ("code_accounting", "amount", "receipt_date")

    one = ttk.Treeview(root7, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("code_accounting", text="Код количества", anchor=W)
    one.heading("amount", text="Количество", anchor=W)
    one.heading("receipt_date", text="Дата поступления", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=60)
    one.column("#3", stretch=NO, width=100)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root7.mainloop()

def authors():
    root8 = Tk()
    root8.title("Авторы")
    root8.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableAuthors()

    # определяем столбцы
    columns = ("code_author", "firstname", "lastname")

    one = ttk.Treeview(root8, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("code_author", text="Код автора", anchor=W)
    one.heading("firstname", text="Имя", anchor=W)
    one.heading("lastname", text="Фамилия", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=60)
    one.column("#3", stretch=NO, width=100)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root8.mainloop()

def basket():
    root9 = Tk()
    root9.title("Корзина")
    root9.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableBasket()

    # определяем столбцы
    columns = ("order_id", "datte", "order")

    one = ttk.Treeview(root9, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("order_id", text="id корзины", anchor=W)
    one.heading("datte", text="дата", anchor=W)
    one.heading("order", text="id юзера", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=100)
    one.column("#3", stretch=NO, width=100)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root9.mainloop()

def books():
    root10 = Tk()
    root10.title("Книги")
    root10.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableBooks()

    # определяем столбцы
    columns = ("id_book", "namebook", "price_one_copy", "release_date", "circulation", "author", "published", "literaturetype")

    one = ttk.Treeview(root10, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("id_book", text="id книги", anchor=W)
    one.heading("namebook", text="Название", anchor=W)
    one.heading("price_one_copy", text="Цена одного экз", anchor=W)
    one.heading("release_date", text="Дата релиза", anchor=W)
    one.heading("circulation", text="кол-во", anchor=W)
    one.heading("author", text="автор", anchor=W)
    one.heading("published", text="Издательство", anchor=W)
    one.heading("literaturetype", text="тип дитературы", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=150)
    one.column("#3", stretch=NO, width=100)
    one.column("#4", stretch=NO, width=100)
    one.column("#5", stretch=NO, width=100)
    one.column("#6", stretch=NO, width=100)
    one.column("#7", stretch=NO, width=100)
    one.column("#8", stretch=NO, width=100)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root10.mainloop()

def orderlines():
    root11 = Tk()
    root11.title("Строки заказа")
    root11.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableOrderLines()

    # определяем столбцы
    columns = ("id_order", "amount", "book", "basketnum")

    one = ttk.Treeview(root11, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("id_order", text="id строки", anchor=W)
    one.heading("amount", text="количество", anchor=W)
    one.heading("book", text="id книги", anchor=W)
    one.heading("basketnum", text="id корзины", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=60)
    one.column("#3", stretch=NO, width=100)
    one.column("#4", stretch=NO, width=100)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root11.mainloop()

def publishhouse():
    root12 = Tk()
    root12.title("Издательства")
    root12.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTablePublishingHouse()

    # определяем столбцы
    columns = ("publisher_code", "publisher_nazv", "city")

    one = ttk.Treeview(root12, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("publisher_code", text="Код издательства", anchor=W)
    one.heading("publisher_nazv", text="Название", anchor=W)
    one.heading("city", text="Город", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=120)
    one.column("#3", stretch=NO, width=100)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root12.mainloop()

def typeofliterature():
    root13 = Tk()
    root13.title("Тип литературы")
    root13.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableTypeofLiterature()

    # определяем столбцы
    columns = ("type_code", "type_literature")

    one = ttk.Treeview(root13, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("type_code", text="Код издательства", anchor=W)
    one.heading("type_literature", text="Название", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=100)
    one.column("#2", stretch=NO, width=150)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root13.mainloop()

def useradm():
    root14 = Tk()
    root14.title("Книги")
    root14.geometry("250x200")

    # определяем данные для отображения
    people = SQLlib.printTableUser()

    # определяем столбцы
    columns = ("number", "rolle", "firstname", "lastname", "passwordd", "number_books_purchased", "age", "loyalty_system", "email")

    one = ttk.Treeview(root14, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("number", text="id пользователя", anchor=W)
    one.heading("rolle", text="Роль", anchor=W)
    one.heading("firstname", text="Имя", anchor=W)
    one.heading("lastname", text="Фамилия", anchor=W)
    one.heading("passwordd", text="Пароль", anchor=W)
    one.heading("number_books_purchased", text="Кол-во купленных книг", anchor=W)
    one.heading("age", text="Возраст", anchor=W)
    one.heading("loyalty_system", text="Система бонусов", anchor=W)
    one.heading("email", text="Почта", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=70)
    one.column("#2", stretch=NO, width=150)
    one.column("#3", stretch=NO, width=100)
    one.column("#4", stretch=NO, width=100)
    one.column("#5", stretch=NO, width=100)
    one.column("#6", stretch=NO, width=100)
    one.column("#7", stretch=NO, width=100)
    one.column("#8", stretch=NO, width=100)
    one.column("#9", stretch=NO, width=150)

    # добавляем данные
    for person in people:
        one.insert("", END, values=person)

    root14.mainloop()


def inserttable():
    def change():
        if var.get() == 0:
            insertaccountBooks()
        elif var.get() == 1:
            insertauthors()
        elif var.get() == 2:
            insertbasket()
        elif var.get() == 3:
            insertbooks()
        elif var.get() == 4:
            insertorderlines()
        elif var.get() == 5:
            insertpublishhouse()
        elif var.get() == 6:
            inserttypeofliterature()
        elif var.get() == 7:
            insertuseradm()

    root15 = Tk()
    root15.title('Выбор таблицы')
    var = IntVar()
    var.set(0)
    rad1 = Radiobutton(text="Вставить в таблицу количество книг",
                      variable=var, value=0)
    rad2 = Radiobutton(text="Вставить в таблицу авторы",
                        variable=var, value=1)
    rad3 = Radiobutton(text="Вставить в таблицу корзина",
                       variable=var, value=2)
    rad4 = Radiobutton(text="Вставить в таблицу книги",
                       variable=var, value=3)
    rad5 = Radiobutton(text="Вставить в таблицу строка заказа",
                       variable=var, value=4)
    rad6 = Radiobutton(text="Вставить в таблицу издательства",
                       variable=var, value=5)
    rad7 = Radiobutton(text="Вставить в таблицу тип литературы",
                       variable=var, value=6)
    rad8 = Radiobutton(text="Вставить в таблицу пользователи",
                       variable=var, value=7)
    button = Button(text="Далее",
                    command=change)

    rad1.pack()
    rad2.pack()
    rad3.pack()
    rad4.pack()
    rad5.pack()
    rad6.pack()
    rad7.pack()
    rad8.pack()
    button.pack()


    root15.mainloop()

def insertaccountBooks():
    def inpute3():
        a = str(code.get())
        b = str(count.get())
        c = str(dat.get())
        SQLlib.inserttablefunk(a, b, c)


    root16 = Tk()
    root16.title('Добавление')
    Label(root16, text="Введите код").pack()
    code = Entry(root16, width=50)
    code.pack()
    Label(root16, text="Введите количество").pack()
    count = Entry(root16, width=50)
    count.pack()
    Label(root16, text="Введите дату").pack()
    dat = Entry(root16, width=50)
    dat.pack()

    b1 = Button(root16, text="добавить", command=inpute3)
    b1.pack()

    accountBooks()
    root16.mainloop()

def insertauthors():
    def inpute4():
        a = str(code.get())
        b = str(name.get())
        c = str(name2.get())
        SQLlib.insertauthorsfunk(a, b, c)

    root17 = Tk()
    root17.title('Добавление')
    Label(root17, text="Введите код").pack()
    code = Entry(root17, width=50)
    code.pack()
    Label(root17, text="Введите имя").pack()
    name = Entry(root17, width=50)
    name.pack()
    Label(root17, text="Введите фамилию").pack()
    name2 = Entry(root17, width=50)
    name2.pack()

    b1 = Button(root17, text="добавить", command=inpute4)
    b1.pack()
    authors()
    root17.mainloop()

def insertbasket():
    def inpute5():
        a = str(code.get())
        b = str(dat.get())
        c = str(code2.get())
        SQLlib.insertbasketfunk(a, b, c)

    root18 = Tk()
    root18.title('Добавление')
    Label(root18, text="Введите код").pack()
    code = Entry(root18, width=50)
    code.pack()
    Label(root18, text="Введите дату").pack()
    dat = Entry(root18, width=50)
    dat.pack()
    Label(root18, text="Введите кодпольз").pack()
    code2 = Entry(root18, width=50)
    code2.pack()

    b1 = Button(root18, text="добавить", command=inpute5)
    b1.pack()
    basket()
    root18.mainloop()

def insertbooks():
    def inpute6():
        a = str(code.get())
        b = str(name.get())
        c = str(price.get())
        d = str(date.get())
        e = str(codecount.get())
        u = str(author.get())
        i = str(publish.get())
        f = str(literaturetype.get())
        SQLlib.insertbooksfunk(a, b, c, d, e, u, i, f)

    root19 = Tk()
    root19.title('Добавление')
    Label(root19, text="Введите код книги").pack()
    code = Entry(root19, width=50)
    code.pack()
    Label(root19, text="Введите имя книги").pack()
    name = Entry(root19, width=50)
    name.pack()
    Label(root19, text="Введите цену одн экз").pack()
    price = Entry(root19, width=50)
    price.pack()
    Label(root19, text="Введите дату релиза").pack()
    date = Entry(root19, width=50)
    date.pack()
    Label(root19, text="Введите кодколва").pack()
    codecount = Entry(root19, width=50)
    codecount.pack()
    Label(root19, text="Введите кодавтора").pack()
    author = Entry(root19, width=50)
    author.pack()
    Label(root19, text="Введите кодиздат").pack()
    publish = Entry(root19, width=50)
    publish.pack()
    Label(root19, text="Введите кодлитературы").pack()
    literaturetype = Entry(root19, width=50)
    literaturetype.pack()

    b1 = Button(root19, text="добавить", command=inpute6)
    b1.pack()
    books()
    root19.mainloop()

def insertorderlines():
    def inpute7():
        a = str(code.get())
        b = str(count.get())
        c = str(book.get())
        d = str(baskenum.get())
        SQLlib.insertorderlinesfunk(a, b, c, d)

    root20 = Tk()
    root20.title('Добавление')
    Label(root20, text="Введите код").pack()
    code = Entry(root20, width=50)
    code.pack()
    Label(root20, text="Введите дату").pack()
    count = Entry(root20, width=50)
    count.pack()
    Label(root20, text="Введите кодпольз").pack()
    book = Entry(root20, width=50)
    book.pack()
    Label(root20, text="Введите кодпольз").pack()
    baskenum = Entry(root20, width=50)
    baskenum.pack()

    b1 = Button(root20, text="добавить", command=inpute7)
    b1.pack()
    orderlines()
    root20.mainloop()

def insertpublishhouse():
    def inpute8():
        a = str(code.get())
        b = str(namepubl.get())
        c = str(city.get())
        SQLlib.insertpublishhousefunk(a, b, c)

    root21 = Tk()
    root21.title('Добавление')
    Label(root21, text="Введите кодизд").pack()
    code = Entry(root21, width=50)
    code.pack()
    Label(root21, text="Введите названиеиздат").pack()
    namepubl = Entry(root21, width=50)
    namepubl.pack()
    Label(root21, text="Введите город").pack()
    city = Entry(root21, width=50)
    city.pack()

    b1 = Button(root21, text="добавить", command=inpute8)
    b1.pack()
    publishhouse()
    root21.mainloop()

def inserttypeofliterature():
    def inpute9():
        a = str(code.get())
        b = str(nazv.get())
        SQLlib.inserttypeofliteraturefunk(a, b)

    root21 = Tk()
    root21.title('Добавление')
    Label(root21, text="Введите кодлитер").pack()
    code = Entry(root21, width=50)
    code.pack()
    Label(root21, text="Введите назвтипалитературы").pack()
    nazv = Entry(root21, width=50)
    nazv.pack()

    b1 = Button(root21, text="добавить", command=inpute9)
    b1.pack()
    typeofliterature()
    root21.mainloop()

def insertuseradm():
    def inpute10():
        a = str(numb.get())
        b = str(rol.get())
        c = str(firstname.get())
        d = str(lastname.get())
        e = str(pasw.get())
        u = str(numpublish.get())
        i = str(age.get())
        f = str(loyalsys.get())
        l = str(emaill.get())
        SQLlib.insertuseradmfunk(a, b, c, d, e, u, i, f, l)

    root22 = Tk()
    root22.title('Добавление')
    Label(root22, text="Введите код пользоателя").pack()
    numb = Entry(root22, width=50)
    numb.pack()
    Label(root22, text="Введите роль").pack()
    rol = Entry(root22, width=50)
    rol.pack()
    Label(root22, text="Введите имя").pack()
    firstname = Entry(root22, width=50)
    firstname.pack()
    Label(root22, text="Введите фамилию").pack()
    lastname = Entry(root22, width=50)
    lastname.pack()
    Label(root22, text="Введите пароль").pack()
    pasw = Entry(root22, width=50, show="*")
    pasw.pack()
    Label(root22, text="Введите колво купл книг").pack()
    numpublish = Entry(root22, width=50)
    numpublish.pack()
    Label(root22, text="Введите возраст").pack()
    age = Entry(root22, width=50)
    age.pack()
    Label(root22, text="Введите очки лояльности").pack()
    loyalsys = Entry(root22, width=50)
    loyalsys.pack()
    Label(root22, text="Введите почту").pack()
    emaill = Entry(root22, width=50)
    emaill.pack()

    b1 = Button(root22, text="добавить", command=inpute10)
    b1.pack()
    useradm()
    root22.mainloop()


def edittable():
    def change():
        if var.get() == 0:
            edittableaccountBooks()
        elif var.get() == 1:
            edittableauthors()
        elif var.get() == 2:
            edittablebasket()
        elif var.get() == 3:
            edittablebooks()
        elif var.get() == 4:
            edittableorderlines()
        elif var.get() == 5:
            edittablepublishhouse()
        elif var.get() == 6:
            edittabletypeofliterature()
        elif var.get() == 7:
            edittableuseradm()

    root23 = Tk()
    root23.title('Редактирование таблицы')
    var = IntVar()
    var.set(0)
    rad1 = Radiobutton(text="Редактировать таблицу количество книг",
                       variable=var, value=0)
    rad2 = Radiobutton(text="Редактировать таблицу авторы",
                       variable=var, value=1)
    rad3 = Radiobutton(text="Редактировать таблицу корзина",
                       variable=var, value=2)
    rad4 = Radiobutton(text="Редактировать таблицу книги",
                       variable=var, value=3)
    rad5 = Radiobutton(text="Редактировать таблицу строка заказа",
                       variable=var, value=4)
    rad6 = Radiobutton(text="Редактировать таблицу издательства",
                       variable=var, value=5)
    rad7 = Radiobutton(text="Редактировать таблицу тип литературы",
                       variable=var, value=6)
    rad8 = Radiobutton(text="Редактировать таблицу пользователи",
                       variable=var, value=7)
    button = Button(text="Далее",
                    command=change)

    rad1.pack()
    rad2.pack()
    rad3.pack()
    rad4.pack()
    rad5.pack()
    rad6.pack()
    rad7.pack()
    rad8.pack()
    button.pack()

    root23.mainloop()


def edittableaccountBooks():
    def inpute11():
        a = str(code.get())
        b = str(count.get())
        c = str(dat.get())
        d = str(change.get())
        SQLlib.edittableaccountbooks1(a, b, c, d)

    root24 = Tk()
    root24.title('Изменение')
    Label(root24, text="Введите код").pack()
    code = Entry(root24, width=50)
    code.pack()
    Label(root24, text="Введите количество").pack()
    count = Entry(root24, width=50)
    count.pack()
    Label(root24, text="Введите дату").pack()
    dat = Entry(root24, width=50)
    dat.pack()
    Label(root24, text="Id замены").pack()
    change = Entry(root24, width=50)
    change.pack()

    b1 = Button(root24, text="изменить", command=inpute11)
    b1.pack()

    accountBooks()
    root24.mainloop()


def edittableauthors():
    def inpute12():
        a = str(code.get())
        b = str(name.get())
        c = str(name2.get())
        d = str(cange.get())
        SQLlib.edittableauthors1(a, b, c, d)

    root25 = Tk()
    root25.title('Изменение')
    Label(root25, text="Введите код").pack()
    code = Entry(root25, width=50)
    code.pack()
    Label(root25, text="Введите имя").pack()
    name = Entry(root25, width=50)
    name.pack()
    Label(root25, text="Введите фамилию").pack()
    name2 = Entry(root25, width=50)
    name2.pack()
    Label(root25, text="Введите кодзамены").pack()
    cange = Entry(root25, width=50)
    cange.pack()

    b1 = Button(root25, text="изменить", command=inpute12)
    b1.pack()
    authors()
    root25.mainloop()


def edittablebasket():
    def inpute13():
        a = str(code.get())
        b = str(dat.get())
        c = str(code2.get())
        d = str(cange.get())
        SQLlib.edittablebasket1(a, b, c, d)

    root26 = Tk()
    root26.title('Изменение')
    Label(root26, text="Введите код").pack()
    code = Entry(root26, width=50)
    code.pack()
    Label(root26, text="Введите дату").pack()
    dat = Entry(root26, width=50)
    dat.pack()
    Label(root26, text="Введите кодпольз").pack()
    code2 = Entry(root26, width=50)
    code2.pack()
    Label(root26, text="Введите idзамены").pack()
    cange = Entry(root26, width=50)
    cange.pack()

    b1 = Button(root26, text="изменить", command=inpute13)
    b1.pack()
    basket()
    root26.mainloop()


def edittablebooks():
    def inpute14():
        a = str(code.get())
        b = str(name.get())
        c = str(price.get())
        d = str(date.get())
        e = str(codecount.get())
        u = str(author.get())
        i = str(publish.get())
        f = str(literaturetype.get())
        g = str(cange.get())
        SQLlib.edittablebooks1(a, b, c, d, e, u, i, f, g)

    root27 = Tk()
    root27.title('Изменение')
    Label(root27, text="Введите код книги").pack()
    code = Entry(root27, width=50)
    code.pack()
    Label(root27, text="Введите имя книги").pack()
    name = Entry(root27, width=50)
    name.pack()
    Label(root27, text="Введите цену одн экз").pack()
    price = Entry(root27, width=50)
    price.pack()
    Label(root27, text="Введите дату релиза").pack()
    date = Entry(root27, width=50)
    date.pack()
    Label(root27, text="Введите кодколва").pack()
    codecount = Entry(root27, width=50)
    codecount.pack()
    Label(root27, text="Введите кодавтора").pack()
    author = Entry(root27, width=50)
    author.pack()
    Label(root27, text="Введите кодиздат").pack()
    publish = Entry(root27, width=50)
    publish.pack()
    Label(root27, text="Введите кодлитературы").pack()
    literaturetype = Entry(root27, width=50)
    literaturetype.pack()
    Label(root27, text="Введите idзамены").pack()
    cange = Entry(root27, width=50)
    cange.pack()

    b1 = Button(root27, text="изменить", command=inpute14)
    b1.pack()
    books()
    root27.mainloop()


def edittableorderlines():
    def inpute15():
        a = str(code.get())
        b = str(count.get())
        c = str(book.get())
        d = str(baskenum.get())
        e = str(cange.get())
        SQLlib.edittableorderlines1(a, b, c, d, e)

    root28 = Tk()
    root28.title('Изменение')
    Label(root28, text="Введите код").pack()
    code = Entry(root28, width=50)
    code.pack()
    Label(root28, text="Введите дату").pack()
    count = Entry(root28, width=50)
    count.pack()
    Label(root28, text="Введите кодпольз").pack()
    book = Entry(root28, width=50)
    book.pack()
    Label(root28, text="Введите кодпольз").pack()
    baskenum = Entry(root28, width=50)
    baskenum.pack()
    Label(root28, text="Введите idзамены").pack()
    cange = Entry(root28, width=50)
    cange.pack()

    b1 = Button(root28, text="изменить", command=inpute15)
    b1.pack()
    orderlines()
    root28.mainloop()


def edittablepublishhouse():
    def inpute16():
        a = str(code.get())
        b = str(namepubl.get())
        c = str(city.get())
        d = str(cange.get())
        SQLlib.edittablepublishhouse1(a, b, c, d)

    root29 = Tk()
    root29.title('Изменение')
    Label(root29, text="Введите кодизд").pack()
    code = Entry(root29, width=50)
    code.pack()
    Label(root29, text="Введите названиеиздат").pack()
    namepubl = Entry(root29, width=50)
    namepubl.pack()
    Label(root29, text="Введите город").pack()
    city = Entry(root29, width=50)
    city.pack()
    Label(root29, text="Введите idзамены").pack()
    cange = Entry(root29, width=50)
    cange.pack()

    b1 = Button(root29, text="изменить", command=inpute16)
    b1.pack()
    publishhouse()
    root29.mainloop()


def edittabletypeofliterature():
    def inpute17():
        a = str(code.get())
        b = str(nazv.get())
        c = str(zamen.get())
        SQLlib.edittabletypeofliterature1(a, b, c)

    root30 = Tk()
    root30.title('Изменение')
    Label(root30, text="Введите id").pack()
    code = Entry(root30, width=50)
    code.pack()
    Label(root30, text="Введите назвтипалитературы").pack()
    nazv = Entry(root30, width=50)
    nazv.pack()
    Label(root30, text="Введите какой id заменить").pack()
    zamen = Entry(root30, width=50)
    zamen.pack()

    b1 = Button(root30, text="изменить", command=inpute17)
    b1.pack()
    typeofliterature()
    root30.mainloop()


def edittableuseradm():
    def inpute18():
        a = str(numb.get())
        b = str(rol.get())
        c = str(firstname.get())
        d = str(lastname.get())
        e = str(pasw.get())
        u = str(numpublish.get())
        i = str(age.get())
        f = str(loyalsys.get())
        l = str(emaill.get())
        h = str(cange.get())
        SQLlib.edittableuseradm1(a, b, c, d, e, u, i, f, l, h)

    root31 = Tk()
    root31.title('Добавление')
    Label(root31, text="Введите код пользоателя").pack()
    numb = Entry(root31, width=50)
    numb.pack()
    Label(root31, text="Введите роль").pack()
    rol = Entry(root31, width=50)
    rol.pack()
    Label(root31, text="Введите имя").pack()
    firstname = Entry(root31, width=50)
    firstname.pack()
    Label(root31, text="Введите фамилию").pack()
    lastname = Entry(root31, width=50)
    lastname.pack()
    Label(root31, text="Введите пароль").pack()
    pasw = Entry(root31, width=50, show="*")
    pasw.pack()
    Label(root31, text="Введите колво купл книг").pack()
    numpublish = Entry(root31, width=50)
    numpublish.pack()
    Label(root31, text="Введите возраст").pack()
    age = Entry(root31, width=50)
    age.pack()
    Label(root31, text="Введите очки лояльности").pack()
    loyalsys = Entry(root31, width=50)
    loyalsys.pack()
    Label(root31, text="Введите почту").pack()
    emaill = Entry(root31, width=50)
    emaill.pack()
    Label(root31, text="Введите idзамены").pack()
    cange = Entry(root31, width=50)
    cange.pack()

    b1 = Button(root31, text="добавить", command=inpute18)
    b1.pack()
    useradm()
    root31.mainloop()


def deleteDatTabl():
    def change():
        if var.get() == 'accountingbooks':

            def doit():
                a = str(delit.get())
                TableNmae = 'accountingbooks'
                SQLlib.deleteData('accountingbooks', 'code_accounting', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            accountBooks()
            root32.mainloop()
        elif var.get() == 'authors':
            def doit():
                a = str(delit.get())
                TableNmae = 'authors'
                SQLlib.deleteData('authors', 'code_author', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            authors()
            root32.mainloop()
        elif var.get() == 'basket':
            def doit():
                a = str(delit.get())
                TableNmae = 'basket'
                SQLlib.deleteData('basket', 'order_id', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            basket()
            root32.mainloop()
        elif var.get() == 'books':
            def doit():
                a = str(delit.get())
                TableNmae = 'books'
                SQLlib.deleteData('books', 'id_book', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            books()
            root32.mainloop()
        elif var.get() == 'orderlines':
            def doit():
                a = str(delit.get())
                TableNmae = 'orderlines'
                SQLlib.deleteData('orderlines', 'id_order', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            orderlines()
            root32.mainloop()
        elif var.get() == 'publishinghouse':
            def doit():
                a = str(delit.get())
                TableNmae = 'publishinghouse'
                SQLlib.deleteData('publishinghouse', 'publisher_code', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            publishhouse()
            root32.mainloop()
        elif var.get() == 'typeofliterature':
            def doit():
                a = str(delit.get())
                TableNmae = 'typeofliterature'
                SQLlib.deleteData('typeofliterature', 'type_code', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            typeofliterature()
            root32.mainloop()
        elif var.get() == 'user':
            def doit():
                a = str(delit.get())
                TableNmae = 'user'
                SQLlib.deleteData('user', 'number', a)

            root32 = Tk()
            root32.title('Удаление')
            Label(root32, text="Введите idудаления").pack()
            delit = Entry(root32, width=50)
            delit.pack()

            b1 = Button(root32, text="удалить", command=doit)
            b1.pack()
            useradm()
            root32.mainloop()

    root32 = Tk()
    root32.title('Удаление строк таблицы')
    var = StringVar()
    var.set('hello')
    rad1 = Radiobutton(text="Удалить строку в таблице количество книг",
                       variable=var, value='accountingbooks')
    rad2 = Radiobutton(text="Удалить строку в таблице авторы",
                       variable=var, value='authors')
    rad3 = Radiobutton(text="Удалить строку в таблице корзина",
                       variable=var, value='basket')
    rad4 = Radiobutton(text="Удалить строку в таблице книги",
                       variable=var, value='books')
    rad5 = Radiobutton(text="Удалить строку в таблице строка заказа",
                       variable=var, value='orderlines')
    rad6 = Radiobutton(text="Удалить строку в таблице издательства",
                       variable=var, value='publishinghouse')
    rad7 = Radiobutton(text="Удалить строку в таблице тип литературы",
                       variable=var, value='typeofliterature')
    rad8 = Radiobutton(text="Удалить строку в таблице пользователи",
                       variable=var, value='user')
    button = Button(text="удалить",
                    command=change)

    rad1.pack()
    rad2.pack()
    rad3.pack()
    rad4.pack()
    rad5.pack()
    rad6.pack()
    rad7.pack()
    rad8.pack()
    button.pack()

    root32.mainloop()




def user():



    root3 = Tk()
    root3.geometry('1240x800')
    root3.title('Книжный магазин пользовательское меню')

    frame1 = LabelFrame(text='Book1', width=100, height=100)
    frame2 = LabelFrame(text='Book2', width=100, height=100)
    frame3 = LabelFrame(text='Book3', width=100, height=100)
    frame4 = LabelFrame(text='Book4', width=100, height=100)
    frame5 = LabelFrame(text='Book5', width=100, height=100)
    frame6 = LabelFrame(text='Book6', width=100, height=100)
    frame7 = LabelFrame(text='Book7', width=100, height=100)
    frame8 = LabelFrame(text='Book8', width=100, height=100)
    frame9 = LabelFrame(text='Book9', width=100, height=100)
    frame10 = LabelFrame(text='Book10', width=100, height=100)

    lab1 = Label(frame1, text="Лисья нора")
    lab2 = Label(frame2, text="Свита короля. Все ради игры")
    lab3 = Label(frame3, text="1984")
    lab4 = Label(frame4, text="Скотный Двор")
    lab5 = Label(frame5, text="География. 9 класс. Контурные карты")
    lab6 = Label(frame6, text="Убийство в Восточном экспрессе")
    lab7 = Label(frame7, text="Смерть на Ниле")
    lab8 = Label(frame8, text="Гарри Поттер и философский камень")
    lab9 = Label(frame9, text="Ходячий замок")
    lab10 = Label(frame10, text="Три товарища")

    frame101 = LabelFrame(text='basket', width=100, height=100)


    b1 = Button(frame1, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket1)
    b2 = Button(frame2, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket2)
    b3 = Button(frame3, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket3)
    b4 = Button(frame4, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket4)
    b5 = Button(frame5, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket5)
    b6 = Button(frame6, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket6)
    b7 = Button(frame7, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket7)
    b8 = Button(frame8, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket8)
    b9 = Button(frame9, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket9)
    b10 = Button(frame10, text='Добавить', bg='black', fg='white', width=10, command=addingtobasket10)

    basketbutn = Button(frame101, text='Перейти', bg='black', fg='white', width=10, command=yourbasket)

    frame1.pack(padx=10, pady=10, side=LEFT)
    frame2.pack(padx=10, pady=10, side=LEFT)
    frame3.pack(padx=10, pady=10, side=LEFT)
    frame4.pack(padx=10, pady=10, side=LEFT)
    frame5.pack(padx=10, pady=10, side=LEFT)
    frame6.pack(padx=10, pady=10, side=BOTTOM)
    frame7.pack(padx=10, pady=10, side=BOTTOM)
    frame8.pack(padx=10, pady=10, side=BOTTOM)
    frame9.pack(padx=10, pady=10, side=BOTTOM)
    frame10.pack(padx=10, pady=10, side=BOTTOM)
    lab1.pack(padx=10, pady=10, side=TOP)
    b1.pack(padx=10, pady=10)
    lab2.pack(padx=10, pady=10, side=TOP)
    b2.pack(padx=10, pady=10)
    lab3.pack(padx=10, pady=10, side=TOP)
    b3.pack(padx=10, pady=10)
    lab4.pack(padx=10, pady=10, side=TOP)
    b4.pack(padx=10, pady=10)
    lab5.pack(padx=10, pady=10, side=TOP)
    b5.pack(padx=10, pady=10)
    lab6.pack(padx=10, pady=10, side=TOP)
    b6.pack(padx=10, pady=10)
    lab7.pack(padx=10, pady=10, side=TOP)
    b7.pack(padx=10, pady=10)
    lab8.pack(padx=10, pady=10, side=TOP)
    b8.pack(padx=10, pady=10)
    lab9.pack(padx=10, pady=10, side=TOP)
    b9.pack(padx=10, pady=10)
    lab10.pack(padx=10, pady=10, side=TOP)
    b10.pack(padx=10, pady=10)
    frame101.pack(padx=10, pady=10, side=TOP)
    basketbutn.pack(padx=10, pady=10)

    root3.mainloop()

def addingtobasket1():
    root4 = Tk()
    root4.geometry('240x240')
    root4.title('кол-во книг')
    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 11
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)


    lab11 = Label(root4, text="Сколько книг вы хотите")
    code = Entry(root4, width=50)

    b11 = Button(root4, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root4.mainloop()

def addingtobasket2():
    root5 = Tk()
    root5.geometry('240x240')
    root5.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 22
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root5, text="Сколько книг вы хотите")
    code = Entry(root5, width=50)

    b11 = Button(root5, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root5.mainloop()


def addingtobasket3():
    root6 = Tk()
    root6.geometry('240x240')
    root6.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 33
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root6, text="Сколько книг вы хотите")
    code = Entry(root6, width=50)

    b11 = Button(root6, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root6.mainloop()


def addingtobasket4():
    root7 = Tk()
    root7.geometry('240x240')
    root7.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 44
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root7, text="Сколько книг вы хотите")
    code = Entry(root7, width=50)

    b11 = Button(root7, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root7.mainloop()


def addingtobasket5():
    root8 = Tk()
    root8.geometry('240x240')
    root8.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 55
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root8, text="Сколько книг вы хотите")
    code = Entry(root8, width=50)

    b11 = Button(root8, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root8.mainloop()


def addingtobasket6():
    root9 = Tk()
    root9.geometry('240x240')
    root9.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 66
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root9, text="Сколько книг вы хотите")
    code = Entry(root9, width=50)

    b11 = Button(root9, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root9.mainloop()


def addingtobasket7():
    root10 = Tk()
    root10.geometry('240x240')
    root10.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 77
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root10, text="Сколько книг вы хотите")
    code = Entry(root10, width=50)

    b11 = Button(root10, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root10.mainloop()


def addingtobasket8():
    root11 = Tk()
    root11.geometry('240x240')
    root11.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 88
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root11, text="Сколько книг вы хотите")
    code = Entry(root11, width=50)

    b11 = Button(root11, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root11.mainloop()


def addingtobasket9():
    root12 = Tk()
    root12.geometry('240x240')
    root12.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 99
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root12, text="Сколько книг вы хотите")
    code = Entry(root12, width=50)

    b11 = Button(root12, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root12.mainloop()


def addingtobasket10():
    root13 = Tk()
    root13.geometry('240x240')
    root13.title('кол-во книг')

    def getbook():
        maxordid = SQLlib.maxIdOrdOrderlines()
        a = str(code.get())
        b = 100
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.insertintoorderlineszakaz(maxordid, a, b, answerline)

    lab11 = Label(root13, text="Сколько книг вы хотите")
    code = Entry(root13, width=50)

    b11 = Button(root13, text='Добавить', bg='black', fg='white', width=10, command=getbook)

    lab11.pack(padx=10, pady=10, side=TOP)
    b11.pack(pady=10)
    code.pack(padx=10, pady=10)
    root13.mainloop()


def yourbasket():
    root13 = Tk()
    root13.geometry('240x240')
    root13.title('кол-во книг')
    def buybook():
        global emailcook
        answerline = SQLlib.lineforbasket(emailcook)
        amountrt = SQLlib.amountreturn(answerline)
        codaccout = SQLlib.acouting(amountrt)
        SQLlib.upgradeamount(codaccout, amountrt)

        numret = SQLlib.returnnumber(emailcook)
        SQLlib.upgradenumber_books_purchased(amountrt, numret)
        SQLlib.upgradeloyalty_system(amountrt, numret)
        SQLlib.destroiorders(answerline)
        root13.destroy()

    def delorder():
        global emailcook

        answerline = SQLlib.lineforbasket(emailcook)
        SQLlib.destroiorders(answerline)
        root13.destroy()

    lab11 = Label(root13, text="Мой заказ")
    global emailcook

    num = SQLlib.lineforbasket(emailcook)
    print(num)


    # определяем данные для отображения

    persons = SQLlib.printorderlbasket(num)

    # определяем столбцы
    columns = ("namebook", "amount", "price_one_copy", "result")

    one = ttk.Treeview(root13, columns=columns, show="headings")
    one.pack(fill=BOTH, expand=1)

    # определяем заголовки с выпавниваем по левому краю
    one.heading("namebook", text="Название книги", anchor=W)
    one.heading("amount", text="Количество", anchor=W)
    one.heading("price_one_copy", text="Цена одного экз", anchor=W)
    one.heading("result", text="Общая цена", anchor=W)

    # настраиваем столбцы
    one.column("#1", stretch=NO, width=100)
    one.column("#2", stretch=NO, width=150)
    one.column("#3", stretch=NO, width=100)
    one.column("#4", stretch=NO, width=100)

    # добавляем данные
    for person in persons:
         one.insert("", END, values=person)

    b12 = Button(root13, text='очистить', bg='black', fg='white', width=10, command=delorder)

    lab11.pack(padx=10, pady=10, side=TOP)

    b12.pack(pady=10)

    b11 = Button(root13, text='купить', bg='black', fg='white', width=10, command=buybook)

    lab11.pack(padx=10, pady=10, side=TOP)

    b11.pack(pady=10)


    root13.mainloop()



root = Tk()
root.title('Книжный магазин')
Label(text="Добро пожаловать в книжный магазин").pack()
Label(text="Зарегистрируйтесь или залогинтесь").pack()
b1 = Button(text="Регистрация", command=registration)
b2 = Button(text="Логин", command=login)
b1.pack()
b2.pack()
root.mainloop()


