import psycopg

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

if __name__ == "__main__":
    with psycopg.connect(DATABASE_URL) as conn, conn.cursor() as cur:
        izena = str(input("Sartu izena: "))
        abizena = str(input("Sartu abizena: "))
        
        cur.execute("""
                    INSERT INTO participants (name, surname)
                    VALUES (%s, %s)
                    RETURNING id, name, surname
                    """,
                    (izena, abizena))
        
        participant = cur.fetchone()
        
        print(participant)