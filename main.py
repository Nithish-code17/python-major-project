import os
from tools.task_manager import (
    add_task,
    view_tasks,
    mark_done,
    filter_tasks_by_status,
    sort_tasks_by_priority
)
from tools.file_renamer import rename_pdf_files


def main():
    while True:
        print("\n========== PYTHON MAJOR PROJECT ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Filter Tasks (Pending/Done)")
        print("5. Sort Tasks by Priority")
        print("6. Rename PDF Files in a Folder")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter priority (High/Medium/Low): ")
            add_task(title, priority)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to mark done: "))
            mark_done(task_id)

        elif choice == "4":
            status = input("Enter status (Pending/Done): ")
            filter_tasks_by_status(status)

        elif choice == "5":
            sort_tasks_by_priority()

        elif choice == "6":
            folder = input("Enter folder path to rename PDFs: ")
            rename_pdf_files(folder)

        elif choice == "7":
            print("✅ Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
