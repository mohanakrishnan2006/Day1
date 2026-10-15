import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    # 'w' mode creates the file automatically if it doesn't exist, 
    # so we don't need a try-except block here.
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark done")
    print("4. Delete task")
    print("5. Quit")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose (1-5): ")
        
        if choice == "1":
            task_title = input("Enter task name: ")
            # Each task is a dictionary tracking the name and status
            new_task = {"task": task_title, "done": False}
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"✅ '{task_title}' added successfully!")
            
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\n--- Your Tasks ---")
                for index, item in enumerate(tasks, start=1):
                    # Show [X] for completed tasks and [ ] for incomplete ones
                    status = "X" if item["done"] else " "
                    print(f"{index}. [{status}] {item['task']}")
                    
        elif choice == "3":
            if not tasks:
                print("No tasks available to mark as done.")
                continue
            
            # Show tasks first so the user knows which number to pick
            print("\nSelect a task number to mark as done:")
            for index, item in enumerate(tasks, start=1):
                status = "X" if item["done"] else " "
                print(f"{index}. [{status}] {item['task']}")
                
            try:
                task_num = int(input("Enter task number: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["done"] = True
                    save_tasks(tasks)
                    print(f"💪 Task marked as completed!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
                
        elif choice == "4":
            if not tasks:
                print("No tasks available to delete.")
                continue
                
            print("\nSelect a task number to delete:")
            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item['task']}")
                
            try:
                task_num = int(input("Enter task number: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted: '{removed['task']}'")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
                
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("❌ Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
