# 3. Functions

Functions package behavior into reusable units.

```python
def greet(name, punctuation="!"):
    """Return a friendly greeting."""
    return f"Hello, {name}{punctuation}"

print(greet("Lin"))
print(greet("Sam", "."))
```

Parameters receive values. `return` sends a result back to the caller. A
default parameter is used when an argument is omitted.

## Type hints

Type hints document intended inputs and outputs:

```python
def discount(price: float, percent: float) -> float:
    return price * (1 - percent / 100)
```

Hints are not enforced automatically, but editors and type checkers can use
them.

## Scope

Variables created inside a function are local to it:

```python
tax_rate = 0.2

def total(price):
    tax = price * tax_rate
    return price + tax
```

Prefer passing values as parameters rather than changing global variables.

## Exercises

1. Write `is_even(number)` that returns a Boolean.
2. Write `word_count(text)` that returns the number of whitespace-separated
   words.
3. Write `average(numbers)` that returns the mean of a non-empty list.
