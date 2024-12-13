import sqlite3

def query_database(protocol=None, min_length=None, max_length=None):
    """
    Query the database with different combinations of protocol and length.

    Args:
        protocol (str, optional): The protocol to filter by (e.g., "UDP", "TCP", "ICMP").
        min_length (int, optional): The minimum packet length to filter by.
        max_length (int, optional): The maximum packet length to filter by.
    """
    try:
        conn = sqlite3.connect("network_data.db")  # Adjust to your database name
        cursor = conn.cursor()

        # Build the query dynamically based on provided parameters
        query = "SELECT * FROM traffic_records WHERE 1=1"
        params = []

        if protocol:
            query += " AND protocol = ?"
            params.append(protocol)

        if min_length is not None:
            query += " AND length >= ?"
            params.append(min_length)

        if max_length is not None:
            query += " AND length <= ?"
            params.append(max_length)

        print("Executing query:", query)
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Display results
        if results:
            print("\nQuery Results:")
            for row in results:
                print(f"Time: {row[0]}, Protocol: {row[1]}, Length: {row[2]}, Source: {row[3]}, Destination: {row[4]}")
            print(f"\n{len(results)} records found for the given parameters.")
        else:
            print("\nNo records found for the given parameters.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("Querying Traffic Records Database\n")

    # Example usage
    print("Query 1: Protocol = 'UDP'")
    query_database(protocol="UDP")

    print("\nQuery 2: Protocol = 'TCP', Min Length = 50")
    query_database(protocol="TCP", min_length=50)

    print("\nQuery 3: Min Length = 50, Max Length = 85")
    query_database(min_length=50, max_length=500)

