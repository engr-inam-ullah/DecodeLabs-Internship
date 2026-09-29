#=========================================
#           Expense Tracker
#=========================================
"""
A command-line tool that accepts expense amounts one at a time,
accumulates them into a running total, and reports a final summary
when the user is done.

Core concepts demonstrated:
    * The Accumulator Pattern      (total = total + new_expense)
    * Defensive Coding             (try/except around user input)
    * Sentinel-Controlled Loops    (type 'quit' to stop safely)
    * Separation of Logic & Output (compute first, display separately)

Developer: <INAM ULLAH>
"""

from dataclasses import dataclass

SENTINEL = "quit"


@dataclass
class ExpenseSummary:
    
    total: float
    transaction_count: int


def prompt_for_expense(transaction_number: int) -> str:
    return input(f"Expense #{transaction_number}: ").strip()


def parse_expense(raw_value: str) -> float:
   
    amount = float(raw_value)  # may raise ValueError for non-numeric text
    if amount < 0:
        raise ValueError("Expense amount cannot be negative.")
    return amount


def track_expenses() -> ExpenseSummary:
  
    total = 0.0
    transaction_count = 0

    print("=" * 45)
    print("   DECODELABS EXPENSE TRACKER")
    print("=" * 45)
    print("Enter an expense amount ")
    print(f"Type '{SENTINEL}' \n")

    while True:
        raw_value = prompt_for_expense(transaction_count + 1)

      
        if raw_value.lower() == SENTINEL:
            break

        # --- Defensive coding: validate before trusting the data ---
        try:
            expense = parse_expense(raw_value)
        except ValueError:
            print("  \u26a0  Invalid entry. Enter a positive number "
                  f"or '{SENTINEL}' to stop.\n")
            continue

        # --- Accumulator pattern: State(new) = State(old) + Input ---
        total += expense
        transaction_count += 1
        print(f"  \u2714 Added ${expense:,.2f}  |  "
              f"Running total: ${total:,.2f}\n")

    return ExpenseSummary(total=total, transaction_count=transaction_count)


def display_summary(summary: ExpenseSummary) -> None:
    """Render the final report. Kept separate from the calculation logic."""
    print("=" * 45)
    print(f"  Transactions recorded : {summary.transaction_count}")
    print(f"  FINAL TOTAL SPENT     : ${summary.total:,.2f}")
    print("=" * 45)


def main() -> None:
    summary = track_expenses()
    display_summary(summary)


if __name__ == "__main__":
    main()