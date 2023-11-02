#random password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters= int(input("How many letters would you like in your password?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))
n_symbols = int(input(f"How many symbols would you like?\n"))

password = ""

for letter in range(n_letters):
    rand_letter= random.randint(0, (len(letters)-1))
    password= password + letters[rand_letter]

for number in range(n_numbers):
    rand_num= random.randint(0, (len(numbers)-1))
    password= password + numbers[rand_num]

for symbol in range(n_symbols):
    rand_sym= random.randint(0, (len(symbols)-1))
    password= password + symbols[rand_sym]

password_list= list(password)
random.shuffle(password_list)

shuffled_password= ''.join(password_list)
print(shuffled_password)