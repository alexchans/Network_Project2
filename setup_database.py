import sqlite3

def setup_database():
    """
    Create the network_data database and the traffic_records table.
    """
    try:
        # Connect to SQLite database
        conn = sqlite3.connect("network_data.db")  # Database name
        cursor = conn.cursor()

        # Create the traffic_records table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS traffic_records (  -- Table name
                time TEXT,
                protocol TEXT,
                length INTEGER,
                source TEXT,
                destination TEXT
            )
        """)

        conn.commit()
        print("Database and table created successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    setup_database()
