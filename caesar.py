from ascii_art import logo
print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
def caesar(direction, user_message, shift_number):
    text = ""
    if direction == "decode":
        shift_number*=-1
    for char in user_message:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_number
            text += alphabets[new_position]
        else:
            text+=char
    print(f"Your {direction}d message is : {text}")

should_continue = True
while should_continue:
    direction = input("Enter your choice: encode for encrypt the message, decode for decrypt the message: ")
    user_message = input("Enter your message: ").lower()
    shift_number = int(input("Enter the shift number: "))

    shift_number = shift_number %  26
    caesar(direction, user_message, shift_number)
    
    user_choice = input("Type yes if you want to continue, otherwise type no: ").lower()
    if user_choice == "yes":
        should_continue = True
    elif user_choice == "no":
        print("Goodbye!")
        should_continue = False