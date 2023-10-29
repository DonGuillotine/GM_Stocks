import tkinter as tk
from tkinter import messagebox

def calculate_vacation_goals():
    try:
        current_savings = float(current_savings_entry.get())
        monthly_savings = float(monthly_savings_entry.get())
        annual_expense = float(annual_expense_entry.get())
        years = float(years_entry.get())
        
        total_savings = current_savings + (monthly_savings * 12 * years)
        total_expenses = annual_expense * years
        
        if total_savings >= total_expenses:
            surplus = total_savings - total_expenses
            result_label.config(text=f'Goal Achieved! Surplus: ${surplus:.2f}')
        else:
            deficit = total_expenses - total_savings
            result_label.config(text=f'Goal Not Achieved. Deficit: ${deficit:.2f}')

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

window = tk.Tk()
window.title("Vacation Goal Calculator")

current_savings_label = tk.Label(window, text="Current Savings:")
current_savings_label.pack()
current_savings_entry = tk.Entry(window)
current_savings_entry.pack()

monthly_savings_label = tk.Label(window, text="Monthly Savings:")
monthly_savings_label.pack()
monthly_savings_entry = tk.Entry(window)
monthly_savings_entry.pack()

annual_expense_label = tk.Label(window, text="Annual Vacation Expense:")
annual_expense_label.pack()
annual_expense_entry = tk.Entry(window)
annual_expense_entry.pack()

years_label = tk.Label(window, text="Years Until Vacation:")
years_label.pack()
years_entry = tk.Entry(window)
years_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_vacation_goals)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
