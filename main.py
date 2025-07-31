def get_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nSession ended.")
        exit()

def suggest_budget(income, fixed_expenses, savings_goal):
    discretionary = income - fixed_expenses - savings_goal
    if discretionary < 0:
        return "Your expenses and savings exceed your income. Consider reducing fixed costs or lowering your savings goal."
    else:
        return (
            f"Here's a quick budget plan:\n"
            f"- Fixed Expenses: ₹{fixed_expenses}\n"
            f"- Savings Goal: ₹{savings_goal}\n"
            f"- Discretionary Spending: ₹{discretionary}\n"
        )

def main():
    print("🧠 Welcome to Budget Bae!")
    name = get_input("What's your name? ")

    income = float(get_input("Enter your monthly income (in ₹): "))
    fixed_expenses = float(get_input("Enter your fixed monthly expenses (in ₹): "))
    savings_goal = float(get_input("Enter your monthly savings goal (in ₹): "))

    print("\nThanks, " + name + "! Let's calculate your budget...\n")
    plan = suggest_budget(income, fixed_expenses, savings_goal)
    print(plan)

if __name__ == "__main__":
    main()