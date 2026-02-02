# Online Supermarket Billing System 🛒

A menu-driven supermarket billing application built using Python and MySQL.  
The system allows users to select products within a given budget, manages inventory using a database, and generates a final bill at checkout.

---

## Features
- Menu-driven console interface
- Budget-based product selection
- Database-backed product management
- Real-time inventory updates
- Cart operations (add, remove, update quantity)
- Discount and GST calculation
- Automated final bill generation

---

## Tech Stack
- Python  
- MySQL  
- SQL  

---

## Project Structure
online-supermarket-billing-system/
│── main.py
│── README.md

---

## How It Works
1. User enters a budget
2. Products are fetched from MySQL database tables
3. User selects required items through menu options
4. System updates stock values dynamically
5. Final bill is generated with applicable discounts and GST

---

## How to Run
1. Install Python (3.x)
2. Set up a MySQL database
3. Create required tables for products
4. Update database credentials in the Python file
5. Run the application:
   ```bash
   python main.py
