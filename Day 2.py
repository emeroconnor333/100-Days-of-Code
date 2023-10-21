#tip calculator
print("Welcome to the tip calculator!")
total= float(input("What was the total bill? €"))
tip= float(input("How much tip would you like to give? 10, 12 or 15? "))
people= float(input("How many people split the bill? "))
pay= (total/ people) * (1 + (tip/ 100))
round_pay= round(float(pay), 2)
round_pay= "{:.2f}".format(round_pay)
print(f"Each person should pay: €{round_pay}")