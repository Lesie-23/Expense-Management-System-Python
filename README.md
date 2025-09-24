# Expense Management System-Python

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server. It allows users to record, update, and analyze their expenses across various categories and time. 


## Project Structure:

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Project Interface:

<img width="675" height="599" alt="Image" src="https://github.com/user-attachments/assets/4ca3a2e1-7f10-4461-860f-38789447d382" />



<img width="668" height="796" alt="analytics_by_category" src="https://github.com/user-attachments/assets/4f992f98-db01-4935-ba28-dbe1e4388743" />



<img width="849" height="759" alt="analytics_by_month_wise" src="https://github.com/user-attachments/assets/f95e3514-be0a-457d-bcee-298eeec54e7e" />

#Features:

1. **Expense Management (CRUD Features)**
- Perform create, read, update, and delete operations on expense records.
- Save expense information—such as date, amount, category, and notes—directly in a MySQL database.

2. **Backend (FastAPI)**
- Built RESTful API endpoints for:
- Adding new expenses

- Retrieving expenses by specific dates
- Producing category-based summaries
- Providing month-by-month analytics
- Implemented logging to assist with debugging and monitoring API usage.

3. **Frontend (Streamlit)**
- Designed a user-friendly interface to handle expense management tasks.
- Integrated an interactive dashboard for visual expense analytics.

4. **Analytics**
- Category-based insights: Analyze spending patterns across different categories.
- Monthly insights: Monitor expenses over time using clear visual representations.



#TechStack Used:
1. Frontend: Streamlit
2. Backend: FastAPI
3. Database: MySQL (Connected using MySQL - Connector-Python)
4. HTTP Testing: Postman
5. Logging: Python's built-in logging module
6. Testing: Pytest 


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
