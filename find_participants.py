import psycopg

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

if __name__ == "__main__":
    participant_id = int(input("Sartu erabiltzailearen ID-a: "))
    
    conn = psycopg.connect(DATABASE_URL)
    
    cur = conn.cursor()
    
    cur.execute(
                """
                SELECT * FROM participants
                WHERE id = %s
                """,
                (participant_id,))
    
    participant = cur.fetchone()
    
    if(participant):
        print(f"Participant ID: {participant[0]}")
        print(participant)
    else:
        print("Participant ID: 99")
        print("Ez da aurkitu")
    