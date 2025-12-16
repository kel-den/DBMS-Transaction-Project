
from db_connect import connect_db

# -----------------------------
# Transaction 1
# -----------------------------
def transaction_1():
    """
    Delete product p1 from Product AND Stock.
    Must delete from Stock first because of FK.
    """
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    try:
        print("\nRunning Transaction 1: Delete product p1...")

        # delete from Stock first
        cur.execute("DELETE FROM Stock WHERE prodID = 'p1';")

        # delete from Product
        cur.execute("DELETE FROM Product WHERE prodID = 'p1';")

        conn.commit()
        print("Transaction 1 completed successfully.\n")

    except Exception as e:
        conn.rollback()
        print("Transaction 1 FAILED:", e)

    finally:
        cur.close()
        conn.close()


# -----------------------------
# Transaction 2
# -----------------------------
def transaction_2():
    """
    Delete depot d1 from Depot AND Stock.
    Must delete from Stock first.
    """
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    try:
        print("\nRunning Transaction 2: Delete depot d1...")

        # delete from Stock first
        cur.execute("DELETE FROM Stock WHERE depotID = 'd1';")

        # delete from Depot
        cur.execute("DELETE FROM Depot WHERE depotID = 'd1';")

        conn.commit()
        print("Transaction 2 completed successfully.\n")

    except Exception as e:
        conn.rollback()
        print("Transaction 2 FAILED:", e)

    finally:
        cur.close()
        conn.close()


# -----------------------------
# Transaction 3
# -----------------------------
def transaction_3():
    """
    Rename product p1 → p10 in BOTH Product and Stock.
    Must update Stock first, then Product (FK update logic).
    """
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    try:
        print("\nRunning Transaction 3: Rename product p1 to p10...")

        # update Stock first
        cur.execute("UPDATE Stock SET prodID = 'p10' WHERE prodID = 'p1';")

        # update Product table  
        cur.execute("UPDATE Product SET prodID = 'p10' WHERE prodID = 'p1';")

        conn.commit()
        print("Transaction 3 completed successfully.\n")

    except Exception as e:
        conn.rollback()
        print("Transaction 3 FAILED:", e)

    finally:
        cur.close()
        conn.close()


# -----------------------------
# Transaction 4
# -----------------------------
def transaction_4():
    """
    Rename depot d1 → dd1 in BOTH Depot and Stock.
    Update depot, on  update cascade automatically update stock.
    """
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    try:
        print("\nRunning Transaction 4: Rename depot d1 to dd1...")

       
        # update Depot
        cur.execute("UPDATE Depot SET depotID = 'dd1' WHERE depotID = 'd1';")
        #ON UPDATE CASCADE automatically updates all Stock records !
        conn.commit()
        print("Transaction 4 completed successfully.\n")

    except Exception as e:
        conn.rollback()
        print("Transaction 4 FAILED:", e)

    finally:
        cur.close()
        conn.close()


# -----------------------------
# Transaction 5
# -----------------------------
def transaction_5():
    """
    Add product (p100, cd, 5) and Stock (p100, d2, 50).
    """
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    try:
        print("\nRunning Transaction 5: Insert new product and stock...")

        cur.execute("""
            INSERT INTO Product VALUES ('p100', 'cd', 5);
        """)

        cur.execute("""
            INSERT INTO Stock VALUES ('p100', 'd2', 50);
        """)

        conn.commit()
        print("Transaction 5 completed successfully.\n")

    except Exception as e:
        conn.rollback()
        print("Transaction 5 FAILED:", e)

    finally:
        cur.close()
        conn.close()


# -----------------------------
# Transaction 6
# -----------------------------
def transaction_6():
    """
    Add depot (d100, Chicago, 100) AND stock entry (p1, d100, 100).
    """
    conn = connect_db()
    if conn is None: return
    cur = conn.cursor()

    try:
        print("\nRunning Transaction 6: Insert depot d100 and stock...")

        cur.execute("""
            INSERT INTO Depot VALUES ('d100', 'Chicago', 100);
        """)

        cur.execute("""
            INSERT INTO Stock VALUES ('p1', 'd100', 100);
        """)

        conn.commit()
        print("Transaction 6 completed successfully.\n")

    except Exception as e:
        conn.rollback()
        print("Transaction 6 FAILED:", e)

    finally:
        cur.close()
        conn.close()


# For debugging directly
if __name__ == "__main__":
    print("Run menu.py to execute transactions.")
from transactions import (
    transaction_1,
    transaction_2,
    transaction_3,
    transaction_4,
    transaction_5,
    transaction_6
)

