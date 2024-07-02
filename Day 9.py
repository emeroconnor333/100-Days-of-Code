import os
def clear():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (os.name is 'posix')
    else:
        os.system('clear')

print("Welcome to the silent auction")
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

bid_dict = {}
more_bidders = True
while more_bidders:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: €"))
  bid_dict[name] = bid
  more_bidders_ask = input("Are there any other bidders? (type 'yes' or 'no'): ").lower()
  clear()
  if more_bidders_ask == "no":
    more_bidders = False

highest_bid = 0
for name in bid_dict:
  if bid_dict[name] > highest_bid:
    highest_bidder = name
    highest_bid = bid_dict[name]
print(f"The winner is {highest_bidder} with a bid of €{highest_bid}.")
