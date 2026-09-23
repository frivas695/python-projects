# 4. Collections

## Lists

Lists are ordered and mutable:

```python
tasks = ["learn", "practice"]
tasks.append("build")
print(tasks[0])
print(tasks[-1])
print(tasks[1:])
```

## Dictionaries

Dictionaries map keys to values:

```python
user = {"name": "Ada", "language": "Python"}
user["level"] = "beginner"
print(user.get("timezone", "unknown"))

for key, value in user.items():
    print(f"{key}: {value}")
```

## Tuples and sets

Tuples are useful for fixed groups of values. Sets contain unique values:

```python
point = (3, 4)
tags = {"python", "learning", "python"}
print(point, tags)
```

## Exercises

1. Count the frequency of each word in a sentence using a dictionary.
2. Remove duplicates from a list while preserving its order.
3. Given two sets of skills, print their intersection and union.
