# 📝 AI-Powered Daily Task Scheduler

A **Gamified Productivity To-Do List** built with **Python**, **Tkinter**, and **SQLite**, designed to help users **track tasks, manage deadlines, and monitor productivity**.

---

## 🌟 Features

### Version 1 — Core To-Do List
- Add tasks with deadlines and priorities (Low / Medium / High)
- Mark tasks as done or pending
- View all tasks in a color-coded list
- Persistent storage using SQLite database

### Version 2 — Gamified Productivity
- Reward points for completing tasks on time
- Daily streak tracking
- Unlock lifelines and badges for motivation
- Dashboard with stats: tasks completed, points, streaks

### Version 3 — AI Analytics & Visualization
- Visual progress charts (line, bar, radial)
- Analyze productivity trends and completion rates
- AI-generated insights and suggestions
- Weekly summary reports

---

## 🗂 Database Design

**Table:** `tasks`
| id | task | priority | deadline | created_at | completed_at | status |
|----|------|----------|---------|------------|--------------|--------|

**Table:** `user_stats`
| id | points | tasks_completed | lifelines | streak_days |

---

## 🖥️ Tech Stack
- Python 3.x
- Tkinter (GUI)
- SQLite (Database)
- Matplotlib (Graphs/Charts)
- AI/ML logic (for productivity insights)

---

## 📂 Project Structure

```

ToDoList-App/
│
├── README.md
├── requirements.txt
├── todo_db.db
├── main.py
├── modules/
│   ├── db_handler.py
│   └── rewards.py
├── assets/
└── graphs/

````

---

## 📌 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
````

2. Run the app:

   ```bash
   python main.py
   ```
3. Add tasks, mark completion, and track your progress!

---

## 📈 Screenshots

*(Add your screenshots here once the app is functional)*

```

---

# **2️⃣ Detailed Action Plan (as a To-Do List)**

### **V1 — Core DBMS App**
- [ ] Set up SQLite database (`tasks` table)  
- [ ] Create Tkinter window and layout  
- [ ] Implement **Add Task** (task name, deadline, priority)  
- [ ] Implement **Mark Task Done / Pending**  
- [ ] Display **All Tasks** in a scrollable list with color-coding  
- [ ] Implement **Persistent Storage** (read/write from DB on startup/exit)  
- [ ] Test V1 thoroughly and push to GitHub  

### **V2 — Gamified Productivity**
- [ ] Add **Points System** for task completion  
- [ ] Implement **Daily Streak Tracker**  
- [ ] Add **Badges / Rewards / Lifelines**  
- [ ] Create **Stats Dashboard** (tasks completed, points, streaks)  
- [ ] Update UI to show points & streaks  
- [ ] Test V2 thoroughly and push to GitHub  

### **V3 — AI Analytics & Visualization**
- [ ] Integrate **Matplotlib graphs** (line, bar, radial)  
- [ ] Implement **AI-based productivity insights** (rule-based or ML model)  
- [ ] Add **weekly summary reports** (PDF/CSV)  
- [ ] Update UI to include analytics page  
- [ ] Test V3 thoroughly and push to GitHub  


