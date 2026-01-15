# 🐍 Python Programming: The Complete Masterclass

**Professor:** *Takes a deep breath and looks at the whiteboard filled with diagrams.*
"You asked for the full roadmap, the 'Grand Tour' of our semester. It is ambitious, but I like your spirit! This file now contains the **entire syllabus** condensed into bite-sized lessons. Think of this as your field guide. We will explore each of these territories in detail, but here is everything you need to know, from your first 'Hello' to building web servers."

---

## 🟢 Module 1: The Foundations (Beginner)

### 1.1 Variables & Types
Labels for your data.
```python
name = "Alice"       # String (str)
age = 20             # Integer (int)
height = 5.9         # Float (float)
is_student = True    # Boolean (bool)
```

### 1.2 Control Flow (Making Decisions)
Teaching the computer logic.
```python
if age >= 18:
    print("Adult")
elif age > 12:
    print("Teenager")
else:
    print("Child")

# Loops
for i in range(5):
    print(f"Counting: {i}")  # Prints 0 to 4
```

---

## 🟡 Module 2: Structuring Data (Data Structures)

### 2.1 Lists (Ordered, Mutable)
A backpack of items.
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits[0])  # apple
```

### 2.2 Tuples (Ordered, Immutable)
A sealed box. You can't change it once created.
```python
coords = (10, 20)
# coords[0] = 5  <-- This would cause an Error!
```

### 2.3 Dictionaries (Key-Value Pairs)
Like a real dictionary or a contact list.
```python
user = {
    "name": "Eve",
    "role": "Admin"
}
print(user["name"])  # Eve
```

### 2.4 Sets (Unordered, Unique)
A bag of unique items. No duplicates allowed.
```python
unique_nums = {1, 2, 2, 3} 
print(unique_nums) # {1, 2, 3}
```

---

## 🟠 Module 3: Reusable Code (Functions)

Don't repeat yourself. Wrap logic in a function.

```python
def greet(name, loud=False):
    msg = f"Hello, {name}!"
    if loud:
        return msg.upper()
    return msg

print(greet("Bob", loud=True)) # HELLO, BOB!
```

---

## 🔵 Module 4: Intermediate Mastery

### 4.1 Comprehensions
Shortcuts for creating lists.
```python
# Old way
squares = []
for x in range(5):
    squares.append(x**2)

# Pythonic way
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
```

### 4.2 String Magic
```python
text = "  python is cool  "
clean = text.strip().upper() # "PYTHON IS COOL"
words = clean.split()        # ["PYTHON", "IS", "COOL"]
```

---

## 🟣 Module 5: Organizing & Reliability

### 5.1 Modules & Packages
Split your code into multiple files.
```python
# In my_module.py
def special_func():
    pass

# In main.py
import my_module
my_module.special_func()
```

### 5.2 Error Handling (Try/Except)
Don't let the program crash!
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This runs no matter what.")
```

### 5.3 File I/O
Reading and writing files.
```python
with open("notes.txt", "w") as f:
    f.write("Remember to buy milk.")

# The 'with' block automatically closes the file for you.
```

---

## 🟤 Module 6: Object-Oriented Programming (OOP)

### 6.1 Classes & Objects
Blueprints for creating things.
```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable

    def bark(self):
        return "Woof!"

my_dog = Dog("Rex")
print(my_dog.bark())
```

### 6.2 Inheritance
Creating new versions of existing things.
```python
class Poodle(Dog):
    def bark(self):
        return "Yip!"  # Overriding behavior
```

---

## ⚫ Module 7: Advanced Python

### 7.1 Decorators
Modifying functions without changing their code.
```python
def log_it(func):
    def wrapper():
        print("Running function...")
        func()
    return wrapper

@log_it
def say_hi():
    print("Hi!")

# say_hi() will now print "Running function..." first.
```

### 7.2 Generators & Yield
Lazy loading data (saves memory).
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5) # Returns a generator object, not a list
```

---

## ⚪ Module 8: Professional Practices

### 8.1 Backend (Web)
Using libraries like Flask or Django to make websites.
```python
# Pseudo-code for a simple web server
# @app.route("/")
# def home():
#     return "Welcome to my website!"
```

### 8.2 Testing
Proving your code works.
```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
```

### 8.3 Concurrency
Doing multiple things at once (Threading vs Asyncio).
```python
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# asyncio.run(main())
```

---

## 🎓 Professor's Closing Thoughts

"We have traversed the entire map! From simple variables to asynchronous web servers.

**Your Homework:**
Pick **ONE** module from above (I recommend starting with Module 1 or 2). Write a small script that uses those concepts. Save it, run it, and show me the results!

Which module should we deep-dive into first?"

---

## 📚 Official Documentation & Resources
*   [Official Python Documentation](https://docs.python.org/3/) - The bible of Python.
*   [Python Package Index (PyPI)](https://pypi.org/) - The repository for third-party modules.
*   [PEP 8 Style Guide](https://peps.python.org/pep-0008/) - How to write clean Python code.
