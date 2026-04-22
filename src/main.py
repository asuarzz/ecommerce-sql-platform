"""
Main orchestator for the E-commerce Data Pipeline.
Uses DatabaseManager for interacto with the database.
"""

from database_manager import DatabaseManager

def main():
    #Create Manager and connect
    db = DatabaseManager()
    db.connect()

    #Read all users
    print("\n--- ALL USERS ---")
    users = db.fetch_data("SELECT * FROM Users")
    for user in users:
        print(user)

    #Read all products
    print("\n--- ALL PRODUCTS ---")
    products = db.fetch_data("SELECT * FROM Products")
    for product in products:
        print(product)

    #Read all orders
    print("\n--- ALL ORDERS ---")
    orders = db.fetch_data("SELECT * FROM Orders")
    for order in orders:
        print(order)

    #Close connection
    db.close()

if __name__ == "__main__":
    main()
