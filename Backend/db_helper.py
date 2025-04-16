#CRUD Create Retrieve Update Delete
import mysql.connector
from contextlib import contextmanager
from datetime import datetime, timedelta
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1631993neelM@d",
        database = "expense_manager"
    )

    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Failed Connection")
    cursor = connection.cursor(dictionary = True)

    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    start = datetime.combine(expense_date, datetime.min.time())
    end = start + timedelta(days=1)
    logger.info(f"fetch_expense_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT amount, category, notes FROM expenses WHERE expense_date >= %s AND expense_date < %s",
            (start, end)
        )
        expenses = cursor.fetchall()
        return [
            {"amount": row["amount"], "category": row["category"], "notes": row["notes"]}
            for row in expenses
        ]


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with expense:{expense_date}, amount {amount}, category{category}, notes{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s,%s,%s,%s)", (expense_date, amount, category, notes))

def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense_for_date called with {expense_date}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date, ))
def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start{start_date}, end{end_date} date")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total
               FROM expenses WHERE expense_date
               BETWEEN %s and %s
               GROUP BY category;''', (start_date, end_date)
        )
        data = cursor.fetchall()
        return data
if __name__ == "__main__":
    summary = fetch_expense_summary("2024-08-01","2024-08-05")
    for record in summary:
        print (record)