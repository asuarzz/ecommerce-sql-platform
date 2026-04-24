"""
Main orchestator for the E-commerce Data Pipeline.
Uses DatabaseManager for interacto with the database.
"""

from database_manager import DatabaseManager

def main():

    # We use 'with' to handle the connection automatically
    with DatabaseManager() as db:
        print("\n---REPORT FROM SQL VIEW---")
        report = db.fetch_data("SELECT * FROM v_OrderSummaries")

        for row in report:
            print(f"Customer:{row[1]} bought:{row[2]} for $:{row[5]}")
  

if __name__ == "__main__":
    main()
