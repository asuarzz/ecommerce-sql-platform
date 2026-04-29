from database_manager import DatabaseManager

def check_integrity():
    """
    Performs basic integrity check to ensure the database is consistent
    """
    with DatabaseManager() as db:
        print("\n---DATABASE INTEGRITY CHECK---")

        #Check 1: Orphaned Orders (Orders without a valid user)
        orphan_orders = db.fetch_data("""SELECT COUNT(*) FROM Orders
                                      WHERE user_id NOT IN (SELECT user_id FROM Users)""")
        
        #Check 2: Empty orders (Orders without any item)
        empty_orders = db.fetch_data("""SELECT COUNT(*) FROM Orders
                                     WHERE order_id NOT EXISTS (SELECT DISTINCT order_id FROM order_items)""")
        
        print(f"Total Orphaned Orders: {orphan_orders[0][0]}")
        print(f"Total Empty Orders: {empty_orders[0][0]}")

        if orphan_orders[0][0] == 0 and empty_orders[0][0] == 0:
            print("\n Integrity Check Passed: All relations are healthy.")
        else:
            print("\n Integrity Warning: Inconsistent data found.")

if __name__ == "__main__":
    check_integrity()
 