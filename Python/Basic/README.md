# Python Fundamentals

This overview provides a complete introduction to Python's core principles, enriched with examples and explanations to support solid learning. Whether you’re a beginner or brushing up, this guide covers Python basics and advanced elements essential for versatile coding.

---

### Table of Contents
1. **Variables and Data Types**
2. **Operators**
3. **Basic Regex**
4. **Conditionals**
5. **Loops**
6. **Generators and Iterators**
7. **Functions**
8. **Error Handling**
9. **Collections: Lists, Tuples, Sets, and Dictionaries**
10. **Comprehensions**
11. **File I/O and Context Managers**
12. **Async Programming**
13. **Classes and Object-Oriented Programming (OOP)**
14. **Decorators and Context Managers**
15. **Modules and Packages**
16. **My Questions**
17. **Common Questions about This Article**
18. **Main Reference Links**

---

## 1. Variables and Data Types

### Variables
Variables are named storage for data values. Python is dynamically typed, meaning variable types don’t need to be declared explicitly.

```python
name = "Alice"         # str  
age = 25               # int  
height = 5.7           # float  
is_student = True      # bool  
```

### Data Types
Python has several built-in data types:
- **int**: Whole numbers (e.g., 42).
- **float**: Decimal numbers (e.g., 3.14).
- **str**: Text (e.g., "Hello").
- **bool**: Boolean values (e.g., True or False).
- **None**: Represents the absence of a value (e.g., None).

### Type Conversion
Python supports type conversion between compatible data types.

```python
age_str = str(age)            # Convert int to str  
height_int = int(height)      # Convert float to int (truncates decimals)  
```

---

## 2. Operators

Python has various operators to manipulate data:
- **Arithmetic**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponentiation)
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`

**Example**:
```python
x = 10  
y = 3  
result = x ** y  # Exponentiation, result is 1000  
```

---

## 3. Basic Regex

Regular expressions (regex) allow for complex string pattern matching and manipulation, useful for tasks like validation, search, and replace. Python's `re` module provides built-in regex support.

```python
import re

# Check if a string contains a phone number pattern
pattern = r'\d{3}-\d{3}-\d{4}'
text = "Call me at 123-456-7890"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())
```

---

## 4. Conditionals

Conditionals allow you to control the flow of the code.

```python
if age > 18:  
    print("Adult")  
elif age == 18:  
    print("Just turned adult")  
else:  
    print("Minor")  
```

### Ternary Conditional
Python also supports single-line conditional expressions.

```python
status = "Adult" if age >= 18 else "Minor"  
```

---

## 5. Loops

### `for` Loop
Used for iterating over a sequence (like lists or strings).

```python
names = ["Alice", "Bob", "Charlie"]  
for name in names:  
    print(name)  
```

### `while` Loop
Repeats as long as a condition is `True`.

```python
count = 0  
while count < 5:  
    print(count)  
    count += 1  
```

### Loop Control Statements
- **break**: Exits the loop.
- **continue**: Skips the current iteration.

---

## 6. Generators and Iterators

Generators and iterators enable efficient, on-demand computation of sequences without loading all elements into memory at once. They're particularly useful for working with large datasets or implementing lazy evaluation in loops.

- **Iterators**: Objects that allow traversing a container (like lists or dictionaries) using the `iter()` and `next()` methods.
- **Generators**: Functions that yield items one at a time using the `yield` keyword. They maintain their state, allowing you to resume from the point you left off.

**Example**:
```python
# Basic iterator example
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))   # Output: 1
print(next(iterator))   # Output: 2

# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(3):
    print(number)
```

---

## 7. Functions

Functions are reusable blocks of code.

```python
def greet(name):  
    return f"Hello, {name}!"  

print(greet("Alice"))  
```

- **Parameters**: Values passed to functions.
- **Return**: The output of the function.

### Lambda Functions
Anonymous functions defined using the lambda keyword.

```python
square = lambda x: x ** 2  
print(square(5))  # output: 25  
```

---

## 8. Error Handling

Python uses `try-except` for error handling.

```python
try:  
    result = 10 / 0  
except ZeroDivisionError:  
    print("Cannot divide by zero!")  
finally:  
    print("Execution completed.")  
```

### Custom Exceptions
You can define custom exceptions by creating a new class.

```python
class CustomError(Exception):  
    pass  

raise CustomError("Something went wrong!")  
```

---

## 9. Collections: Lists, Tuples, Sets, and Dictionaries

### Lists
Ordered and mutable collection.

```python
fruits = ["apple", "banana", "cherry"]  
fruits.append("orange")  
```

### Tuples
Ordered and immutable collection.

```python
coordinates = (10, 20)  
```

### Sets
Unordered collection of unique elements.

```python
unique_numbers = {1, 2, 3, 3}  
```

### Dictionaries
Key-value pairs.

```python
person = {"name": "Alice", "age": 25}  
print(person["name"])   # output: Alice
```

---

## 10. Comprehensions

Python comprehensions offer a concise syntax for creating lists, sets, dictionaries, and even generators in a single line. This feature makes code both efficient and expressive, similar to set builder notation in mathematics, where you define a set by specifying a rule for its elements.



- **List Comprehension**: `[x * 2 for x in range(5)]`
- **Set Comprehension**: `{x ** 2 for x in range(5)}`
- **Dictionary Comprehension**: `{x: x ** 2 for x in range(5)}`

In mathematics, for instance, you might define a set like {x^2 | x ∈ ℤ, x < 5}, meaning "the set of squares of all integers less than 5." Python comprehensions enable a similar approach for generating values concisely.

**Example**:
```python
# List comprehension for squares of even numbers
numbers = [1, 2, 3, 4, 5]
squared_even = [x ** 2 for x in numbers if x % 2 == 0]  # Output: [4, 16]

# This example is equivalent to the following code but more compact:
squared_even = []
for x in numbers:
    if x % 2 == 0:
        squared_even.append(x ** 2)
```

Python comprehensions allow for **conditions** to selectively include elements and apply transformations to each item, producing a new list (or other data structure) in a single line, which is often easier to read and understand.

---

## 11. File I/O and Context Managers

The `with` statement is used to manage resources efficiently, ensuring files are properly closed after use.

### Reading and Writing Files

```python
# Writing to a file  
with open("example.txt", "w") as file:  
    file.write("Hello, World!")  

# Reading from a file  
with open("example.txt", "r") as file:  
    content = file.read()  
```

### Context Managers (`with` Statement)
The `with` statement is used to manage resources efficiently, ensuring files are properly closed after use.

---

## 12. Async Programming

Asynchronous programming allows you to run tasks concurrently, making it ideal for I/O-bound tasks such as web requests and file I/O. It's powered by `async` and `await` keywords, using Python's `asyncio` library to handle tasks in a non-blocking manner.

```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)      # Simulate network delay
    return "Data received!"

async def main():
    result = await fetch_data()
    print(result)

# Run the asynchronous function
asyncio.run(main())
```

---

## 13. Classes and Object-Oriented Programming (OOP)

Classes are blueprints for creating objects (instances).

```python
class Dog:  
    def __init__(self, name):  
        self.name = name  

    def bark(self):  
        return f"{self.name} says Woof!"  

dog = Dog("Buddy")  
print(dog.bark())  
```

### OOP Concepts
- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class.
- **Attributes**: Variables that belong to a class.
- **Methods**: Functions that belong to a class.
- **Inheritance**: Creating a new class from an existing class.

---

## 14. Decorators and Context Managers

### Decorators
A way to modify functions or methods dynamically. Decorators are often used in Django for adding functionality like authentication or logging.

```python
def my_decorator(func):  
    def wrapper():  
        print("Something is happening before the function is called.")  
        func()  
        print("Something is happening after the function is called.")  
    return wrapper  

@my_decorator  
def say_hello():  
    print("Hello!")  

say_hello()  
```

### Context Managers
Context managers help manage resources, like files or database connections, with the `with` statement.

```python
with open("example.txt", "r") as file:  
    content = file.read()  
```

---

## 15. Modules and Packages

### Importing Modules
Modules allow you to organize code into separate files.

```python
import math  
print(math.sqrt(16))  
```

### Custom Modules
You can create your own module by saving Python functions in a file and importing it.

```python
# In a file named my_module.py  
def greet(name):  
    return f"Hello, {name}!"  

# In another file  
from my_module import greet  
print(greet("Alice"))  
```

### Packages
Packages are collections of modules. By organizing related modules into packages, Python projects can be structured more effectively.

---

## 16. My Questions

### Q1: Regular Expression: `pattern = r'\d{3}-\d{3}-\d{4}'`

This regular expression is used to **match strings in a phone number format**. Here's a breakdown of the components:

- `\d`: Represents any digit (0-9).
- `{3}`: Specifies that the preceding pattern (a digit in this case) should repeat exactly 3 times.
- `-`: Matches the hyphen character `-`.

So the pattern `r'\d{3}-\d{3}-\d{4}'` will match strings like `123-456-7890`, a typical 10-digit phone number format.

### Q2: Understanding `iterator = iter(my_list)` and `next(iterator)`

- The `iter(my_list)` function creates an **iterator object** from `my_list`, allowing you to access its elements one by one.
- Calling `next(iterator)` retrieves the next item in the iterator's sequence.

In the example below:
```python
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # Output: 1, the first element
print(next(iterator))  # Output: 2, the second element
```

When `next()` is called, it returns the next element in the list. This approach is especially useful for large data collections or for implementing custom sequences.

### Q3: Lambda Functions and the `**` Operator

#### Lambda Functions:

- A `lambda` function is an **anonymous (nameless)** function created in a single line.
- It’s often used when a short function is needed for a limited purpose without the need for a full function definition.

```python
# Traditional function
def square(x):
    return x ** 2

# Equivalent lambda function
square_lambda = lambda x: x ** 2
print(square_lambda(5))  # Output: 25
```

Lambda functions are compact, often making code shorter and simpler for straightforward operations like filtering or mapping.

#### `**` Operator for Exponentiation

- The `**` operator is used for exponentiation in Python. 

```python
result = 5 ** 3  # Output: 125, as 5 * 5 * 5 = 125
```

It is often used in mathematical and scientific calculations, offering a convenient way to handle powers and roots.

### Q4: `pass` and `raise` in Custom Exception Classes

#### `pass`

- The `pass` statement **does nothing** and is often used to create a minimal structure for a class or function without any content.
- For instance, in a custom exception class where no additional functionality is needed, `pass` can be used.

```python
class CustomException(Exception):
    pass
```

#### `raise`

- The `raise` keyword **triggers an exception** and is used to raise an error explicitly when a specific condition is met.
- For example, `raise CustomException("Error!")` will trigger the `CustomException` with the message `"Error!"`.

```python
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("y cannot be zero")
    return x / y
```

### Q5: Comprehensions as Mathematical Set Builder Notation

In Python, **comprehensions** allow the concise creation of lists, dictionaries, sets, etc., and can be thought of as similar to set builder notation in mathematics.

- **List comprehension** example:
```python
numbers = [1,2,3,4,5]

# Includes only squares of even numbers
squared_numbers = [x ** 2 for x in numbers if x % 2 == 0]
```
- Just like in set builder notation, comprehensions **allow for conditions** to include only specific elements and apply transformations to each element, producing a new list (or other data structure).

### Q6: `from` and `import`

#### `import` Statement

The `import` statement is used to include external modules or libraries in your code, making their functions, classes, and variables available to use. For example:

```python
import math
print(math.sqrt(16))    # Output: 4.0
```

In this case, the entire `math` module is imported, and you access its functions using `math.` as a prefix.

#### `from ... import` Statement

The `from ... import` syntax allows you to import specific functions, classes, or variables directly, so you don't need to prefix them with the module name. For example:

```python
from math import sqrt
print(sqrt(16)) # Output: 4.0
```

Here, only `sqrt` is imported from the `math` module, and you can use it directly without the `math.` prefix.

---

## 17. Common Questions about This Article

### Q1: How can I practice these Python concepts?

The best way to practice is by building small projects or exercises that use multiple concepts together. Start with simpler projects, like a basic calculator (variables, operators, and conditionals) or a student management system (classes, file handling, collections, etc.). Many online platforms also offer interactive exercises; refer to the Main Reference Links section for resources like Codecademy, Exercism, and HackerRank.

### Q2: Which concepts are most important for a beginner to focus on?

For beginners, focus on variables and data types, conditionals, loops, and functions. These form the foundation for most coding tasks. Once comfortable with these, proceed to error handling and collections. Advanced topics like OOP, async programming, and decorators can be approached once you’re comfortable with the basics.

### Q3: How do I use regular expressions effectively?
Regular expressions (regex) can seem complex at first, but they are powerful tools for string manipulation. Start by learning simple patterns, like matching digits (`\d`), letters (`\w`), and whitespace (`\s`). Experiment using the `re` module in Python, and practice with small tasks, like validating phone numbers or email addresses. Tools like RegexOne or Pythex allow you to test patterns interactively.

### Q4: What is the difference between synchronous and asynchronous programming?

In **synchronous programming**, tasks run one after another, which can lead to delays if a task takes a long time (e.g., reading from a file or making a network request). **Asynchronous programming** allows certain tasks to run concurrently, enabling a program to handle other work while waiting for slower tasks to complete. Python’s asyncio library is often used for this and is particularly useful in web development and applications with many I/O operations.

### Q5: When should I use comprehensions instead of regular loops?

Comprehensions (e.g., list comprehensions) provide a concise way to create lists, sets, and dictionaries and can make code easier to read when used for simple transformations. For example, `[x * 2 for x in range(10)]` is often clearer than a `for` loop for creating lists based on existing values. However, for more complex logic or side effects, a regular loop is usually more readable and should be preferred.

### Q6: Where can I get help if I’m stuck?

If you encounter issues or have questions, official documentation and community resources like **Stack Overflow** are invaluable. Real Python also offers tutorials with community support for questions. For more in-depth help, consider joining a Python community on platforms like Reddit’s r/learnpython or Python-specific Discord servers.

### Q7: What are some recommended projects to build after learning these concepts?

Great beginner-to-intermediate projects include:

- **To-Do List**: Practice lists, conditionals, and functions.
- **Student Management System**: Apply OOP, file handling, and error handling.
- **Weather App**: Use API requests with async programming for fetching data.
- **Basic Calculator**: Practice operators, functions, and error handling.
These projects can help reinforce your understanding and challenge you to combine concepts.

---

## 18. Main Reference Links

1. **Python Official Documentation**: [Python Docs](https://docs.python.org/3/)
2. **Real Python**: [Real Python](https://realpython.com/)
3. **Python Cheatsheet**: [Python Cheatsheet](https://www.pythoncheatsheet.org/)