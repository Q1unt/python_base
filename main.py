import psycopg2

def create_db():
    cur.execute("""
    DROP TABLE client;
    DROP TABLE number_phone;
    """)

    # создание таблицы
    cur.execute("""
    CREATE TABLE IF NOT EXISTS number_phone(
        id SERIAL PRIMARY KEY,
        number VARCHAR (40),
        mobile_operator VARCHAR(50)
    );
    CREATE TABLE IF NOT EXISTS client(
        id SERIAL PRIMARY KEY,
        name VARCHAR (50) NOT NULL,
        surname VARCHAR (50) NOT NULL,
        email VARCHAR (200) NOT NULL,
        phones_id INTEGER REFERENCES number_phone(id)
    );
    """)

# добавление имени клиента, фамилии и емайла
def add_client(name, surname, email, phones_id=None):
    postgres_insert_query = """ INSERT INTO client (name, surname, email)
                            VALUES (%s,%s,%s)"""
    record_to_insert = (name, surname, email)
    cur.execute(postgres_insert_query, record_to_insert)

def add_phone(number, mobile_operator):
    postgres_insert_query = """ INSERT INTO number_phone(number, mobile_operator )
                              VALUES (%s,%s) """
    record_to_insert = (number, mobile_operator)
    cur.execute(postgres_insert_query, record_to_insert)

def update_client(phones_id, client_id):
    postgres_insert_query = """UPDATE client SET phones_id=%s
                                WHERE id=%s"""
    record_to_insert = (phones_id, client_id)
    cur.execute(postgres_insert_query, record_to_insert)

def change_client(client_id, name=None, surname=None, email=None):
    if name != None:
        cur.execute("""
           UPDATE client SET name=%s
           WHERE id =%s;
           """, (client_id, name))
    if surname != None:
        cur.execute("""
            UPDATE client SET surname=%s
            WHERE id =%s;
            """, (client_id, surname))
    if email != None:
        cur.execute("""
            UPDATE client SET email=%s
            WHERE id =%s;
            """, (client_id, email))


def delete_client(client_id):
    postgres_insert_query = """ DELETE FROM client
                            WHERE id=%s"""
    record_to_insert = (client_id)
    cur.execute(postgres_insert_query, record_to_insert)

def delete_phone(add_id):
    postgres_insert_query = """ DELETE FROM number_phone
                                WHERE id=%s"""
    record_to_insert = (add_id)
    cur.execute(postgres_insert_query, record_to_insert)

def find_client(cur, name=None, surname=None, email=None, phones_id=None):
    cur.execute("""SELECT * FROM client
                where name=%s or surname=%s or email=%s or phones_id=%s""", (name, surname, email, phones_id,))

    print(cur.fetchall())

conn = psycopg2.connect(database="client_base", user="postgres", password="x26n06dimon26")
with conn.cursor() as cur:

    # Функция на создание бд
    create_db()

    # Функция по заполнению клиентов
    client_id = add_client('дима', 'кукушкин', 'dima.@mail.ru', None)
    client_id = add_client('рома', 'буцко', 'dima.namitka.@gmail.com', None)
    client_id = add_client('рома', 'буцко', 'dima.namitka.@gmail.com', None)
    client_id = add_client('влад', 'беляев', 'vlad.03.@mail.ru', None)
    client_id = add_client('влад', 'игнатьев', 'roma.23.@mail.ru', None)

    #Функция по заполнению таблицы номеров
    add_id = add_phone('89617655565', 'билайн',)
    add_id = add_phone('89624567316', 'билайн')
    add_id = add_phone('89282655781', 'мтс')
    add_id = add_phone('89182345399', 'мегафон')

    # Функция по удалению клиента
    update_client(1, 1)
    update_client(2, 2)
    update_client(3, 3)
    update_client(4, 4)

    # # Функция позволяющая найти клиента по его данным
    find_client(cur, 'дима', None, None, None)

    # Функция по удалению номера
    delete_client([2])
    delete_client([3])
    delete_phone([2])
    delete_phone([3])
    # #
    # # # Функция позволяющая изменить клиенту данные
    change_client('ilya', 4)

    cur.execute("""
            SELECT * FROM client;
            """)
    print(cur.fetchall())

    cur.execute("""
            SELECT * FROM number_phone;
            """)
    print(cur.fetchall())

conn.close()
