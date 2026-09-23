# 5. Files and errors

## Reading and writing files

Use `with` so Python closes the file automatically:

```python
from pathlib import Path

path = Path("notes.txt")
path.write_text("First note\nSecond note\n", encoding="utf-8")

for line in path.read_text(encoding="utf-8").splitlines():
    print(line)
```

`Path` works consistently across operating systems.

## Handling exceptions

```python
def read_number():
    try:
        return int(input("Enter a whole number: "))
    except ValueError:
        print("That was not a whole number.")
        return None
```

Catch only errors you know how to handle. Put cleanup in `finally` when it must
always happen.

## Exercises

1. Read a text file and print its line count.
2. Write a function that safely divides two numbers and handles division by
   zero.
3. Save a list of names to a file, one name per line, then read it back.
