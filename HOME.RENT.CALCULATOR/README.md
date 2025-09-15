🏠 Hostel/Flat Expense Splitter

This Python program helps roommates/flatmates calculate and split expenses such as rent, food, and electricity bills equally among all persons.

🚀 Features

Takes input for rent, food, electricity usage, charge per unit, and number of persons

Automatically calculates total expenses

Splits the expenses equally per person

Simple and beginner-friendly program

🛠️ Technologies Used

Python 3.x

📂 Project Structure
Expense_Splitter/
│── main.py       # Main program
│── README.md     # Documentation

2️⃣ Run the program
python main.py

📖 Program Code
print("Welcome to Connectinwhizttech")

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity spend (units) = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)

📊 Example Usage
Welcome to Connectinwhizttech
Enter your hostel/flat rent = 8000
Enter the amount of food ordered = 3000
Enter the total electricity spend (units) = 150
Enter the charge per unit = 10
Enter the number of persons living in room/flat = 4
Each person will pay = 2975

✅ Notes

Make sure all inputs are numbers only

Division uses integer division (//) → result is a whole number

You can change // to / if you want exact float values
