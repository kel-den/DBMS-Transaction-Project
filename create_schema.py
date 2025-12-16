from db_connect import connect_db

def create_schema():
    conn = connect_db()
    if conn is None:
        return
    
    cur = conn.cursor()
    
    try:
        print("\nDropping old tables (if they exist)...")
        cur.execute("DROP TABLE IF EXISTS Stock CASCADE;")
        cur.execute("DROP TABLE IF EXISTS Product CASCADE;")
        cur.execute("DROP TABLE IF EXISTS Depot CASCADE;")

        print("Creating tables...")

        cur.execute("""
            CREATE TABLE Product (
                prodID VARCHAR(10) PRIMARY KEY,
                pname  VARCHAR(50),
                price  DECIMAL(10,2)
            );
        """)

        cur.execute("""
            CREATE TABLE Depot (
                depotID VARCHAR(10) PRIMARY KEY,
                addr    VARCHAR(100),
                volume  INTEGER
            );
        """)

        cur.execute("""
            CREATE TABLE Stock (
                prodID  VARCHAR(10),
                depotID VARCHAR(10),
                quantity INTEGER,
                PRIMARY KEY (prodID, depotID),
                FOREIGN KEY (prodID) REFERENCES Product(prodID) ON DELETE CASCADE, ON UPDATE CASCADE,
                FOREIGN KEY (depotID) REFERENCES Depot(depotID) ON DELETE CASCADE, ON UPDATE CASCADE
            );
        """)

        print("Inserting sample data...")

        cur.execute("""
            INSERT INTO Product VALUES
            ('p1', 'tape', 2.5),
            ('p2', 'tv', 250),
            ('p3', 'vcr', 80);
        """)

        cur.execute("""
            INSERT INTO Depot VALUES
            ('d1', 'New York', 9000),
            ('d2', 'Syracuse', 6000),
            ('d3', 'Chicago', 2000);
        """)

        cur.execute("""
            INSERT INTO Stock VALUES
            ('p1', 'd1', 100),
            ('p1', 'd2', 50),
            ('p2', 'd1', 300),
            ('p3', 'd1', 200),
            ('p3', 'd3', 250);
        """)

        conn.commit()
        print("\nSchema created and sample data inserted successfully!")

    except Exception as e:
        print("Error creating schema:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    create_schema()
