import tkinter as tk
from tkinter import messagebox

def calculate_marriage_goals():
    try:
        current_savings = float(current_savings_entry.get())
        monthly_savings = float(monthly_savings_entry.get())
        total_expense = float(total_expense_entry.get())
        
        months_until_marriage = float(months_until_marriage_entry.get())
        total_savings_at_marriage = current_savings + (monthly_savings * months_until_marriage)
        
        if total_savings_at_marriage >= total_expense:
            surplus = total_savings_at_marriage - total_expense
            result_label.config(text=f'Goal Achieved! Surplus: ${surplus:.2f}')
        else:
            deficit = total_expense - total_savings_at_marriage
            result_label.config(text=f'Goal Not Achieved. Deficit: ${deficit:.2f}')

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

window = tk.Tk()
window.title("Marriage Goal Calculator")

current_savings_label = tk.Label(window, text="Current Savings:")
current_savings_label.pack()
current_savings_entry = tk.Entry(window)
current_savings_entry.pack()

monthly_savings_label = tk.Label(window, text="Monthly Savings:")
monthly_savings_label.pack()
monthly_savings_entry = tk.Entry(window)
monthly_savings_entry.pack()

total_expense_label = tk.Label(window, text="Total Marriage Expense:")
total_expense_label.pack()
total_expense_entry = tk.Entry(window)
total_expense_entry.pack()

months_until_marriage_label = tk.Label(window, text="Months Until Marriage:")
months_until_marriage_label.pack()
months_until_marriage_entry = tk.Entry(window)
months_until_marriage_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_marriage_goals)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
