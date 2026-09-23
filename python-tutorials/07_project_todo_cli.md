# 7. Project: a command-line todo app

Save this as `todo.py`, then run `python3 todo.py`. It combines functions,
lists, file handling, exceptions, and a simple command loop.

```python
from pathlib import Path

DATA_FILE = Path("todos.txt")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    return DATA_FILE.read_text(encoding="utf-8").splitlines()


def save_tasks(tasks):
    DATA_FILE.write_text("\n".join(tasks), encoding="utf-8")


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    tasks = load_tasks()
    print("Commands: list, add, done, quit")
    while True:
        command = input("> ").strip().lower()
        if command == "list":
            show_tasks(tasks)
        elif command == "add":
            task = input("Task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
        elif command == "done":
            try:
                index = int(input("Task number: ")) - 1
                tasks.pop(index)
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("Enter a valid task number.")
        elif command == "quit":
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
```

## Extensions

- Add a `clear` command.
- Store completed tasks instead of deleting them.
- Add due dates.
- Replace the text file with JSON using Python's `json` module.
