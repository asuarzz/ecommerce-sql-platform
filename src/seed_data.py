"""
Script to populate the database with fake data.
This is called 'Seeding' the databse
"""

from faker import Faker
from database_manager import DatabaseManager

#Initialize the Faker generator
#If we prefer we can use 'es_ES' for Spanish names 

fake = Faker()

def seed_users(db, count=10):
    """
    Generates and insert fakes users. 
    'count' defines hoy many users to create
    """
    print(f"--- Generating {count} fake uses ---")

    for i in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()

        #We use '?' as placeholder for security (Parameterized Query)
        query = "INSERT INTO Users (first_name, last_name, email) VALUES (?, ?, ?)"
        params = (first_name, last_name, email)

        try: 
            db.execute_query(query, params)
            print(f"[{i+1}Added: {first_name} {last_name}]")
        except Exception as e:
            print(f"Error adding user {i+1}: {e}")

def main():
    with DatabaseManager() as db:
        seed_users(db, count=10)
        print("\nSeeding completed successfully!")

if __name__ == "__main__":
    main()