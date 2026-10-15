import psycopg

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

if __name__ == "__main__":

    with psycopg.connect(DATABASE_URL) as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM participants")
        rows = cur.fetchall()

    print(rows)