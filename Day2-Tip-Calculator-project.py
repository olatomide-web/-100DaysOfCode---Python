print("welcome to the tip calculator!")

total_bill = float(input("what was the total bill? \n$"))
tip = int(input("what percentage tip will you like to give? 10, 12 or 15?\n"))
people = int(input("how many people are spliting the bill?\n"))



bill_with_tip = tip / 100 * total_bill + total_bill

bill_per_person = bill_with_tip / people

total_pay = round(bill_per_person,2)
total_pay = "{:.2f}".format(bill_per_person, 2)
print(f"each person should pay ${total_pay}")


