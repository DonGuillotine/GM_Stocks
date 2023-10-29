import tkinter as tk
from tkinter import messagebox
import numpy_financial as npf


def calculate_future_medical_expenses(current_expenses, inflation_rate, years):
    return current_expenses * (1 + inflation_rate) ** years

def calculate_savings_and_investment(salary, current_expenses, inflation_rate, rate_of_return, years):
    future_expenses = calculate_future_medical_expenses(current_expenses, inflation_rate, years)
    total_savings_needed = future_expenses * years
    monthly_savings = total_savings_needed / (years * 12)
    monthly_investment = (monthly_savings * (1 + rate_of_return / 12) ** (years * 12)) - monthly_savings
    return monthly_savings, monthly_investment


def on_calculate():
    try:
        salary = float(salary_entry.get())
        current_expenses = float(current_expenses_entry.get())
        inflation_rate = float(inflation_rate_entry.get()) / 100
        rate_of_return = float(rate_of_return_entry.get()) / 100
        years = int(years_entry.get())
        monthly_savings, monthly_investment = calculate_savings_and_investment(
            salary, current_expenses, inflation_rate, rate_of_return, years
        )
        result_label.config(text=f"Monthly Savings: ${monthly_savings:.2f}, Monthly Investment: ${monthly_investment:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

window = tk.Tk()
window.title("Medical Insurance Goal Calculator")

salary_label = tk.Label(window, text="Monthly Salary:")
salary_label.pack()
salary_entry = tk.Entry(window)
salary_entry.pack()

current_expenses_label = tk.Label(window, text="Current Monthly Medical Expenses:")
current_expenses_label.pack()
current_expenses_entry = tk.Entry(window)
current_expenses_entry.pack()

inflation_rate_label = tk.Label(window, text="Annual Inflation Rate (%):")
inflation_rate_label.pack()
inflation_rate_entry = tk.Entry(window)
inflation_rate_entry.pack()

rate_of_return_label = tk.Label(window, text="Annual Rate of Return on Investment (%):")
rate_of_return_label.pack()
rate_of_return_entry = tk.Entry(window)
rate_of_return_entry.pack()

years_label = tk.Label(window, text="Years Until Retirement:")
years_label.pack()
years_entry = tk.Entry(window)
years_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=on_calculate)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
