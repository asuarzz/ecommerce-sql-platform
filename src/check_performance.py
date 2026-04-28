from database_manager import DatabaseManager

def show_sales_report():
    """
    Fetches and displays the performance report from the database view.
    """
    with DatabaseManager() as db:
        print("\n--- SALES PERFORMANCE REPORT ---")
        query = "SELECT customer_name, total_orders, total_spent FROM v_SalesPerformance ORDER BY total_spent DESC"
        results = db.fetch_data(query)

        if not results:
            print("No sales available")
            return
        
        print(f"{'Customer Name':<25} | {'Orders':<8} | {'Total_Spent':<12}")
        print("-" * 50)

        for row in results:
            name, orders, spent = row
            #If spent is none(user hasn't bought anything), we show 0
            spent_val = spent if spent else 0
            print(f"{name:<25} | {orders:<8} | ${spent_val:12.2f}")

if __name__ == "__main__":
    show_sales_report()
