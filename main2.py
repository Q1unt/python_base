import email

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
    def add_client(conn, name, surname, email, phones=None):
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

    # def change_client(conn, name=None, surname=None, email=None, phones=None, client__id):
    #     postgres_insert_query = """UPDATE client SET name=%s surname=%s email=%s phones=%s
    #                                 WHERE id=%s"""
    #     record_to_insert = ( name, surname, email, phones, client__id)
    #     cur.execute(postgres_insert_query, record_to_insert)
    #     conn.commit()

    # def delete_phone(conn, add_id):
    #     postgres_insert_query = """ DELETE FROM number_phone
    #                                 WHERE id=%s"""
    #     record_to_insert = (add_id)
    #     cur.execute(postgres_insert_query, record_to_insert)
    #     conn.commit()
    #
    # def delete_client(conn, client__id):
    #     postgres_insert_query = """ DELETE FROM client
    #                                 WHERE id=%s"""
    #     record_to_insert = client__id
    #     cur.execute(postgres_insert_query, record_to_insert)
    #     conn.commit()

    # Функция на создание бд
    create_db(conn)

    # Функция на создание клиента
    client_id = add_client(conn, 'Дима', 'Кукушкин', 'dima.@mail.ru', None)
    client_id = add_client(conn, 'рома', 'буцко', 'dima.namitka.@gmail.com', None)
    client_id = add_client(conn, 'влад', 'беляев', 'vlad.03.@mail.ru', None)
    client_id = add_client(conn, 'влад', 'игнатьев', 'roma.23.@mail.ru', None)
    #
    add_id = add_phone(conn, '89617655565', 'билайн',)
    add_id = add_phone(conn, '89624567316', 'билайн')
    add_id = add_phone(conn, '89282655781', 'мтс')
    add_id = add_phone(conn, '89182345399', 'мегафон')

    update_client(conn, 1, 1)
    update_client(conn, 2, 2)
    update_client(conn, 3, 3)
    # update_client(conn, 4, 3)

    # delete_phone(conn, [1])


    # change_client(conn, 'ilya', 'журат', 'ilya.01.@mail.ru', '89614465612', 1)
    # delete_phone(conn, [2])
    # delete_phone(conn, [3])
    # delete_client(conn, [2])



    # cur.execute("""
    #         DELETE FROM client WHERE id=%s;
    #         """, (,))
    # conn.commit()
    # cur.execute("""
    #         SELECT * FROM client;
    #         """)
    # print(cur.fetchall())

    cur.execute("""
                SELECT * FROM client;
                """)
    print(cur.fetchall())
    cur.execute("""
                SELECT * FROM number_phone;
                """)
    print(cur.fetchall())

conn.close()