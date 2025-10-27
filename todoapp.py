def display_menu():
    print("Welcome to the ToDo App!")
    print("Please choose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f'Task "{task}" added.')
        elif choice == '2':
            if tasks:
                print("Your Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks available.")
        elif choice == '3':
            if tasks:
                print("Select the task number to delete:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f'Task "{removed_task}" deleted.')
                else:
                    print("Invalid task number.")
            else:
                print("No tasks available to delete.")
        elif choice == '4':
            print("Exiting the ToDo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
