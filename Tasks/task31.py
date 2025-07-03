tasks = [] 

while True:
    print("\n--- To-Do List Task ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Delete Task")
    print("5. Exit")
    
    ch = int(input("Enter Choice: "))

    match ch:
        case 1:
            name = input("Enter Task Name: ")
            tasks.append({"task": name, "status": "Pending"})
            print("Task added successfully!")

        case 2:
            if not tasks:
                print("No tasks to show.")
            else:
                print("\nAll Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task['task']} - {task['status']}")

        case 3:
            if not tasks:
                print("No tasks to mark.")
            else:
                    task_no = int(input("Enter task number to mark as done: "))
                    tasks[task_no - 1]['status'] = "Done"
                    print("Task marked as done!")

        case 4:
            if not tasks:
                print("No tasks to delete.")
            else:
                    task_no = int(input("Enter task number to delete: "))
                    deleted = tasks.pop(task_no - 1)
                    print(f"Task '{deleted['task']}' deleted.")
                

        case 5:
            print("Exit")
            break

        case _:
            print("Invalid Choice.")
