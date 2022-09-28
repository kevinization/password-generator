#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_characters = nr_letters + nr_numbers + nr_symbols
counter_letters = 0
counter_symbols = 0
counter_numbers = 0
password = []
password_string = ""

for number in range(1, total_characters):
  if(counter_letters != nr_letters):
    random_letters = random.randint(0, len(letters) - 1)
    password += letters[random_letters]
    counter_letters += 1
    
  if(counter_symbols != nr_symbols):
    random_symbols = random.randint(0, len(symbols) - 1)
    password += symbols[random_symbols]
    counter_symbols += 1

  if(counter_numbers != nr_numbers):
    random_numbers = random.randint(0, len(numbers) - 1)
    password += numbers[random_numbers]
    counter_numbers += 1

random.shuffle(password)

for character in password:
  password_string += character
  
print(f"\nYour generated password is: {password_string}")