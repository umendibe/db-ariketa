import psycopg

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

if __name__ == "__main__":

    conn = psycopg.connect(DATABASE_URL)

    cur = conn.cursor()

    cur.execute("SELECT * FROM participants")

    rows = cur.fetchall()

    print(rows)