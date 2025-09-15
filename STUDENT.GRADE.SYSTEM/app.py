import pandas as pd

# Initial Data
data = [
    {"Name": "Rahul", "Algebra": 45, "Arithmetic": 40, "General English": 42},
    {"Name": "Priya", "Algebra": 48, "Arithmetic": 50, "General English": 49},
    {"Name": "Amit", "Algebra": 30, "Arithmetic": 35, "General English": 32},
]

df = pd.DataFrame(data)

def calculate_fields():
    df["Total"] = df[["Algebra", "Arithmetic", "General English"]].sum(axis=1)
    df["Average"] = df["Total"] / 3
    df["Grade"] = df["Average"].apply(lambda avg: "A" if avg >= 50 else "B" if avg >= 40 else "C")
    df["Section"] = "AGE"

def add_student():
    name = input("Enter name: ")
    algebra = int(input("Algebra marks: "))
    arithmetic = int(input("Arithmetic marks: "))
    english = int(input("General English marks: "))
    df.loc[len(df)] = [name, algebra, arithmetic, english, 0, 0, "", ""]
    calculate_fields()

def update_name():
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")
    df.loc[df["Name"] == old_name, "Name"] = new_name

def delete_student():
    name = input("Enter name to delete: ")
    global df
    df = df[df["Name"] != name]

def update_marks():
    name = input("Enter name to update marks: ")
    if name in df["Name"].values:
        subject = input("Which subject? (Algebra / Arithmetic / General English): ")
        new_mark = int(input("Enter new mark: "))
        df.loc[df["Name"] == name, subject] = new_mark
        calculate_fields()
    else:
        print("Name not found.")

def display():
    print("\nCurrent Data:\n", df[["Name", "Algebra", "Arithmetic", "General English", "Total", "Average", "Grade", "Section"]])

def save_file():
    df.to_excel("isa_final_report.xlsx", index=False)
    print("Saved as 'isa_final_report.xlsx'")

# Main Program
calculate_fields()

while True:
    print("\n--- ISA Manager ---")
    print("1. Add Student")
    print("2. Update Name")
    print("3. Delete Student")
    print("4. Update Marks")
    print("5. Show Report")
    print("6. Save and Exit")
    choice = input("Enter choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_name()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        display()
    elif choice == "6":
        save_file()
        break
    else:
        print("Invalid choice. Try again.")