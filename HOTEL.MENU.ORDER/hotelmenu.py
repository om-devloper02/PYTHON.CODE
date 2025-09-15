
# Define the menu of restaurant with numeric choices
menu = {
	1: ('Maharashtrian Veg Thali', 120),
	2: ('Special Veg Thali', 160),
	3: ('Bhakri Thali (2 Bhakris)', 130),
	4: ('Pithla Bhakri', 100),
	5: ('Zunka Bhakri', 90),
	6: ('Chapati Bhaji Plate', 80),
	7: ('Varan Bhat + Papad', 70),
	8: ('Matki Usal + Bhakri', 110),
}

# Greet and display numbered menu
print("WELCOME TO PYTHON RESTAURANT //Bhakri House//")
print("Please select items by number. Enter 0 when you are finished.\n")

for choice_number, (item_name, item_price) in menu.items():
	print(f"{choice_number}. {item_name}: {item_price}")

order_total = 0

while True:
	choice = input(f"\nEnter item number (1-{len(menu)}) or 0 to finish: ")
	if not choice.isdigit():
		print("Please enter a valid number.")
		continue

	choice_num = int(choice)
	if choice_num == 0:
		break
	if choice_num in menu:
		selected_name, selected_price = menu[choice_num]
		order_total += selected_price
		print(f"Added {selected_name} - Rs.{selected_price}. Current total: {order_total}")
	else:
		print("Invalid choice number. Please try again.")

print(f"\nThe total amount to pay is Rs.{order_total}")
