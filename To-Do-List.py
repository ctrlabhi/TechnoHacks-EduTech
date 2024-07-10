class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task "{self.tasks[task_number - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    def main(self):
        while True:
            print("\nTo-Do List")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_number = int(input("Enter the task number to mark as completed: "))
                self.mark_task_completed(task_number)
            elif choice == '4':
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
            elif choice == '5':
                print("Exiting the To-Do List application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.main()
