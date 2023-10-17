
import requests
import os

os.system('cls')

# Define BCX, Default is set to 1
BCX = 1

# Add More cards to the dictionary if desired on new lines
shopping_list = (
    {"Card": "Cornealus", "ID": "199", "Gold": "false", "Edition": "4"},
    {"Card": "Phantom of the Abyss", "ID": "177", "Gold": "false", "Edition": "4"},
    {"Card": "Sea Wreck", "ID": "558", "Gold": "false", "Edition": "8"},
    {"Card": "Immolation", "ID": "559", "Gold": "false", "Edition": "8"}
)

print("--Current Lowest Prices--")
print()

for card in shopping_list:
    lowest_buy_price = float('inf')

    getstring = "https://api.splinterlands.io/market/for_sale_by_card?card_detail_id=" + card["ID"] + "&gold=" + card["Gold"] + "&edition=" + card["Edition"]
    response = requests.get(getstring)
    cards = response.json()

    for foundcard in cards:
        if foundcard["bcx"] == BCX:
            buy_price = foundcard["buy_price"]
            if buy_price < lowest_buy_price:
                lowest_buy_price = buy_price

    print("Card:", card["Card"])
    print(f'Lowest Buy Price: ${lowest_buy_price}, BCX: {BCX}, Gold Foil: {card["Gold"]}')
    print()

os.system('pause')