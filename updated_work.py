# Build a terminal-based To-Do List Manager where 
# users can add, remove, and mark tasks as completed. 
# The program should store tasks using basic data types 
# (str, list, dict) and allow interaction through a simple menu.

# Mandatory Requirements
# 1. Add Tasks
# 2. View Tasks
# 3. Mark Tasks as Completed
# 4. Remove Tasks
# 5. Keep Running Until User Exits
# 6. Basic Input Validation
# 7. Github

# Extra Features
# 1. Save & Load Tasks
# 2. Task Categories
# 3. Due Dates
# 4. Prioritize Tasks
# 5. Search for Tasks

from enum import Enum
from datetime import datetime
from typing import List, Tuple


class Task:
    def __init__(self, description: str = "", category: str = "", deadline: str = "%Y-%m-%d", priority: Enum = None, status: bool = False):
    # Tuple[str] = ("low", "medium", "high")
        self.description = description
        self.category = category
        self.deadline = deadline
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"Description: {self.description}, Category: {self.category}, Deadline: {self.deadline}, Priority: {self.priority.name.lower()}, Status: {'[✔]' if self.status else '[ ]'}"


class Priority(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Task_manager:
    def __init__(self):
        self.all_tasks: List[dict] = []


    def add_task(self):
        description = input("Enter task decription: ")
        category = input("Enter task category: ")
        deadline = task_manager.set_deadline()
        priority = task_manager.set_priority()
        status = False



        new_task = Task(description, category, deadline, priority, status)
        self.all_tasks.append(new_task)

        self.all_tasks.sort(key=lambda x: x.priority.value)



    def set_category(self):
        while True:
            try:
                category =  input("Enter task category: ")

                if category == None:
                    return f"n/a"


            except ValueError as e:
                print(e)
            pass



    def set_deadline(self):
        while True:
            due_date = input("Enter deadline (YYYY-MM-DD): ")

            if due_date == "":
                return "n/a"
            
            try:
                deadline = datetime.strptime(due_date, "%Y-%m-%d")
                return deadline.strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format!")


    def set_priority(self):
        valid_priorities = ("low", "medium", "high")

        while True:
            try:
                priority_input = input("Set priority (low, medium, high): ").lower()
                if priority_input == "":
                    return Priority.NONE
                if priority_input in valid_priorities:
                    return Priority[priority_input]
                else:
                    print("Invalid selection!")
                    continue
            except ValueError as e:
                print(e)



    def set_status(self):
        self.task_report()
        while True:
            try:
                selected_index = int(input("Enter the number of task to complete: "))
                if 1 <= selected_index <= len(self.all_tasks):
                    selected_task = self.all_tasks[selected_index-1]
                    if hasattr(selected_task, "status"):
                        selected_task.status = not selected_task.status
                        print(f"Task: {selected_task.description} | Status: {'[✔]' if selected_task.status else '[ ]'}")
                        break
                else:
                    print("Invalid selection!")
                
            except ValueError:
                print("Enter a valid number!")




    def remove_task(self):
        pass


    def task_report(self):
        for index, task in enumerate(self.all_tasks, start=1):
            print(f"{index}. {task}")

        return self.all_tasks


    def search_task(self):
        self.task_report()

        while True:
            try:
                search_selection = input("Search Task by Index (I) or Name (N): ").lower()
                if search_selection == "i":
                    search_index = int(input("Enter task index: "))
                    if 1 <= search_index <= len(self.all_tasks):
                        selected_task = self.all_tasks[search_index-1]
                        print(selected_task)
                    else:
                        print("Invalid selection!")

                elif search_selection == "n":
                    search_name = input("Enter task description: ")
                    if search_name in self.all_tasks["description"]:
                        
                        pass
                else:
                    print("Invalid selection (I/N)!")
                
            except ValueError:
                print("Value Error!")

            pass




    def save_task_report(self):
        pass




task_manager = Task_manager()


while True:
    
    print("\n===== To-Do List Manager =====")
    print("1. Add New Task\n2. Set Category\n3. Set Deadline\n4. Set Priority\n5. Set task as completed")
    print("6. Remove task\n7. View Task Report\n8. Search\n9. Save tasks to .txt\n0. Exit")

    try:
        menu_selection = int(input("Enter your selection: "))
        if 0 <= menu_selection <= 9:
            if menu_selection == 0:
                # task_manager.save_and_exit(self)
                break
            elif menu_selection == 1:
                task_manager.add_task()
                continue
            elif menu_selection == 2:
                task_manager.set_category()
                continue
            elif menu_selection == 3:
                task_manager.set_deadline()
                continue
            elif menu_selection == 4:
                task_manager.set_priority() 
                continue
            elif menu_selection == 5:
                task_manager.set_status()
                continue
            elif menu_selection == 6:
                task_manager.remove_task()
                continue
            elif menu_selection == 7:
                task_manager.task_report()
                continue
            elif menu_selection == 8:
                task_manager.search_task()
                continue
            elif menu_selection == 9:
                task_manager.save_task_report()
                continue
        else:
            print("Invalid selection (1 - not in range)")
    except ValueError:
        print("Invalid selection (2 - wrong type)")
    except Exception as e:
        print(e)
        
