import sqlite3

# def create_connection(db_file):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_file)
#     except sqlite3.Error as e:
#         print(e)
#     return connection

# def create_table(connection, sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql)
#     except sqlite3.Error as error:
#         print(error)

def create_table(db_file, sql):
    with sqlite3.connect(db_file) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
        except sqlite3.Error as error:
            print(error)

def insert_product(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''INSERT INTO products (product_title, price, quantity) 
                        VALUES (?, ?, ?)
            '''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

def update_products(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''UPDATE products SET price = ?, quantity = ? WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)  # (2300.0, False, 2)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

def delete_products(db_file, id):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''DELETE FROM products WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except sqlite3.Error as error:
            print(error)

def select_all_products(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

def select_products_by_limit(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products WHERE price < 100.00 AND quantity > 5'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

def select_all_products_search(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            need = input('Введите название нужного вам продукта: ')
            sql = '''SELECT * FROM products WHERE product_title LIKE need% '''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

db_name = 'hw.db'

sql_to_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

# my_connection = create_connection(db_name)
# if my_connection is not None:
#     print('Successfully connected to database')
# here will be operations with DB
# create_table(my_connection, sql_to_create_products_table)
# my_connection.close()
# create_table(db_name, sql_to_create_products_table)

# insert_product(db_name, ("Пайтон Кола", 45.0, 23))
# insert_product(db_name, ("Джава Пепси", 44.10, 23))
# insert_product(db_name, ("Пайтон Кола без сахара", 26.00, 20))
# insert_product(db_name, ("Пельмени ПРЕМИУМ", 999.99, 22))
# insert_product(db_name, ("Пицца от Альфреда", 200, 60))
# insert_product(db_name, ("Футболка НАЙК", 1200.00, 24))
# insert_product(db_name, ("Игрушечный Нож от компании TaleUnder", 215.14, 43))
# insert_product(db_name, ("плюшевый золотой медведь", 200.00, 26))
# insert_product(db_name, ("Кроссовки не китайские 100%", 2300.00, 100))
# insert_product(db_name, ("Памперсы 4 размер", 310.00, 26))
# insert_product(db_name, ("влажные салфетки", 47.00, 78))
# insert_product(db_name, ("Большое мыло с запахом бананов", 200.00, 40))
# insert_product(db_name, ("Обычные салфетки", 100.00, 29))
# insert_product(db_name, ("туалетная бумага", 20.00, 20))
# insert_product(db_name, ("мороженное ванильное", 20, 26))
# insert_product(db_name, ("Макароны", 60, 34))

update_products(db_name, (95, 57, 4))
delete_products(db_name, 16)
select_all_products(db_name)
print((select_products_by_limit(db_name)))
select_all_products_search(db_name)
