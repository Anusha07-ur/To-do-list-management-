from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n📌 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(title, description, due_date)
            print("✅ Task added successfully!")
        
        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                print(f"[{task.task_id}] {task.title} - {task.status} (Due: {task.due_date})")

        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
            print("🗑️ Task deleted!")

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            status = input("Enter new status (Pending/Completed): ")
            manager.update_task_status(task_id, status)
            print("🔄 Task updated!")

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
