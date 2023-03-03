alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(start_text, shift_position, cipher_direction):
    end_text = ' '
    if cipher_direction == "decode":
        shift_position = shift_position * -1
    for character in start_text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_position
            end_text += alphabet[new_position]
        else:
            end_text += character
            
    print(f"Here's the {cipher_direction}d result: {end_text}")



from ceaser_art import logo
print(logo)


should_end = False
while not should_end:  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))




    shift = shift % 26
    ceasar(start_text = text, shift_position = shift, cipher_direction = direction)


    restart = input("Type 'yes' if you want to go again. otherwise, type 'no'.\n")
    if restart == "no":
        should_end = False
        print("Good bye")
















##
##def encrypt(normal_text, shift_position):
##
##    cipher_text = " "
##    
##    for letter in normal_text:
##        position = alphabet.index(letter)
##        new_position = position + shift_position
##        cipher_text += alphabet[new_position]
##    print(f"The encoded text is {cipher_text}")
        

#######################################################################

##def decrypt(cipher_text, shift_position):
##    normal_text = ' '
##    for letter in cipher_text:
##        position = alphabet.index(letter)
##        new_position = position - shift_position
##        normal_text += alphabet[new_position]
##    print(f"the decoded text is {normal_text}")
##
##if direction == "encode":
##    encrypt(normal_text = text, shift_position = shift)
##elif direction == "decode":
##    decrypt(cipher_text = text, shift_position = shift)
##






