import psycopg

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

def main():
    participant_id = int(input("Sartu erabiltzailearen ID-a: "))
    new_name = str(input("Sartu izena: "))
    new_surname = str(input("Sartu abizena: "))

    with psycopg.connect(DATABASE_URL) as conn, conn.cursor() as cur:
        cur.execute(
            """
            UPDATE participants
            SET name = %s, surname = %s
            WHERE id = %s
            RETURNING id, name, surname
            """,
            (new_name, new_surname, participant_id)
        )
        
        updated_participant = cur.fetchone()
        
        if updated_participant:
            print(f"Updated Participant ID: {updated_participant[0]}")
            print(updated_participant)
        else:
            print(f"Participant ID: {participant_id}")
            print("Ez da aurkitu")

if __name__ == "__main__":
    main()