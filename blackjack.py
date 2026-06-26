import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

face_card_values = {
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}


def draw_card():
    return random.choice(cards)


def hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        if isinstance(card, int):
            total += card
        else:
            total += face_card_values[card]
            if card == "A":
                aces += 1

    # Convert aces from 11 to 1 if necessary
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


# ----------------------
# Initial Deal
# ----------------------

player_hand = [draw_card(), draw_card()]
dealer_hand = [draw_card(), draw_card()]

# ----------------------
# Player Turn
# ----------------------

while True:

    print("\n-------------------")
    print("Dealer shows:", dealer_hand[0])
    print("Your hand:", player_hand)
    print("Your total:", hand_value(player_hand))

    if hand_value(player_hand) > 21:
        print("Bust! Dealer wins.")
        quit()

    choice = input("Hit or Stay? ").lower()

    if choice == "hit":
        player_hand.append(draw_card())
    elif choice == "stay":
        break
    else:
        print("Invalid input.")

# ----------------------
# Dealer Turn
# ----------------------

while hand_value(dealer_hand) < 17:
    dealer_hand.append(draw_card())

# ----------------------
# Results
# ----------------------

player_total = hand_value(player_hand)
dealer_total = hand_value(dealer_hand)

print("\n===================")
print("Dealer hand:", dealer_hand)
print("Dealer total:", dealer_total)
print()
print("Your hand:", player_hand)
print("Your total:", player_total)
print("===================")

if dealer_total > 21:
    print("Dealer busts! You win!")

elif player_total > dealer_total:
    print("You win!")

elif dealer_total > player_total:
    print("Dealer wins!")

else:
    print("Push! It's a tie.")