print("Welcome to Connectinwhizttech")

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter thr total of electricity spend = "))
charge_per_unit = int(input("Enter the chage per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))


total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)
