alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

import art
print(art.logo)


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text+= char
      continue
    position = alphabet.index(char)
    new_position = position + shift_amount
    if new_position > 25:
      new_position = new_position % 26
    elif new_position <0:
      new_position += 26
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


while input('Do you want to try again? (yes/no) ').lower() == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text,shift_amount=shift,cipher_direction=direction)