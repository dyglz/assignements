### **📌 To-Do List Manager – Full Task Description**  

**💡 Objective:**  
Build a terminal-based **To-Do List Manager** where users can add, remove, and mark tasks as completed. The program should store tasks using basic **data types** (`str`, `list`, `dict`) and allow interaction through a simple menu.  

---

## **🌟 Mandatory Requirements (Base Task - 10 points)**  

✅ **1. Add Tasks**  
- Users can add a task by providing a description.  
- Tasks should be stored in a **list of dictionaries**, each having:  
  ```python
  {"task": "Buy groceries", "done": False}
  ```  
  
✅ **2. View Tasks**  
- Show all tasks, with **[✔]** for completed ones and **[ ]** for pending ones.  

✅ **3. Mark Tasks as Completed**  
- Users can select a task by **index number** to mark it as completed.  

✅ **4. Remove Tasks**  
- Users should be able to remove a specific task from the list.  

✅ **5. Keep Running Until User Exits**  
- The program should run in a loop, allowing multiple operations until the user chooses to exit.  

✅ **6. Basic Input Validation**  
- Ensure users enter valid inputs (e.g., prevent marking a non-existent task).  

✅ **6. Github**  
- Upload your project to Github.

---

## **🌟 Extra Features (Bonus Points - Up to 5 extra points!)**  

🔹 **7. Save & Load Tasks (1 point)**  
- Store tasks in a file (`tasks.txt`) so they persist between sessions.  

🔹 **8. Task Categories (1 point)**  
- Allow users to assign a category to each task (e.g., "Work", "Personal").  

🔹 **9. Due Dates (1 point)**  
- Let users specify a **due date** for each task.  

🔹 **10. Prioritize Tasks (1 point)**  
- Allow tasks to be sorted by priority (e.g., **High, Medium, Low**).  

🔹 **11. Search for Tasks (1 point)**  
- Enable searching for a task by name.  

---

## **🛠️ Example Program Run**  

```
===== To-Do List Manager =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Remove Task
5. Exit
Enter your choice: 1

Enter task description: Buy milk
Task added!

===== To-Do List =====
1. Buy milk [ ]  
Enter task number to mark as completed: 1
Task "Buy milk" marked as completed!

===== To-Do List =====
1. Buy milk [✔]

Enter your choice: 5
Goodbye!
```

---

Good luck! 🚀
