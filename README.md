# Ecommerce SQL Platform

## 🛠️ Tech Stack & Environment
- **Operating System:** macOS (Apple Silicon M1)
- **Language:** Python 3.x
- **Database:** Microsoft SQL Server (running via Docker/Azure SQL Edge)
- **Libraries:** `pyodbc`, `python-dotenv`
- **Architecture:** Decoupled Data Access Layer (DatabaseManager) with SQL Views.

## 🚀 Key Features (Updated May 2026)
- **Transactional Simulation:** A dedicated engine (`generate_sales.py`) that creates realistic orders and links them to users and products.
- **Relational Integrity Checks:** Custom scripts to identify orphaned records and ensure database health.
- **Business Intelligence Layer:** SQL Views built to aggregate sales data and customer performance in real-time.

## 📂 Project Structure
- `database/scripts/`: SQL definitions for tables and views.
- `src/`: 
    - `database_manager.py`: Core connection handler.
    - `generate_sales.py`: Logic for creating complex relational data.
    - `data_integrity_check.py`: Quality assurance tool.
    - `check_performance.py`: BI reporting tool.