# student-attendance-visualizer
basic bar graph showing attendance of the class
# 🎓 Girish Institute of Technology - Attendance Tracker

A simple **Python Attendance Management System** that allows teachers to record and visualize student attendance using **Matplotlib**.

This project records attendance for a range of roll numbers and generates a **visual attendance report** for the entire class.

---

## 📌 Features

* Enter **section name**
* Define **roll number range**
* Record attendance **period-wise**
* Option to enter:

  * **Present students**
  * **Absent students**
* Automatically calculates **total attendance per student**
* Displays **attendance graph using Matplotlib**
* Clean and simple **command-line interface**

---

## 🛠 Technologies Used

* Python 🐍
* Matplotlib 📊

---

## 📂 How the Program Works

1. Enter the **Section (SEC)**.
2. Enter the **Roll number range** (Example: `1-60`).
3. Enter the **number of periods** conducted.
4. For each period:

   * Enter the **subject name**.
   * Choose whether to enter:

     * Present students (`P`)
     * Absent students
5. The program calculates total attendance.
6. A **bar chart** is generated showing attendance of each student.

---

## 📊 Example Graph

The program generates a **bar graph** where:

* **X-axis → Roll Numbers**
* **Y-axis → Number of Classes Attended**

---

## ▶ How to Run the Program

### 1️⃣ Install Required Library

```bash
pip install matplotlib
```

### 2️⃣ Run the Python File

```bash
python attendance.py
```

---

## 💻 Example Input

```
Enter SEC: A
Enter roll no range: 1-10
Enter how many periods: 2

Period 1
Subject: Python
Enter presentes: 1 2 3 4 5

Period 2
Subject: Maths
Enter absentees: 3 7
```

---

## 📈 Output

The program displays:

* Attendance count for each student
* A **Matplotlib bar graph** representing class attendance

---

## 🚀 Future Improvements

* Individual student attendance report
* Attendance percentage calculation
* CSV file export
* GUI version using Tkinter
* Automatic attendance storage

---

## 👨‍💻 Author

**Girish**

B.Tech Student |Keshav Memorial Engineering College | Learning Python, NumPy, Pandas & Data Visualization 

---

⭐ If you like this project, consider **starring the repository**.
