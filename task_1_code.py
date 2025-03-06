# Build a terminal-based To-Do List Manager where 
# users can add, remove, and mark tasks as completed. 
# The program should store tasks using basic data types 
# (str, list, dict) and allow interaction through a simple menu.

# Mandatory Requirements
# 1. Add Tasks + 
# 2. View Tasks +
# 3. Mark Tasks as Completed +
# 4. Remove Tasks +
# 5. Keep Running Until User Exits +
# 6. Basic Input Validation +
# 7. Github +

# Extra Features
# 1. Save & Load Tasks +
# 2. Task Categories +
# 3. Task Due Dates + 
# 4. Tasks Priorities +
# 5. Search for Tasks by name +

import json
from enum import Enum
from datetime import datetime
from typing import List, Optional


class Task:
    def __init__(self, description: str = "", category: str = "", deadline: str = "%Y-%m-%d", priority: Enum = None, status: bool = False):
        self.description = description
        self.category = category
        self.deadline = deadline
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Description: {self.description[:30]}, Category: {self.category[:20]}, Deadline: {self.deadline}, Priority: {self.priority.name.lower()}, Status: {'[✔]' if self.status else '[ ]'}"



class Priority(Enum):
    NONE = 3
    LOW = 2
    MEDIUM = 1
    HIGH = 0

    def __str__(self):
        return self.name.lower()



class TaskManager:
    def __init__(self):
        self.all_tasks: List[Task] = []    # better to change to global value?


    def add_task(self) -> bool:
        description = self.set_description()  # mandatory to enter
        if description:
            category = self.set_category()
            deadline = self.set_deadline()
            priority = self.set_priority()
            status = False

            new_task = Task(description, category, deadline, priority, status)
            self.all_tasks.append(new_task)
            self.all_tasks.sort(key=lambda x: x.deadline)
        else:
            return False


    def set_description(self) -> str:
        while True:
            description = input("Enter task decription (max 30 characters) (or Q to quit): ").capitalize()
            if description == "Q":
                break
            if len(description) > 30:
                print("Description cannot exceed 30 characters!")
                continue
            if description.strip() == "":
                print("Description field cannot be empty!")
                continue
            else:
                return description


    def set_category(self) -> str:
        category = input("Enter task category (or press ENTER to skip): ")
        if category == "":
            return "none"
        else:
            return category


    def set_deadline(self) -> str:
        while True:
            due_date = input("Enter deadline (YYYY-MM-DD) (or press ENTER to skip): ")
            if due_date == "":
                return "none" 
            try:
                deadline = datetime.strptime(due_date, "%Y-%m-%d")
                return deadline.strftime("%Y-%m-%d")  
            except ValueError:
                print("Invalid date format!")


    def set_priority(self) -> Priority:
        valid_priorities = ("low", "medium", "high")

        while True:
            priority_input = input("Set priority (low, medium, high) (or press ENTER to skip): ").lower()
            if priority_input == "":
                return Priority.NONE
            if priority_input in valid_priorities: # can be done differently?
                return Priority[priority_input.upper()]
            else:
                print("Invalid selection!")




    def search_task_index(self) -> Optional[int]:
        self.task_report()
        while True:   
            try:
                search_index = int(input("Enter Task Index (0 to quit): "))
                if search_index == 0:
                    print("Search closed")
                    return None
                elif 1 <= search_index <= len(self.all_tasks):
                    return search_index
                else:
                    print("Task does not exist!")
            except ValueError:
                print("Invalid selection!")


    def set_status(self) -> str:
        selected_index = self.search_task_index()
        if selected_index == None:
            return "No status modified"

        selected_task = self.all_tasks[selected_index-1]
        selected_task.status = not selected_task.status
        return f"Task: {selected_task.description} | Status: {'[✔]' if selected_task.status else '[ ]'}"


    def remove_task(self) -> str:
        selected_index = self.search_task_index()
        if selected_index == None:
            return "No task removed"

        self.all_tasks.pop(selected_index-1)
        return "Task is removed!"




    def search_task_name(self) -> Optional[List[Task]]:
        self.task_report() 

        search_name = input("Enter Task Name (ENTER to quit): ").lower()

        if search_name.strip() == "":
            print("Search closed")
            return None
        
        matching_tasks = []
                
        for task in self.all_tasks:
            if search_name in task.description.lower():
                matching_tasks.append(task)

        if matching_tasks:
            for task in matching_tasks:
                print(task)
            return matching_tasks
        else:
            print("No task under this descriprion!")
            return None




    def task_report(self) -> List[Task]:
        self.all_tasks.sort(key=lambda x: x.deadline)

        for index, task in enumerate(self.all_tasks, start=1):
            print(f"{index}. {task}")

        return self.all_tasks


    def task_report_sorted_priority(self) -> List[Task]:
        self.all_tasks.sort(key=lambda task: task.priority.value)

        for index, task in enumerate(self.all_tasks, start=1):
            print(f"{index}. {task}")

        return self.all_tasks

    
    def delete_all_tasks(self) -> str:
        if not self.all_tasks:
            return "No tasks to delete"
        else:
            self.all_tasks = []
            return "All tasks have been deleted."




    def save_task_report(self, filename: str = "tasks.txt") -> None:
        try:
            tasks_data = []
            for task in self.all_tasks:
                task_dict = {
                    "Description": task.description,
                    "Category": task.category, 
                    "Deadline": task.deadline,
                    "Priority": task.priority.name,
                    "Status": "[✔]" if task.status else "[ ]"
                }
                tasks_data.append(task_dict)


            with open(filename, "w") as file:
                json.dump(tasks_data, file, indent=4)
            print(f"Tasks saved successfully to {filename}")
        except Exception as e:
            print(f"unexpected error: {e}")


    def open_task_report(self, filename: str = "tasks.txt") -> None:
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
            self.all_tasks = []

            for task_data in tasks_data:
                description = task_data["Description"]
                category = task_data["Category"]
                deadline = task_data["Deadline"]
                priority = Priority[task_data["Priority"].upper()]
                status = task_data["Status"] == "[✔]"

                new_task = Task(description, category, deadline, priority, status)
                self.all_tasks.append(new_task)

            print(f"Tasks loaded successfully from {filename}")

        except Exception as e:
            print(f"unexpected error: {e}")

    


task_manager = TaskManager()


while True:
    
    print("\n===== To-Do List Manager =====")
    print("1. Add New Task\n2. Set task as completed\n3. Remove task\n4. Search task by name\n5. Task Report | Sort by deadline")
    print("6. Task Report | Sort by priority\n7. Save tasks to tasks.txt file\n8. Open tasks.txt file\n9. Delete all Tasks\n0. Exit")

    try:
        menu_selection = int(input("Enter your selection: "))
        if 0 <= menu_selection <= 9:
            if menu_selection == 0:
                print("===    Program is Closed    ===")
                break
            elif menu_selection == 1:
                task_manager.add_task()
                # task_manager.task_report()
            elif menu_selection == 2:
                print(task_manager.set_status())
            elif menu_selection == 3:
                print(task_manager.remove_task())
            elif menu_selection == 4:
                task_manager.search_task_name()
            elif menu_selection == 5:
                task_manager.task_report()
            elif menu_selection == 6:
                task_manager.task_report_sorted_priority()
            elif menu_selection == 7:
                task_manager.save_task_report()
            elif menu_selection == 8:
                task_manager.open_task_report()
            elif menu_selection == 9:
                print(task_manager.delete_all_tasks())
        else:
            print("Invalid menu selection!")
    except ValueError:
        print("Invalid symbol entered!")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        