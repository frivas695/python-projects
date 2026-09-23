# 1. Python basics

## Your first program

```python
print("Hello, Python!")
```

`print` displays a value. Text is a **string**, written inside quotes.

## Variables and types

```python
name = "Ada"       # str
age = 36           # int
temperature = 21.5 # float
is_learning = True # bool

print(name, age)
print(type(temperature))
```

Python determines the type from the value. Use `str`, `int`, and `float` to
convert between common types:

```python
year = int("2026")
message = "Age: " + str(age)
```

## Strings and f-strings

```python
first = "Grace"
last = "Hopper"
print(f"{first} {last}")
print(f"{first.lower()} wrote code.")
```

F-strings let you insert expressions inside `{}`.

## Arithmetic

```python
total = 7 + 3
remainder = 17 % 5
power = 2 ** 4
average = (8 + 10) / 2
```

## Exercises

1. Store your name and favorite number, then print both in one f-string.
2. Convert `"42"` to an integer and print twice its value.
3. Given `minutes = 135`, calculate the hours and remaining minutes.
