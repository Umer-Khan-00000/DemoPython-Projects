tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")
