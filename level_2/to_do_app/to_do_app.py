import json
#Loading or creating the JSON file if it doesn't exist
try:
    with open("level_2/tasks.json", "r") as f:
        tasks = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = {}
    with open("level_2/tasks.json", "w") as f:
        json.dump(tasks, f)

#Main loop for the to-do list application
def menu_list():
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Tasks as Completed")
    print("5. Exit")
def task_list():
    print("Tasks:")
    for task, status in tasks.items():
        status_str = "Completed" if status else "Pending"
        print(f"    - {task} ({status_str})")
menu_list()
while True:
    print("---To-Do List Application---")
    print("Type 'r' to repeat the menu")
    choice = input("Enter choice: ")
    if choice == '5':
        print("Exiting To-Do List Application. Goodbye!")
        break
    elif choice == '1':
        if not tasks:
            print("No tasks available.")
        else:
            task_list()
    elif choice == '2':
        new_task = input("Enter the new task: ")
        if new_task in tasks:
            print("Task already exists.")
        else:
            tasks[new_task] = False
            with open("level_2/tasks.json", "w") as f:
                json.dump(tasks, f)
            print(f"Task '{new_task}' added.")
    elif choice == '3':
        task_list()
        del_task = input("Enter the task to remove('all' to remove all tasks): ")
        if del_task in tasks:
            del tasks[del_task]
            with open("level_2/tasks.json", "w") as f:
                json.dump(tasks, f)
            print(f"Task '{del_task}' removed.")
        elif del_task == "all":
            tasks.clear()
            with open("level_2/tasks.json", "w") as f:
                json.dump(tasks, f)
            print("All tasks removed.")
        else:
            print("Task not found.")
    elif choice == '4':
        task_list()
        comp_task = input("Enter the task to mark as completed: ")
        if comp_task in tasks:
            tasks[comp_task] = True
            with open("level_2/tasks.json", "w") as f:
                json.dump(tasks, f)
            print(f"Task '{comp_task}' marked as completed.")
        else:
            print("Task not found.")
    elif choice == 'r':
        menu_list()
    else:
        print("Invalid choice. Please try again.")
    