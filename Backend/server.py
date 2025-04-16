from http.client import HTTPException

from fastapi import FastAPI
from datetime import date
import db_helper
from pydantic import BaseModel
from typing import List
import requests



class Expense(BaseModel):
    amount : float
    category : str
    notes : str

class DateRange(BaseModel):
    start_date: date
    end_date: date


app = FastAPI(debug = True)
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    raw_expenses = db_helper.fetch_expenses_for_date(expense_date) or []
    expenses = [Expense(**expense) for expense in raw_expenses]
    return expenses
@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses:List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expense Update Successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)

    total = sum([row['total'] for row in data])
    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total":row['total'],
            "percentage":percentage
        }
    return breakdown

