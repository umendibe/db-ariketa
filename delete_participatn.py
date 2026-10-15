import psycopg

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

def main():
    participant_id = int(input("Sartu erabiltzailearen ID-a: "))

    with psycopg.connect(DATABASE_URL) as conn, conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM participants
            WHERE id = %s
            RETURNING id, name, surname
            """,
            (participant_id,)
        )
        
        deleted_participant = cur.fetchone()
        
        if deleted_participant:
            print(f"Deleted Participant ID: {deleted_participant[0]}")
            print(deleted_participant)
        else:
            print(f"Participant ID: {participant_id}")
            print("Ez da aurkitu")

if __name__ == "__main__":
    main()