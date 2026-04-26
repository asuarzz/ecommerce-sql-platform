from database_manager import DatabaseManager

def reset_datbase():
    """
    Cleans all data from the tables in the correct order
    due to Foreign Key constaints
    """

    with DatabaseManager() as db:
        print("Starting database reset...")

        #The order is mandatory
        #First, delete those tables that depends of others (Child tables) to not ciolate the Foreign Keys
        queries = [
            "Delete from OrderItems",
            "Delete from Orders",
            "Delete from Users"
        ] 
        for query in queries:
            try:
                db.execute_query(query)
                print(f"Executed: {query}")
            except Exception as e:
                print("Error in {query}: {e}")

print("\n Database is clean and ready for fresh data!")

if __name__ == "__main__":
    #We ask for a simple confirmation to do not delete by error.
    confirm = input("This will delete ALL DATA (Users, Orders, Items). Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        reset_datbase()
    else:
        print("Reset cancelled.")