dict = {}
def populate_dict(name, bid):

    dict[name] = bid
    return dict



print("Welcome to the silent auction!")
while True:
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))
    other_bids = input("Are there any other bidders? 'yes' or 'no'").lower()

    populate_dict(name, bid)
    
    if other_bids == "yes":
        pass
    else:
        break

max = 0
for key in dict:
    if dict[key] > max:
        max = dict[key]

print(f"The highest bid was {max}")





