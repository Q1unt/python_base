import psycopg2

conn = psycopg2.connect(database="client_base", user="postgres", password="x26n06dimon26")
with conn.cursor() as cur:
    def create_db(conn):
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
        conn.commit()


    # добавление имени клиента, фамилии и емайла
    def add_client(conn, name, surname, email, phones_id=None):
        postgres_insert_query = """ INSERT INTO client (name, surname, email)
                                VALUES (%s,%s,%s)"""
        record_to_insert = (name, surname, email)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    def add_phone(conn, number, mobile_operator):
        postgres_insert_query = """ INSERT INTO number_phone(number, mobile_operator )
                                  VALUES (%s,%s) """
        record_to_insert = (number, mobile_operator)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    def update_client(conn, phones_id, client_id):
        postgres_insert_query = """UPDATE client SET phones_id=%s
                                    WHERE id=%s"""
        record_to_insert = (phones_id, client_id)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    def change_client(conn, client_id, name=None, surname=None, email=None, phones_id=None):
        postgres_insert_query = """UPDATE client SET name=%s, surname=%s, email=%s, phones_id=%s
                                WHERE id=%s;"""
        record_to_insert = (client_id, name, surname, email, phones_id)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    def delete_client(conn, client_id):
        postgres_insert_query = """ DELETE FROM client
                                    WHERE id=%s"""
        record_to_insert = (client_id)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    def delete_phone(conn, add_id):
        postgres_insert_query = """ DELETE FROM number_phone
                                    WHERE id=%s"""
        record_to_insert = (add_id)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    def find_client(cur, name=None, surname=None, email=None, phones_id=None):

        cur.execute("""SELECT * FROM client
                    where name=%s""", (name,))
        cur.execute("""SELECT * FROM client
                    where surname=%s""", (surname,))
        cur.execute("""SELECT * FROM client
                    where email=%s""", (email,))
        cur.execute("""SELECT * FROM client
                    where phones_id=%s""", (phones_id,))

        return cur.fetchall()

    # Функция на создание бд
    create_db(conn)

    # Функция по заполнению клиентов
    client_id = add_client(conn, 'дима', 'кукушкин', 'dima.@mail.ru', None)
    client_id = add_client(conn, 'рома', 'буцко', 'dima.namitka.@gmail.com', None)
    client_id = add_client(conn, 'рома', 'буцко', 'dima.namitka.@gmail.com', None)
    client_id = add_client(conn, 'влад', 'беляев', 'vlad.03.@mail.ru', None)
    client_id = add_client(conn, 'влад', 'игнатьев', 'roma.23.@mail.ru', None)
    #
    #Функция по заполнению таблицы номеров
    add_id = add_phone(conn, '89617655565', 'билайн',)
    add_id = add_phone(conn, '89624567316', 'билайн')
    add_id = add_phone(conn, '89282655781', 'мтс')
    add_id = add_phone(conn, '89182345399', 'мегафон')

    # Функция по удалению клиента
    update_client(conn, 1, 1)
    update_client(conn, 2, 2)
    update_client(conn, 3, 3)
    update_client(conn, 4, 4)

    #Функция позволяющая найти клиента по его данным
    print(find_client(cur, 'рома', 'буцко', 'dima.namitka.@gmail.com', 1))

    # Функция по удалению номера
    delete_client(conn, [2])
    delete_client(conn, [3])
    delete_phone(conn, [2])
    delete_phone(conn, [3])

    #Функция позволяющая изменить клиенту данные
    change_client(conn, 'ilya', 'журак', 'dima.ilya.@mail.ru', 4, 5)

conn.close()
