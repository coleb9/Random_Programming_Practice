letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


def encode(shift, message):
    encoded = ""
    for char in message:
        if letters.index(char) + shift > 25:
            encoded += letters[(letters.index(char) + shift) - 26]
        else:
            encoded += letters[letters.index(char) + shift]
    print(encoded)

def decode(shift, message):
    decoded = ""
    for char in message:
        if letters.index(char) - shift < 0:
            decoded += letters[(letters.index(char) - shift) + 26]
        else:
            decoded += letters[letters.index(char) - shift]
    print(decoded)



print("Welcome to the Caesar Cipher.")

while True:
    choice = input("Would you like to encode or decode a message? Enter anything else to exit. ")
    if choice == "encode":
        shift = int(input("Enter an amount to shift: "))
        message = input("Enter the message you would like to encode: ")
        encode(shift, message)
    elif choice == "encode":
        shift = int(input("Enter an amount to shift: "))
        message = input("Enter the message you would like to decode: ")
        decode(shift, message)
    else:
        break


