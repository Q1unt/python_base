import psycopg2


conn = psycopg2.connect(database="client_base", user="postgres", password="x26n06dimon26")
with conn.cursor() as cur:
    cur.execute("""
    DROP TABLE client;
    DROP TABLE number_phone;
    """)

    # создание таблицы
    cur.execute("""
        CREATE TABLE IF NOT EXISTS number_phone(
            id SERIAL PRIMARY KEY,
            number_phone INTEGER
        );
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            id SERIAL PRIMARY KEY,
            name VARCHAR (50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            email VARCHAR (200) NOT NULL,
            number_phone_id INTEGER REFERENCES number_phone(id)
        );
        """)
    conn.commit()

conn.close()