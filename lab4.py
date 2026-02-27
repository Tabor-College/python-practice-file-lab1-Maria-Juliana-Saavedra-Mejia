############################### LAB PRINCIPLES############################

############################### SEMANTICS ###############################

# Correct: sum then divide by count
def average(a, b, c):
    return (a + b + c) / 3  # ✅

print(average(4, 6, 8))
# Correct answer

x = 5          # Step 1: store 5 in x
y = 3          # Step 2: store 3 in y
z = x + y     # Step 3: read x(5) + read y(3) = 8, store in z
print(z)       # Step 4: display z → 8


#### QUESTION 1 SEMANTICS ############

def double(x):
    return x * 2

print(double(5)) # will give 10

#### QUESTION 2 SEMANTICS ############
def area(w, h):
    return w * h # Rectangle area formula = width × height.

#### QUESTION 3 SEMANTICS ############
a = 10         # variable a stores 10
b = a - 3      # 10 - 3 = 7 → b stores 7
print(b)       # prints 7

#### QUESTION 4 SEMANTICS ############

# False, a semantic error means the program 
# runs, but gives the wrong result. 



############################## GRAMMAR ##################################

# Grammar rule: how to write an if statement
# <if_stmt> ::= "if" <condition> ":" <body>

# Valid — follows the rule
if x > 5:
    print("big")

# NOT valid — missing colon (breaks the grammar rule)
# if x > 5
#    print("big")   # SyntaxError!


#### QUESTION 1 GRAMMAR ############

# a) x = 5
# Correct — no grammar error.
# b) if x > 3 print(x)
# SyntaxError — missing colon : after the condition.
# Correct version:
if x > 3:
    print(x)
#c) def f(): return 1
# Valid syntax. Python allows one-line function definitions.
# Answer: b is the grammar (SyntaxError).

#### QUESTION 2 GRAMMAR ############

# Valid Function 
def greet():
    print("Hello")

# Remove the colon: 

# def greet()
#    print("Hello")
# Python gives a SyntaxError.
# Because the colon : tells Python that an indented block 
# will follow. Without it, Python’s grammar rules are broken.

#### QUESTION 3 GRAMMAR ############

# A Python while loop must have:
# The keyword while
# A condition (something that evaluates to True or False)
# A colon :
# An indented block of code underneath

# If any of those parts are missing → SyntaxError.

#### QUESTION 4 GRAMMAR ############

# Python:
# Uses indentation to define code blocks.
# Makes structure visually clear.
# Prevents messy formatting.

# C++:
# Uses { } curly braces to define blocks.
# Indentation is optional (just for readability).

# Why Python requires indentation:
# It forces clean, readable structure.
# Eliminates inconsistent formatting.
# Which is easier to read?
# Most people find Python easier to read because the
# structure is visually obvious without extra symbols.



############################### RECURSION #############################

def countdown(n):
    if n == 0:               # BASE CASE — stop here
        print("Done!")
        return
    print(n)                  # print current number
    countdown(n - 1)          # RECURSIVE CASE — smaller input

countdown(3)

def factorial(n):
    if n == 0:       # base case
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
print(factorial(3))  # 6


#### QUESTION 1 RECURSION ############

# Typical count down function 

def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

# Trace it:
# countdown(5) → prints 5
# countdown(4) → prints 4
# countdown(3) → prints 3
# countdown(2) → prints 2
# countdown(1) → prints 1
# countdown(0) → prints "Done!"

#### QUESTION 2 RECURSION ############

# Typical factorial:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# factorial(0) → returns 1 (base case)
# factorial(1) → returns 1 × factorial(0) → 1 × 1 = 1
# Both return 1

#### QUESTION 3 RECURSION ############

def say_hello(n):
    if n == 0:          
        return
    print("Hello!")
    say_hello(n - 1)

say_hello(3)

# Hello!
# Hello!
# Hello!

#### QUESTION 4 RECURSION ############

# The base case is: 
# if n == 0:

# It matters because:
# It stops the recursion.
# It prevents infinite calls.
# If we remove it:
# The function would keep calling itself forever.
# Eventually Python would crash with a RecursionError
#  (maximum recursion depth exceeded).

########################## HIGHER - ORDER FNS ######################

# A simple function
def say_hello(name):
    return "Hello, " + name

# A higher-order function — it takes a function as input
def greet_person(name, greet_func):
    return greet_func(name)   # call whatever function was passed in

# Pass say_hello as the function
result = greet_person("Alice", say_hello)
print(result)   # Hello, Alice

numbers = [1, 2, 3, 4]

# double: a simple function
def double(x):
    return x * 2

# map() applies double to EVERY item in the list
result = list(map(double, numbers))
print(result)   # [2, 4, 6, 8]

# Same thing with a lambda (a tiny one-line function)
result2 = list(map(lambda x: x * 2, numbers))
print(result2)  # [2, 4, 6, 8]


#### QUESTION 1 HIGHER - ORDER FNS  ############

def add_one(x):
    return x + 1

map(add_one, [10, 20, 30])

# Step-by-step:
# add_one(10) → 11
# add_one(20) → 21
# add_one(30) → 31
# Result (as a list): [11,21,31]

#### QUESTION 2 HIGHER - ORDER FNS  ############

def apply(func, value):
    return func(value)

def double(x):
    return x * 2

apply(double, 5)

# Result: 10 Because it runs: double(5)

#### QUESTION 3 HIGHER - ORDER FNS  ############

sorted(["banana", "apple", "kiwi"], key=len)

# key=len tells sorted() to sort using the length of each word.
# len is the built-in function that returns how many characters are in a string.
# So it sorts by word length:
# "kiwi" → 4
# "apple" → 5
# "banana" → 6

#### QUESTION 4 HIGHER - ORDER FNS  ############

# double → the function itself (a reference to the function).
# the recipe
# double(5) → calling the function, which runs it and returns 10. 
# actually cooking the recipe


############################## ADTs ################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

p = Person("Alice", 20)
print(p.name)  # Alice
print(p.age)   # 20

from enum import Enum

class TrafficLight(Enum):   # sum type: ONE of these options
    RED    = "red"
    YELLOW = "yellow"
    GREEN  = "green"

light = TrafficLight.RED
print(light)         # TrafficLight.RED

if light == TrafficLight.RED:
    print("Stop!")
elif light == TrafficLight.GREEN:
    print("Go!")

#### QUESTION 1 ADTs  ############

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog("Buddy", "Golden Retriever")

print(my_dog.name)
print(my_dog.breed)

#### QUESTION 2 ADTs  ############

# A month of the year is a sum type because it can 
# be one of several distinct options (January, February, etc.), 
# but only one at a time.

#### QUESTION 3 ADTs  ############

from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

print(Season.SUMMER)


#### QUESTION 4 ADTs  ############

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(3, 4)
point2 = Point(7, 2)

print(point1.x, point1.y)
print(point2.x, point2.y)

########################### Expression Trees #########################

#      +           ← addition happens LAST (root)
#     / \
#    5   *         ← multiplication happens FIRST
#       / \
#      3   2

# Calculate from bottom up:
#  Step 1: 3 * 2 = 6
#  Step 2: 5 + 6 = 11
# Answer: 11

import ast

# Parse the expression into a tree
code = "5 + 3 * 2"
tree = ast.parse(code)

# Print the tree structure
print(ast.dump(tree, indent=2))

# You will see: BinOp (binary operation)
#   left:  Constant(5)
#   op:    Add()
#   right: BinOp
#            left:  Constant(3)
#            op:    Mult()
#            right: Constant(2)


#### QUESTION 1 Expression Trees  ############

#    +
#   / \
#  2   4

# + is the root (operator)
# 2 and 4 are the leaf nodes (operands)


#### QUESTION 2 Expression Trees  ############

# Multiplication (2 * 3) happens first because it
#  has higher precedence than subtraction.

#         (-)
#       /   \
#     10     (*)
#           /   \
#          2     3

#### QUESTION 3 Expression Trees  ############

import ast
print(ast.dump(ast.parse("1+2"), indent=2))

# Module(
#  body=[
#    Expr(
#      value=BinOp(
#        left=Constant(value=1),
#        op=Add(),
#        right=Constant(value=2)))],
#  type_ignores=[])

# BinOp = Binary Operation
# Add() = the + operator
# Constant(value=1) and Constant(value=2) are the leaves

#### QUESTION 4 Expression Trees  ############

# Without brackets:
# 10 - 2 * 3

#        (-)
#       /   \
#     10     (*)
#          /   \
#         2     3

# Multiplication happens first → Result = 4

# With brackets:
# (10 - 2) * 3

#         (*)
#       /   \
#     (-)    3
#    /   \
#  10     2

# subtraction happens first:
# 10 - 2 = 8
# 8 * 3 = 24

# The structure of the tree changes, which changes 
# the order of evaluation:
# The root operator changes from - to *, 
# which changes the final result.

########################### Type Checking #########################

x = 5           # x is an integer
x = "hello"     # x is now a string — Python allows this!
x = 3.14        # x is now a float — also fine in Python

# Type error - caugth when this LINE runs: 
# print("Age: " + 25)

# Fix: convert the number to a strng first 
print("age: " + str(25)) # "Age: 25 "

x = 5
x = "hello"  # ✅ OK in Python

#### QUESTION 1 Type Checking  ############

print(type(42))      # int
print(type("hello")) # str
print(type(3.14))    # float
print(type(True))    # bool

#### QUESTION 2 Type Checking  ############

# Error: 
# print("My age is: " + 20)

# Fixed 
print("My age is: " + str(20)) # My age is: 20

#### QUESTION 3 Type Checking  ############

# because Python is dynamically typed — variables do not 
# have fixed types.

#C++ does not allow this because it is statically 
# typed — once a variable is declared as a type (like int), 
# it cannot change to another type (like string).

#### QUESTION 4 Type Checking  ############

print(isinstance(42, int))
print(isinstance("hi", int))

# 42 is an int = True
# "hi" is not an int = False

########################### Mutable State #########################

# MUTABLE — lists CAN be changed
fruits = ["apple", "banana"]
fruits.append("cherry")   # add an item
fruits[0] = "avocado"      # change an item
print(fruits)             # ['avocado', 'banana', 'cherry']

# IMMUTABLE — strings CANNOT be changed
name = "Alice"
# name[0] = "B"   ← this would cause an ERROR
name = "Bob"        # this is OK — we rebind the name
print(name)         # Bob  (but "Alice" still exists somewhere)

a = [1, 2, 3]
b = a           # b points to the SAME list as a

b.append(4)   # change b
print(a)        # [1, 2, 3, 4] ← a changed too! Surprise!

# Fix: make a copy so a and b are separate
a = [1, 2, 3]
b = a.copy()    # now b is its own separate list
b.append(4)
print(a)        # [1, 2, 3] ← a is unchanged now ✅

#### QUESTION 1 Mutable state  ############
nums = [10, 20, 30]
nums.append(40)
nums[0] = 99
print(nums)

#### QUESTION 2 Mutable state  ############

# TypeError: 'str' object does not support item assignment
# Strings are immutable in Python — you cannot change 
# individual characters after creation.

#### QUESTION 3 Mutable state  ############

x = [1,2]
y = x
y.append(3)
print(x)

# [1, 2, 3]
# y = x does not copy the list.
# Both x and y point to the same list in memory.
# So modifying y also changes x.

#### QUESTION 4 Mutable state  ############

# TypeError: 'tuple' object does not support item assignment
# Tuples cannot be changed after they are created.

########################### Scope & Closures #########################

greeting = "Hello"    # GLOBAL — visible everywhere

def say_hi():
    name = "Alice"    # LOCAL — only exists inside say_hi
    print(greeting)   # OK — can see global variable
    print(name)       # OK — can see local variable

say_hi()
# print(name)   ← ERROR! 'name' doesn't exist out here

def outer():
    count = 0          # lives in outer
    def inner():
        return count   # remembers count!
    return inner

f = outer()
print(f())  # 0 — f remembers count=0

#### QUESTION 1 Scope & Closures  ############

def test():
    num = 100
    print(num)

test()
# print(num)

# NameError: name 'num' is not defined
# x is a local variable, so it only exists inside the function.

#### QUESTION 2 Scope & Closures  ############

city = "London"

def show_city():
    print(city)

show_city()

# Yes — the function can see global variables as 
# long as it does not try to modify them.

#### QUESTION 3 Scope & Closures  ############

def make_greeter(word): 
    def greet(name):
         return word + " " + name; 

    return greet

hi = make_greeter("Hi")
print(hi("Bob"))

# Hi Bob

# The inner function greet remembers the variable 
# word from the outer function.
# This is called a closure.

#### QUESTION 4 Scope & Closures  ############

x = 10

def change():
    global x
    x = 99

change()
print(x)

# Yes — it changes the global x.
# Without global, Python would create a new
# local variable instead.

############################### Currying #############################

# Normal function — takes both at once
def add(a, b):
    return a + b

print(add(3, 4))   # 7

# Curried version — takes one at a time
def add_curried(a):
    def step2(b):
        return a + b
    return step2          # return the second step

print(add_curried(3)(4))  # 7 — same result, different style

# Pre-fill the first argument
add5 = add_curried(5)   # add5 is now a function that adds 5
print(add5(10))          # 15
print(add5(20))          # 25

#### QUESTION 1 Currying  ############

def multiply(a):
    def inner(b):
        return a * b
    return inner

double = multiply(2)
print(double(7))

#### QUESTION 2 Currying  ############

# add_curried(3) returns a function, not a number.

# You know this because a curried function:

# Takes one argument.
# Returns another function that waits for the next argument.

# It does not compute the final result until the second
# argument is given.

#### QUESTION 3 Currying  ############

from functools import partial

add = lambda a, b: a + b
add10 = partial(add, 10)

print(add10(5))

# partial(add, 10) fixes the first argument (a = 10).
# So add10(5) becomes 10 + 5.

#### QUESTION 4 Currying  ############

# add(3, 4) → normal function call with two arguments at once.
# add(3)(4) → curried style:
# First call returns a function
# Second call gives the final value

# add(3,4) = one step
# add(3)(4) = two steps
# Both can give the same result, but the structure is different.

############################### Callbacks #############################

# A function that does work, then calls a callback
def calculate(a, b, when_done):
    result = a + b
    when_done(result)     # call the callback with the result

# Define what to do when done
def print_result(value):
    print("The answer is:", value)

# Pass print_result as the callback
calculate(10, 5, print_result)  # The answer is: 15

names = ["Charlie", "Al", "Bob"]

# Sort normally (alphabetical)
print(sorted(names))          # ['Al', 'Bob', 'Charlie']

# Sort by LENGTH — pass len as callback
print(sorted(names, key=len)) # ['Al', 'Bob', 'Charlie']

# sorted calls len("Charlie"), len("Al"), len("Bob")
# and uses those numbers to decide the order

#### QUESTION 1 Callbacks  ############

def do_twice(action):
    action()
    action()

def say_hello():
    print("Hello!")

do_twice(say_hello)

# We pass the function say_hello (not say_hello()).
# do_twice calls it two times — this is a callback.

#### QUESTION 2 Callbacks  ############

words = ["cat", "zebra", "apple"]
sorted_words = sorted(words, key=lambda w: w[-1])
print(sorted_words)

# It sorts using the last character of each word:
# "zebra" → 'a'
# "apple" → 'e'
# "cat" → 't'
# Alphabetical order of last letters: a, e, t.

#### QUESTION 3 Callbacks  ############

def greet_all(names, formatter):
    for name in names:
        print(formatter(name))

def friendly(name):
    return "Hi " + name + "!"

def formal(name):
    return "Good evening, " + name + "."

names = ["Alice", "Bob"]

greet_all(names, friendly)
greet_all(names, formal)

# Hi Alice!
# Hi Bob!
# Good evening, Alice.
# Good evening, Bob.

# formatter is a callback — we can change the 
# behavior by passing a different function.

#### QUESTION 4 Callbacks  ############

# sorted(items, key=len)

# len is not being called — it is being passed as a function.
# There are no parentheses (len, not len()).
# If it were called, it would need an argument like len(item).
# sorted() will call len() internally for each item.

################################## CPS ################################

def add(a, b):
    return a + b   # returns result

result = add(3, 4)
print(result)       # 7

def add_cps(a, b, k):
    k(a + b)   # pass result to k

# k = "what to do with the result"
add_cps(3, 4, print)    # 7

def add_cps(a, b, k):
    k(a + b)         # pass result forward

def double_cps(x, k):
    k(x * 2)         # pass result forward

# Goal: add 3+4, then double the result
# Chain: add 3+4 → then double → then print
add_cps(3, 4, lambda sum:
    double_cps(sum, print)
)
# add 3+4 = 7 → double 7 = 14 → print(14)

#### QUESTION 1 CPS ############

def square_cps(x, k):
    k(x * x)

#### QUESTION 2 CPS ############

square_cps(5, print)

# x * x → 5 * 5 = 25
# Then k(25) → print(25)

#### QUESTION 3 CPS ############

add_cps(3, 4, print)

# The continuation is print.
# It receives the result of 3 + 4.
# It prints the result.
# So the continuation is what happens next with the result.

#### QUESTION 4 CPS ############

# A continuation is similar to a callback because:
# Both are functions passed as arguments.
# Both define what happens after a computation finishes.
# Instead of returning a value, the function hands the result to another function.

# Callback = “run this after”
# Continuation = “this is the rest of the program”

################################ Summary ##############################

# PRINCIPLES OF PROGRAMMING LANGUAGES
#│
#├── STRUCTURE OF CODE
#│   ├── Grammar ──────── rules for what code is allowed
#│   └── Expression Trees ─ how Python reads your math
#│
#├── MEANING OF CODE
#│   └── Semantics ─────── what your code actually DOES
#│
#├── DATA
#│   ├── Types & Type Checking ─ what kind of data
#│   ├── ADTs ──────────────── how data is combined (AND / OR)
#│   └── Mutable State ─────── data that can change
#│
#├── NAMES & VISIBILITY
#│   └── Scope & Closures ── where variables can be seen
#│
#└── FUNCTION PATTERNS
#    ├── Recursion ──────── function calls itself
#    ├── Higher-Order Fns ─ pass functions around
#    ├── Currying ────────── one argument at a time
#    ├── Callbacks ───────── pass a function for "later"
#    └── CPS ─────────────── pass result to "next step"

# 01 Semantics ─── meaning of code (does it do the right thing?)
x = 2 + 3                       # evaluates 2+3=5, binds x to 5

# 02 Grammar ──── rules for writing valid code
if x > 3:                         # colon is required by grammar
    print("yes")

# 03 Recursion ── function that calls itself
def fact(n): return 1 if n == 0 else n * fact(n-1)

# 04 Higher-Order Fns ─ pass/return functions
squares = list(map(lambda n: n**2, [1,2,3]))  # [1,4,9]

# 05 ADT ─────── group data (AND) or choose type (OR)
class Person: name = "Alice"; age = 20  # product type

# 06 Expression Tree ─ Python builds a tree to evaluate math
import ast; ast.parse("5+3*2")     # try ast.dump() to see it

# 07 Type Checking ─ right data for the right operation
print(type(42))                    # <class 'int'>

# 08 Mutable State ─ lists change, strings don't
lst = [1,2]; lst.append(3)         # list mutated in place

# 09 Scope ─────── local vs global visibility
y = 10  # global
def f(): z = 5   # z is local to f

# 10 Currying ─── one argument at a time
def add(a): return lambda b: a + b
add5 = add(5)                      # add5(3) = 8

# 11 Callbacks ── pass a function for "later"
sorted(["banana","kiwi"], key=len)  # len is the callback

# 12 CPS ──────── pass result to next step (k)
def add_cps(a,b,k): k(a+b)
add_cps(3,4,print)                  # prints 7

#### QUESTION 1 Summary ############

def add(a,b): 
    return a+b

print(add(3,4)) # prints 7

# This is testing semantics — you understand what
#  the function does and how function calls work. 
# The syntax is correct; the question checks meaning.

#### QUESTION 2 Summary ############

# One thing Python lets you do that C++ does not (from this course):
# Pass functions easily as values (first-class functions).
# Dynamically change variable types.
# Write code without declaring variable types.

# One thing C++ catches earlier than Python:
# Type errors (because C++ is statically typed).
# Many errors are caught at compile time before running.

#### QUESTION 3 Summary ############

# Topics that use the idea of “passing a function”:
# Higher-order functions
# map()
# filter()
# sorted(..., key=...)
# Callbacks
# Continuations (CPS)
# Lambda functions
# All of these involve treating functions as values.

#### QUESTION 4 Summary ############

lst = [3, 1, 4, 1, 5]

lst.sort()      # Sort
lst.reverse()   # Reverse
print(lst)      # Print

# Sorted list: [1, 1, 3, 4, 5]
# Reversed: [5, 4, 3, 1, 1]

# How many concepts did you use?
# Lists
# Methods (.sort(), .reverse())
# Mutation
# Function calls
# Printing/output
# Order of execution

#### QUESTION 5 Summary ############

# One thing I found most interesting from these
# topics was how functions can be passed as values. 
# At first, I thought functions were only things you call, 
# but learning about higher-order functions, callbacks, and 
# continuations showed me they can also be treated like data. 
# That completely changed how I see programming. It made code 
# feel more flexible and powerful. I also found it surprising 
# how small syntax differences can completely change the meaning 
# of a program.