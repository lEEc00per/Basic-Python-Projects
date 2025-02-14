#Bank Management System

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not todo_list:
        print("No tasks available.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def remove_task(task_index):
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Removed task: '{removed_task}'")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            if todo_list:
                view_tasks()
                try:
                    task_index = int(input("Enter task number to remove: ")) - 1
                    remove_task(task_index)
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks available to remove.")
        elif choice == '4':
            print("Visit Again!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()