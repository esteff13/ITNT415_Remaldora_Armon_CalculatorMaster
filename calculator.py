# ==========================================================
#  Calculator Master - S-ITNT415 Midterm Summative
#  Author : Armon Jhon M. Remaldora
#  Repo   : ITNT415_Remaldora_Armon_CalculatorMaster
#  A menu-driven calculator built one Git branch at a time.
# ==========================================================

APP_NAME = "Calculator Master by Remaldora"


# ---------- Operation: addition (branch addition_Remaldora) ----------
def add(a, b):
    """Return the sum of a and b."""
    return a + b


# ---------- Operation: subtraction (branch subtraction_Remaldora) ----------
def subtract(a, b):
    """Subtraction - to be implemented on branch subtraction_Remaldora."""
    raise NotImplementedError


# ---------- Operation: multiplication (branch multiplication_Remaldora) ----------
def multiply(a, b):
    """Multiplication - to be implemented on branch multiplication_Remaldora."""
    raise NotImplementedError


# ---------- Operation: division (branch division_Remaldora) ----------
def divide(a, b):
    """Division - to be implemented on branch division_Remaldora."""
    raise NotImplementedError


# ---------- Helpers (main branch) ----------
def get_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("  [!] Invalid input '{}'. Please enter a number.".format(raw))


def fmt(value):
    """Show whole numbers without a trailing .0"""
    return str(int(value)) if float(value).is_integer() else str(value)


OPERATIONS = {
    "1": ("Addition", "+", add),
    "2": ("Subtraction", "-", subtract),
    "3": ("Multiplication", "*", multiply),
    "4": ("Division", "/", divide),
}


def show_menu():
    print("\n==========================================")
    print("   " + APP_NAME)
    print("==========================================")
    for key, (name, symbol, _) in OPERATIONS.items():
        print("  [{}] {:<15} ({})".format(key, name, symbol))
    print("  [5] Exit")
    print("------------------------------------------")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye! - Remaldora's Calculator Master")
            break
        if choice not in OPERATIONS:
            print("  [!] Invalid choice '{}'. Pick a number from 1 to 5.".format(choice))
            continue
        name, symbol, func = OPERATIONS[choice]
        a = get_number("Enter first number : ")
        b = get_number("Enter second number: ")
        try:
            result = func(a, b)
            print("  Result: {} {} {} = {}".format(fmt(a), symbol, fmt(b), fmt(result)))
        except NotImplementedError:
            print("  [!] {} is not available yet (still being built on its branch).".format(name))
        except ZeroDivisionError as err:
            print("  [!] Error: {}".format(err))


if __name__ == "__main__":
    main()
