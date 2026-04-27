import random
from database_manager import DatabaseManager

def create_random_numbers(db, num_orders=5):
    """
    Simulates e-commerce by creating random orders for existing users
    """
    #1. Fetch existing Users and Products IDs data
    users = db.fetch_data("SELECT user_id FROM Users")
    products = db.fetch_data("SELECT product_id, price FROM Product")

    if not users or not products:
        print("Error: No users or product found to generate sales.")
        return
    
    #Extracting only the IDs from the database response
    user_ids = [u[0] for u in users]
    print(f"Generating {num_orders} random orders...")

    for i in range(num_orders):
        #Pick a random user
        user_id = random.choice(user_ids)

        #Insert the Main Order (The Header)
        order_query = "INSERT INTO Orders (user_id, order_date, status)" \
                      "VALUES(?, GETDATE(), 'Completed')"
        db.execute_query(order_query, user_id)

        #Retrieve the ID from the order we just created
        #@@IDENTITY is a SQL command to get the las generated ID
        order_id_result = db.fetch_data("SELECT @@IDENTITY")
        order_id = order_id_result[0][0]

        #Add 1 to 3 random Products to this specific order(The details)
        num_items = random.randint(1, 3)
        for _ in range(num_items):
            #Pick a random product (id, price)
            product = random.choice(products)
            product_id, price = product[0], product[1]
            quantity = random.randint(1, 5)

            item_query = """
                        INSERT INTO OrderItems(order_id, product_id, quantiry, unit_price)
                        VALUES(?, ?, ?, ?)
                        """
            db.execute_query(item_query, (order_id, product_id, quantity, price))
        
    print(f"Successful: {num_orders} orders successfully simulated")

if __name__ == "__main__":
    with DatabaseManager() as db:
        create_random_numbers(db, num_orders=10)