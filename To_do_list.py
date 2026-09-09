"""
DecodeLabs Industrial Training Kit — Python Programming
Project 1: The To-Do List
Batch 2026

Goal
----
Build a program where users can add tasks to a list and view them,
using core Python data-management skills: lists, append(), loops,
and enumerate(). The program follows the IPO model taught in the
training deck:

    INPUT  -> Data Entry      (add_task)
    PROCESS -> Logic/Modify   (delete_task, mark_done)
    OUTPUT -> Display/View    (view_tasks)

As a bonus, task data is persisted to a JSON file (tasks.json) so
the list survives even after the program (and RAM) is closed —
addressing the "Volatile Trap" slide: RAM is volatile, Process
Terminated = Data Lost.
"""

import json
import os

DATA_FILE = "tasks.json"


# ============================================================
# MODEL LAYER — Data Logic (Storage + Persistence)
# ============================================================

def load_tasks():
    """Load tasks from disk into memory. Returns an empty list if no
    save file exists yet (first run)."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Persist the current in-memory task list to disk as JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


# ============================================================
# PROCESS LAYER — Core Logic
# ============================================================

def add_task(tasks, description):
    """Add a new task dictionary to the list (like an INSERT INTO a table).

    Each task is stored as a dictionary — the same pattern used to
    model a database row: {"id": ..., "task": ..., "done": ...}
    """
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": new_id, "task": description, "done": False}
    tasks.append(task)          # O(1) amortized — dynamic array append
    save_tasks(tasks)
    print(f"\n✅ Task added: \"{description}\" (ID: {new_id})")


def mark_done(tasks, task_id):
    """Mark a task as completed by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"\n✅ Task {task_id} marked as done.")
            return
    print(f"\n  No task found with ID {task_id}.")


def delete_task(tasks, task_id):
    """Remove a task from the list by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"\n  Task {task_id} deleted.")
            return
    print(f"\n No task found with ID {task_id}.")


# =============================================================
# VIEW LAYER — Display / User Interface
# =============================================================

def view_tasks(tasks):
    """Display all tasks using enumerate() for clean index + value access."""
    print("\n" + "=" * 40)
    print("            YOUR TO-DO LIST")
    print("=" * 40)

    if not tasks:
        print("  (No tasks yet — add one to get started!)")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✔ Done" if task["done"] else "◻ Pending"
            print(f"  {index}. [{status}] {task['task']}  (ID: {task['id']})")

    print("=" * 40)


def show_menu():
    print("\n--- DecodeLabs To-Do List Manager ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


# =============================================================
# MAIN — Program Entry Point
# =============================================================

def main():
    tasks = load_tasks()   # Load persisted data at startup

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("Enter task description: ").strip()
            if description:
                add_task(tasks, description)
            else:
                print("\n  Task description cannot be empty.")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            try:
                task_id = int(input("Enter task ID to mark as done: "))
                mark_done(tasks, task_id)
            except ValueError:
                print("\n  Please enter a valid numeric ID.")

        elif choice == "4":
            view_tasks(tasks)
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            except ValueError:
                print("\n  Please enter a valid numeric ID.")

        elif choice == "5":
            print("\n Goodbye! Your tasks have been saved.")
            break

        else:
            print("\n Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()