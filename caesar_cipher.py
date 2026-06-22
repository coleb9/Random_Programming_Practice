letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


def shift_letter(char, shift):
    if char.lower() not in letters:
        return char

    old_index = letters.index(char.lower())
    new_index = (old_index + shift) % len(letters)
    new_char = letters[new_index]

    if char.isupper():
        return new_char.upper()

    return new_char


def encode(shift, message):
    encoded = ""
    for char in message:
        encoded += shift_letter(char, shift)
    print(encoded)


def decode(shift, message):
    decoded = ""
    for char in message:
        decoded += shift_letter(char, -shift)
    print(decoded)


def get_shift():
    while True:
        shift = input("Enter an amount to shift: ")
        try:
            return int(shift)
        except ValueError:
            print("Please enter a whole number, like 3 or 13.")


print("Welcome to the Caesar Cipher.")

while True:
    choice = input("Would you like to encode or decode a message? Enter anything else to exit. ").lower()
    if choice == "encode":
        shift = get_shift()
        message = input("Enter the message you would like to encode: ")
        encode(shift, message)
    elif choice == "decode":
        shift = get_shift()
        message = input("Enter the message you would like to decode: ")
        decode(shift, message)
    else:
        break


