alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt():
    encoded_word=""
    for char in text:
        if char not in alphabet:
            encoded_word=encoded_word + char 
        else:
            position_letter=alphabet.index(char)
            new_position=position_letter + shift
            if new_position > 25:
                new_position=new_position % 26
            encoded_letters=alphabet[new_position]
            for x in encoded_letters:
                encoded_word=encoded_word + x
    print(f"encoded word ={encoded_word}")            
def decrypt():
    decoded_word=""
    for char in text:
        if char not in alphabet:
            decoded_word=decoded_word + char
        else:
            position_letter=alphabet.index(char)
            new_position=position_letter - shift
            if new_position <0:
                new_position=26 + new_position
            decoded_letters=alphabet[new_position]
            for y in decoded_letters:
                decoded_word=decoded_word + y
    print(f"decoded word ={decoded_word}")
      
def caesar(text, shift):
    if direction=="encode":
       encrypt()
    else:
        decrypt()      
caesar(text, shift)
restart_Cipher=input("Type 'Yes' if you want to go again, Otherwise, type, 'No'.\n")
while  restart_Cipher=='Yes'.lower():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift)
    restart_Cipher=input("Type 'Yes' if you want to go again, Otherwise, type, 'No'.\n")
    if restart_Cipher=='No'.lower():
       print("Good Bye!")
        
    
                
                
    
             

