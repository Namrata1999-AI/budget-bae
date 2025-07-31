def calculate_savings(income, expenses):
    savings = income - expenses
    if savings < 0:
        return savings, "You're overspending! Time to cut back!"
    elif savings == 0:
        return savings, "You're breaking even. Try to save a bit!"
    else:
        return savings, "Great job! You're saving money!"