import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '?', '>', '<']


print("Generate a password")
choose_letters = int(input("How many LETTERS do you want in your password? \n"))
choose_numbers = int(input("How many NUMBERS do you want in your password? \n"))
choose_symbols = int(input("How many SYMBOLS do you want in your password? \n"))


password_list = []


for letter in range(1, choose_letters + 1):
    password_list.append(random.choice(letters))
    



for number in range(1, choose_numbers + 1):
    password_list.append(random.choice(numbers))




for symbol in range(1, choose_symbols + 1):
    password_list.append(random.choice(symbols))


print(password_list)
random.shuffle(password_list)
print(password_list)

##
##password_list = " ".join(str(x) for x in password_list)
##print(password_list)
#or

password = ' '

for character in password_list:
    password = password + character
print(f"Your password is {password}")

