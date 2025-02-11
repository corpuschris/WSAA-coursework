import requests

# Step 1: Shuffle a new deck of cards
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)

if response.status_code != 200:
    print("Failed to shuffle the deck.")
    exit()

# Get the deck_id from the response
deck_id = response.json()["deck_id"]
print(f"Deck ID: {deck_id}")

# Step 2: Draw 5 cards from the deck
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)

if response.status_code != 200:
    print("Failed to draw cards.")
    exit()

# Step 3: Print the value and suit of each card
cards = response.json()["cards"]
print("Your 5 cards are:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")

# Step 4: Check for pairs, triples, straights, or flush
values = []
suits = []
for card in cards:
    values.append(card['value'])
    suits.append(card['suit'])

# Check for pairs or triples
value_counts = {}
for value in values:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

has_pair = False
has_triple = False
for count in value_counts.values():
    if count == 2:
        has_pair = True
    if count == 3:
        has_triple = True

if has_triple:
    print("Congratulations! You have a triple.")
elif has_pair:
    print("Congratulations! You have a pair.")

# Check for a straight
value_map = {
    "JACK": 11,
    "QUEEN": 12,
    "KING": 13,
    "ACE": 14
}
numerical_values = []
for value in values:
    if value in value_map:
        numerical_values.append(value_map[value])
    elif value.isdigit():
        numerical_values.append(int(value))
    else:
        numerical_values.append(0)  # Handle unexpected values

numerical_values.sort()
is_straight = True
for i in range(len(numerical_values) - 1):
    if numerical_values[i + 1] != numerical_values[i] + 1:
        is_straight = False
        break

if is_straight:
    print("Congratulations! You have a straight.")

# Check for a flush
is_flush = True
first_suit = suits[0]
for suit in suits:
    if suit != first_suit:
        is_flush = False
        break

if is_flush:
    print("Congratulations! You have a flush!")