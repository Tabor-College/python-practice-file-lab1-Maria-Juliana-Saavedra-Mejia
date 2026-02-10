tasks = []
boolean = True

print("Welcome to the Student Task Tracker")

# Part A — Initial task input
initial = input("How many tasks do you want to enter initially?: ").strip()

if initial.isdigit():
    initial = int(initial)
    for i in range(initial):
        task = input(f"Enter task {i + 1}: ").strip()
        if task != "":
            tasks.append(task)

    if tasks:
        print("Initial task list:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
else:
    print("No initial tasks added")

# Main Menu Loop

while boolean:
    print("""
        1. Add a new task
        2. Insert a task at a position
        3. Remove a task by name
        4. Remove a task by index
        5. Update a task
        6. View all tasks
        7. Sort tasks
        8. Reverse tasks
        9. Search for a task
        10. Task statistics
        11. Copy task list
        12. Clear all tasks
        13. Exit    
    """)

    choice = input("Type the number of your choice: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number")
        continue

    selection = int(choice)

    # Option 1 — Add task

    if selection == 1:
        newTask = input("Write the new task: ").strip()

        if newTask == "":
            print("There is nothing in the new task")
        else:
            tasks.append(newTask)
            print("New task added successfully")

    # Option 2 — Insert task

    elif selection == 2:
        if not tasks:
            print("No tasks to insert into")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            newTaskInsert = input("Write the new task: ").strip()

            if newTaskInsert == "":
                print("There is nothing in the new task")
            else:
                pos = input("Type the position of the task: ").strip()

                if pos.isdigit():
                    pos = int(pos) - 1
                    if 0 <= pos <= len(tasks):
                        tasks.insert(pos, newTaskInsert)
                        print("New task added successfully")
                    else:
                        print("Invalid position")
                else:
                    print("Invalid position")

    # Option 3 — Remove by name

    elif selection == 3:
        if not tasks:
            print("No tasks to remove")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            remove = input("Write the task you want to delete: ").strip()

            if remove == "":
                print("You forgot to write something")
            elif remove in tasks:
                tasks.remove(remove)
                print("Task removed correctly")
            else:
                print("Task not found")

    # Option 4 — Remove by index 

    elif selection == 4:
        if not tasks:
            print("No tasks to remove")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            taskDelete = input("Write the number of the assignment you want to remove: ").strip()

            if taskDelete == "":
                print("You forgot to write something")
            elif not taskDelete.isdigit():
                print("Please enter a valid number")
            else:
                number = int(taskDelete) - 1

                if number < 0 or number >= len(tasks):
                    print("That task number does not exist")
                else:
                    removed_task = tasks.pop(number)
                    print(f"Task '{removed_task}' deleted correctly")

    # Option 5 — Update task

    elif selection == 5:
        if not tasks:
            print("No tasks to update")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            taskUpdate = input("Write the number of the assignment you want to update: ").strip()

            if taskUpdate == "":
                print("You forgot to write something")
            elif not taskUpdate.isdigit():
                print("Please enter a valid number")
            else:
                update = int(taskUpdate) - 1

                if update < 0 or update >= len(tasks):
                    print("That task number does not exist")
                else:
                    updatesNotes = input("Write the new task description: ").strip()

                    if updatesNotes == "":
                        print("Task cannot be empty")
                    else:
                        tasks[update] = updatesNotes
                        print("Task updated correctly")

    # Option 6 — View tasks

    elif selection == 6:
        if not tasks:
            print("No tasks to display")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Option 7 — Sort tasks

    elif selection == 7:
        if not tasks:
            print("No tasks to display")
        else:
            tasks.sort()
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Option 8 — Reverse tasks

    elif selection == 8:
        if not tasks:
            print("No tasks to display")
        else:
            tasks.reverse()
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Option 9 — Search

    elif selection == 9:
        if not tasks:
            print("No tasks to search")
        else:
            searchTask = input("Write the task you want to search for: ").strip()

            if searchTask in tasks:
                print("Task found")
                print("Occurrences:", tasks.count(searchTask))
                print("First position:", tasks.index(searchTask) + 1)
            else:
                print("Task not found")

    # Option 10 — Statistics

    elif selection == 10:
        if not tasks:
            print("No tasks available")
        else:
            print("Total number of tasks:", len(tasks))
            print("First task:", tasks[0])
            print("Last task:", tasks[-1])

    # Option 11 — Copy list

    elif selection == 11:
        if not tasks:
            print("No tasks to copy")
        else:
            tasksCopy = tasks.copy()

            print("Original task list:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            print("\nCopied task list:")
            for i in range(len(tasksCopy)):
                print(i + 1, ".", tasksCopy[i])

    # Option 12 — Clear list

    elif selection == 12:
        if not tasks:
            print("Task list is already empty")
        else:
            tasks.clear()
            print("All tasks have been cleared")

    # Option 13 — Exit

    elif selection == 13:
        print("Thank you for visiting the Student Task Tracker")
        boolean = False

    else:
        print("Wrong choice, try again")


# Reflection (Comments Only)

# 1. remove() deletes an element by value,
#  while pop() deletes an element by index.

# 2. copy() is safer than assignment because it 
# creates a new list instead of referencing the same one.

# 3. sort() permanently changes the order of the list
#  alphabetically.

# 4. List indexing starts at 0, meaning the first element
#  is at index 0.
