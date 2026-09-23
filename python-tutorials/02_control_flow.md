# 2. Control flow

## Conditions

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "Keep practicing"

print(grade)
```

Indentation defines blocks. Comparisons include `==`, `!=`, `<`, `>`, `<=`,
and `>=`. Combine conditions with `and`, `or`, and `not`.

## Loops

```python
for number in range(1, 4):
    print(number)

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
```

Use `break` to stop a loop and `continue` to skip to its next iteration.

## Comprehensions

```python
squares = [number ** 2 for number in range(6)]
even_squares = [value for value in squares if value % 2 == 0]
print(even_squares)
```

## Exercises

1. Print the numbers from 1 to 20, labeling each as even or odd.
2. Keep asking for a password until the user enters `"python"`.
3. Create a list of cubes for numbers 1 through 10 using a comprehension.
