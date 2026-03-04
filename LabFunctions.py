def greet_user():
    """Ask the user for their name and greet them."""
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to the course.")

greet_user()

def calculate_total(price, quantity):
    total = price * quantity
    return total

item_price = 19.99
item_quantity = 3
bill_total = calculate_total(item_price,item_quantity)

print("Total bill: ", bill_total)

def checkout(amount,shipping=5.0):
    final_amount = amount + shipping
    return final_amount

print("order 1: ", checkout(50))
print("order 2: ", checkout(50, shipping=10))

def register_student(name,program,year):
    print("------- Student Registration -------")
    print(f"Name : {name}")
    print(f"Program : {program}")
    print(f"Year : {year}")
    print("-----------------------------------")

register_student("Anu", "Computer Science", 1)
register_student(year=2, name="Rahul", program="Data Science")

def average_score(*scores):
    """Calculate average of any number of scores."""
    if not scores:
        print("No scores provided.")
        return None
    
    total = sum(scores)
    avg = total/len(scores)
    print(f"Scores: {scores}")
    print(f"Average: {avg}")
    return avg

average_score(80,90,75)
average_score(100,95)
average_score()

def create_profile(**info):
    """Create a user profile with any number of attributes."""
    if not info:
        print("Empty profile.")
        return None 
    
    print("------- User Profile -------")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    print("----------------------------")

create_profile(name="K", role="Professor", department="CS")
create_profile(name="Sam", city="Sacramento")
create_profile()

def log_event(event_type, *details, **metadata):
    """Log an event with details and metadata. """
    print("=== Event Log ===")
    print(f"Type:{event_type}")

    if details:
        print(f"Details:{details}")
    else:
        print("Details: (none)")

    if metadata:
        print("Metadata: ")
        for key, value in metadata.items():
            print(f" {key} = {value}")
    else:
        print("Metadata: (none)")
    print("=================")

log_event("LOGIN", "Success", user="K", ip="192.168.0.10")
log_event("FILE_UPLOAD", "report.pdf", size="2MB")
log_event("PING")

def analyze_sales(sales):
    """Analyze sales data and return min, max, total, and average."""
    if not sales:
        return None, None, 0, 0
    
    min_sale = min(sales)
    max_sale = max(sales)
    total = sum(sales)
    average = total / len(sales)
    return min_sale, max_sale, total, average

week_sales = [120, 150, 90, 200, 175]
min_s, max_s, total_s, avg_s = analyze_sales(week_sales)

print(f"Min sale : ${min_s}")
print(f"Max sale : ${max_s}")
print(f"Total sale: ${total_s}")
print(f"Average : ${avg_s:.2f}")

balance = 1000 
def deposit_correct(amount):
    global balance 
    balance = balance + amount
    print(f"Deposited ${amount}, new balance = ${balance}")

def deposit_wrong(amount):
    balance = balance + amount 
    return balance

print("Initial balance:", balance)
deposit_correct(200)
print("After deposit:", balance)

def ten_percent_discount(amount):
    return amount * 0.9

def flat_five_discount(amount):
    return amount - 5

def apply_discount(amount, discount_func):
    """Apply a discount function to an amount."""
    new_amount = discount_func(amount)
    print(f"Original: ${amount}, After discount: ${new_amount}")
    return new_amount

apply_discount(100, ten_percent_discount)
apply_discount(100, flat_five_discount)

square = lambda x: x ** 2
print(square(5)) 

products = [
    ("Notebook", 4.99),
    ("Pen", 1.49),
    ("Backpack", 29.99),
    ("Bottle", 9.99),
]

sorted_by_price = sorted(products, key=lambda item: item[1])
print("Products sorted by price:")
for name, price in sorted_by_price:
    print(f" {name}: ${price}")


def celsius_to_fahrenheit(c):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    Args:
    c (float): Temperature in Celsius
    Returns:
    float: Temperature in Fahrenheit
"""
    return (c * 9 / 5) + 32

result = celsius_to_fahrenheit(37)
print(f"37°C in Fahrenheit = {result}°F")

print("\nDocstring:")
print(celsius_to_fahrenheit.__doc__)

my_tuple = (1, 2, 3, 4, 5)

single = (5,)

mixed = (1, "hello", 3.14, True)


fruits = ("apple", "banana", "cherry")

print(fruits[0])
print(fruits[-1])
print(fruits[0:2])


person = ("Alice", 25, "NYC")
name, age, city = person


my_set = {1, 2, 3, 4, 5}

my_set = {1, 2, 2, 3}
print(my_set)

empty = set()
wrong = {}


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)


my_set = {1, 2, 3}

my_set.add(4)
my_set.update([5, 6])
my_set.remove(2)
my_set.discard(10)


squares = [x**2 for x in range(1, 6)]
print(squares)


numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)


words = ["hello", "world"]
upper = [w.upper() for w in words]
print(upper)


numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)


numbers = [1, 2, 2, 3, 3, 3]
unique = {x**2 for x in numbers}
print(unique)


squares = {x: x**2 for x in range(1, 4)}
print(squares)


try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    x = 0


try:
    x = int(input("Number: "))
    y = int(input("Divisor: "))
    result = x / y
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print(f"You entered: {x}")


file = None
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()


def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")
