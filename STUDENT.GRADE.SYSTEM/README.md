# ISA Manager (Internal Student Assessment)

This is a simple Python project to manage student marks, calculate totals, averages, grades, and export the final report to Excel.

---

## 📌 Features
- Add a new student with marks for Algebra, Arithmetic, and General English.
- Update student name.
- Delete a student.
- Update marks for a specific subject.
- Automatically calculate:
  - **Total Marks**
  - **Average**
  - **Grade** (A, B, C)
  - **Section** (AGE – Algebra, General English, Arithmetic)
- Display student report in the console.
- Save the report as an **Excel file** (`isa_final_report.xlsx`).

---

## 📊 Grading System
- **A** → Average ≥ 50  
- **B** → Average ≥ 40  
- **C** → Average < 40  

---

## ⚙️ Requirements
Make sure you have Python installed. Install required package:

```bash
pip install pandas openpyxl
▶️ How to Run
Save the script as isa_manager.py.

Open terminal/command prompt in the project folder.

Run:

bash
Copy code
python isa_manager.py
📖 Menu Options
When you run the program, you will see this menu:

pgsql
Copy code
--- ISA Manager ---
1. Add Student
2. Update Name
3. Delete Student
4. Update Marks
5. Show Report
6. Save and Exit
1 → Add Student: Enter name and marks for subjects.

2 → Update Name: Change student’s name.

3 → Delete Student: Remove a student by name.

4 → Update Marks: Update marks for any subject.

5 → Show Report: Display current data in table format.

6 → Save and Exit: Save the report as Excel and close program.

📂 Output Example
Console Report
less
Copy code
Current Data:
     Name  Algebra  Arithmetic  General English  Total    Average Grade Section
0   Rahul       45          40               42    127  42.333333     B     AGE
1   Priya       48          50               49    147  49.000000     B     AGE
2    Amit       30          35               32     97  32.333333     C     AGE
Excel File
Saved as isa_final_report.xlsx with all calculated fields.