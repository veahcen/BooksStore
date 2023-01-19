import psycopg2
#глобальные переменные

#глобальные переменные

def conectBase():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='db0091_15', user='st0091', password='qwerty91',  host="172.20.8.18", port="5432")
        # создание объекта курсора
        cur = conn.cursor()
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Сбой подключения')
    # возвращаем объекты conn и cut
    # для использования позже
    return conn, cur

def printTable():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.user')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def printDataUser(data):
    # iterating over all the
    # rows in the table
    for row in data:
        # printing the columns
        print(row[0], '|', row[1], '|', row[2], '|', row[3], '|', row[4], '|', row[5], '|', row[6], '|', row[7], '|',  row[8], "\n")





def loginUser(log, passw):
    conn, cur = conectBase()
    try:
        cur.execute('select rolle from bookstore.user where email = \'' + log + '\' and passwordd = \'' + passw + '\';')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def numusercheck(log):
    conn, cur = conectBase()
    try:
        cur.execute('select number from bookstore.user where email = \'' + log + '\';')
        data2 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data2:
        number1 = row[0]
    return number1





def maxOrdId():
    conn, cur = conectBase()
    try:
        cur.execute('SELECT MAX(order_id) FROM bookstore.basket;')
        conn.commit()
        data3 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data3:
        number2 = row[0]
    return number2

def maxOrd():
    conn, cur = conectBase()
    try:
        cur.execute('SELECT MAX(basket.order) FROM bookstore.basket;')
        conn.commit()
        data4 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data4:
        number5 = row[0]
    return number5

def maxIdOrdOrderlines():
    conn, cur = conectBase()
    try:
        cur.execute('SELECT MAX(orderlines.id_order) FROM bookstore.orderlines;')
        conn.commit()
        data7 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data7:
        number9 = row[0]
    return number9

def createnewbasket(code, num):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.basket VALUES ('
                     + str(code) + ', CURRENT_DATE,' + str(num) + ');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def lineforbasket(mail):
    conn, cur = conectBase()
    try:
        cur.execute('select basket.order_id from bookstore.basket where basket.order = ' +
                    '(select number from bookstore.user where email = \'' + str(mail) + '\' );')
        conn.commit()
        data10 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data10:
        number11 = row[0]
    return number11



def maxNum():
    conn, cur = conectBase()
    try:
        cur.execute('SELECT MAX(number)FROM bookstore.user;')
        conn.commit()
        data = cur.fetchall()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data:
        number = row[0]
    return number

num11 = maxNum()

def insertintoorderlineszakaz(id_order, amount, book, basketnum):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.orderlines (id_order, amount, book, basketnum) VALUES ('
                    + str(id_order + 1) + ',' + str(amount) + ',' + str(book) + ',' + str(basketnum) + ');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def regustrationUser(firstName, lastName, password, age, email):
    conn, cur = conectBase()
    rolle = 'false'
    numbooks = 0
    loya_sys = 0.0000000
    try:

        cur.execute('INSERT INTO bookstore.user (number, rolle, firstname, lastname, passwordd, number_books_purchased, age, loyalty_system, email) VALUES ('
                     + str(num11 + 1) + ',' + str(rolle) + ',\'' + str(firstName) + '\',\'' + str(lastName) + '\',\'' + str(password) + '\',' + str(numbooks) + ',' + str(age) + ',' + str(loya_sys) + ',\'' + str(email) + '\');')
        conn.commit()
        print('gotovo')
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()



def printTableAccountBooks():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.accountingbooks')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def printTableAuthors():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.authors')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def printTableBasket():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.basket')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def printTableBooks():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.books')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data


def printTableBooksAllInfo():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.allinfobook')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data


def printTableOrderLines():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.orderlines')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def printTablePublishingHouse():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.publishinghouse')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def printTableTypeofLiterature():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.typeofliterature')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def printTableUser():
    conn, cur = conectBase()
    try:
        cur.execute('select * from bookstore.user')
        data = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data

def inserttablefunk(code, amoun, daterelase):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.accountingbooks (code_accounting, amount, receipt_date) VALUES ('
                     + str(code) + ',' + str(amoun) + ',\'' + str(daterelase) + '\');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def insertauthorsfunk(code, firstname, lastname):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.authors (code_accounting, amount, receipt_date) VALUES ('
                     + str(code) + ',\'' + str(firstname) + '\',\'' + str(lastname) + '\');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def insertbasketfunk(code, date, order):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.basket (code_accounting, amount, receipt_date) VALUES ('
                     + str(code) + ',\'' + str(date) + '\',' + str(order) + ');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def insertbooksfunk(idbook, namebk, pricecopy, releasedate, circulat, author, published, literaturetype):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.books (id_book, namebook, price_one_copy, release_date, circulation, author, published, literaturetype) VALUES ('
                     + str(idbook) + ',\'' + str(namebk) + '\',' + str(pricecopy) + ',\'' + str(releasedate) + '\',' + str(circulat) + ',' + str(author) + ',' + str(published) + ',' + str(literaturetype) + ');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def insertorderlinesfunk(id_order, amount, book, basketnum):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.orderlines (id_order, amount, book, basketnum) VALUES ('
                     + str(id_order) + ',' + str(amount) + ',' + str(book) + ',' + str(basketnum) + ');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()


def insertpublishhousefunk(publishercode, publishernazv, city):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.publishinghouse (publisher_code, publisher_nazv, city) VALUES ('
                     + str(publishercode) + ',\'' + str(publishernazv) + '\',\'' + str(city) + '\');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def inserttypeofliteraturefunk(typecode, typeliterature):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.typeofliterature (type_code, type_literature) VALUES ('
                     + str(typecode) + ',\'' + str(typeliterature) + '\');')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def insertuseradmfunk(number1, rolle, firstName, lastName,numberbooks, password, age, loya_sys, email):
    conn, cur = conectBase()
    try:
        cur.execute('INSERT INTO bookstore.user (number, rolle, firstname, lastname, passwordd, number_books_purchased, age, loyalty_system, email) VALUES ('
                     + str(number1) + ',' + str(rolle) + ',\'' + str(firstName) + '\',\'' + str(lastName) + '\',\'' + str(password) + '\',' + str(numberbooks) + ',' + str(age) + ',' + str(loya_sys) + ',\'' + str(email) + '\');')
        conn.commit()
        print('gotovo')
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()




def edittabletypeofliterature1(num1, num2, num3):
    conn, cur = conectBase()
    try:
        cur.execute('UPDATE bookstore.typeofliterature SET type_code = ' + num1 + ',' + 'type_literature = \'' + num2 + '\'' +
        ' WHERE type_code = ' + num3 +';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()


def edittableaccountbooks1(num1, num2, num3, num4):
    conn, cur = conectBase()
    try:
        cur.execute(
            'UPDATE bookstore.accountingbooks SET code_accounting = ' + num1 + ',' + 'amount = ' + num2 + ',receipt_date = \'' + num3 + '\'' +
            ' WHERE code_accounting = ' + num4 + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def edittableauthors1(num1, num2, num3, num4):
    conn, cur = conectBase()
    try:
        cur.execute(
            'UPDATE bookstore.authors SET code_author = ' + num1 + ',' + 'firstname = \'' + num2 + '\',lastname = \'' + num3 + '\'' +
            ' WHERE code_author = ' + num4 + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def edittablebasket1(num1, num2, num3, num4):
    conn, cur = conectBase()
    try:
        cur.execute(
            'UPDATE bookstore.basket SET order_id = ' + num1 + ',' + 'datte = \'' + num2 + '\',order = ' + num3 +
            ' WHERE order_id = ' + num4 + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def edittablebooks1(idbook, namebk, pricecopy, releasedate, circulat, author, published, literaturetype, code):
    conn, cur = conectBase()
    try:
        cur.execute(
            'UPDATE bookstore.books SET id_book =  ' + str(idbook) + ', namebook = \'' + str(namebk) + '\',' + 'price_one_copy = ' + str(pricecopy) + ',' +
            'release_date = ' + '\'' + str(releasedate) + '\',' + 'circulation = ' + str(circulat) + ',' + 'author = ' + str(author) + ', published = ' +
            str(published) + ', literaturetype = ' + str(literaturetype) + ' WHERE id_book = ' + code + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def edittableorderlines1(num1, num2, num3, num4, num5):
    conn, cur = conectBase()
    try:
        cur.execute(
            'UPDATE bookstore.orderlines SET id_order = ' + num1 + ',' + 'amount = ' + num2 + ',book = ' + num3 + ',basketnum =' + num4 +
            ' WHERE id_order = ' + num5 + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def edittablepublishhouse1(num1, num2, num3, num4):
    conn, cur = conectBase()
    try:
        cur.execute(
            'UPDATE bookstore.publishinghouse SET publisher_code = ' + num1 + ',' + 'publisher_nazv = \'' + num2 + '\',city = \'' + num3 + '\'' +
            ' WHERE publisher_code = ' + num4 + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def edittableuseradm1(number1, rolle, firstName, lastName,numberbooks, password, age, loya_sys, email, num4):
    conn, cur = conectBase()
    try:
        cur.execute('UPDATE bookstore.books SET number = ' + str(number1) + ', rolle = ' + str(rolle) + ', firstname = ' + '\'' + str(firstName) + '\', lastname = ' +
                    '\'' + str(lastName) + '\', passwordd = ' + '\'' + str(password) + '\'' + ', number_books_purchased = ' + str(numberbooks) + ', age = ' + str(age) +
                    ', loyalty_syste = ' + str(loya_sys) + ', email = \'' + str(email) + '\' ' + ' WHERE number = ' + num4 + ';')
        conn.commit()
        print('gotovo')
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()


def deleteData(tableName, n, num):
    conn, cur = conectBase()
    try:
        cur.execute('DELETE FROM "bookstore".' + tableName + ' WHERE "' + tableName + '"."' + n + '" = ' + num)
        conn.commit()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()


def printorderlbasket(num):
    conn, cur = conectBase()
    try:
        cur.execute('select books.namebook, orderlines.amount, books.price_one_copy, orderlines.amount * books.price_one_copy AS result' +
                    ' from bookstore.orderlines, bookstore.books ' +
                    'where orderlines.book = books.id_book and orderlines.basketnum = ' + str(num) + ';')

        data20 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    return data20

def returnnumber(mal):
    conn, cur = conectBase()
    try:
        cur.execute('select number from bookstore.user where email = \'' + str(mal) + '\';')
        conn.commit()
        data23 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data23:
        number17 = row[0]
    return number17

def amountreturn(numbr):
    conn, cur = conectBase()
    try:
        cur.execute('select orderlines.amount from  bookstore.orderlines where orderlines.basketnum =' + str(numbr) + ';')
        data30 = cur.fetchall()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data30:
        number13 = row[0]
    return number13
    return number13

def upgradeamount(codeeaccout, amoutt):
    conn, cur = conectBase()
    try:
        cur.execute('update bookstore.accountingbooks set amount = amount - ' + str(amoutt) +
                    ' where accountingbooks.code_accounting = ' + str(codeeaccout) + ';' )
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def upgradenumber_books_purchased(amounn, num):
    conn, cur = conectBase()
    try:
        cur.execute('update bookstore.user set number_books_purchased = number_books_purchased + ' + str(amounn) +
                    'where number = ' + str(num) + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def upgradeloyalty_system(amounn, num):
    conn, cur = conectBase()
    try:
        cur.execute('update bookstore.user set loyalty_system = loyalty_system + ' + str(0.0000001 * amounn) +
                    'where number = ' + str(num) + ';')
        conn.commit()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def acouting(amou):
    conn, cur = conectBase()
    try:
        cur.execute('select accountingbooks.code_accounting from bookstore.accountingbooks, bookstore.orderlines' +
                        ' where code_accounting = (select circulation from bookstore.books where ' +
						 'orderlines.basketnum = ' + str(amou) + 'and orderlines.book = books.id_book);')

        data21 = cur.fetchall()

    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data21:
        number12 = row[0]
    return number12

def destroiorders(num):
    conn, cur = conectBase()
    try:
        cur.execute('delete from bookstore.orderlines where orderlines.basketnum = ' + str(num) + ';')
        conn.commit()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()

def createPasswHash(passw):
    conn, cur = conectBase()
    try:
        cur.execute('SELECT MD5(\'' + str(passw) + '\'); ')
        data211 = cur.fetchall()
        conn.commit()
    except Exception as ex:
        print('error', ex)
    finally:
        if conn:
            cur.close()
            conn.close()
    for row in data211:
        number121 = row[0]
    return number121


