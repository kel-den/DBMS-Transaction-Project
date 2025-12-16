import psycopg2

def connect_db():
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(
            dbname='DBMSproject',
            user='postgres',
            password='1429',
            host='localhost',
            port='5433'
        )
        print("Database connection successful")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None