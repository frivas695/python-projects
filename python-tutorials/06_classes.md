# 6. Classes and objects

Classes describe data and behavior together.

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

    def summary(self) -> str:
        return f"{self.title} by {self.author} ({self.pages} pages)"

book = Book("The Left Hand of Darkness", "Ursula K. Le Guin", 304)
print(book.summary())
```

`@dataclass` generates useful methods such as `__init__` and `__repr__`.
Methods receive the instance as `self`.

## Exercises

1. Create a `Rectangle` dataclass with `width`, `height`, and an `area` method.
2. Add a `completed` Boolean to a `Task` class and a method to mark it done.
3. Create three objects and store them in a list. Print their summaries.
