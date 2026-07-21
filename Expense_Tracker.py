total = 0.0 # accumulator — initialized OUTSIDE the loop so it isn't reset each time
count = 0 # keeps track of how many valid expenses were entered
print("===== EXPENSE TRACKER =====")
print("Enter an expense amount, or type 'done' to see your total.\n")
while True:
    user_input = input("Enter expense amount: ").strip()
    if user_input.lower() == "done":
        break
    try:
        expense = float(user_input)
        if expense < 0:
            print("Expense cannot be negative. Try again.")
            continue
        total += expense # the accumulator pattern: State(new) = State(old) + Input
        count += 1
        print(f"Added {expense:.2f}. Running total: {total:.2f}")
    except ValueError:
        print("Invalid input — please enter a number (e.g., 100, 50.5).")
print("\n===== SUMMARY =====")
print(f"Number of expenses entered: {count}")
print(f"Total Spent: {total:.2f}")