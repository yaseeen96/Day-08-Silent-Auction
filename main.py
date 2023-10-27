from art import logo
from replit import clear

bid_complete = False
bidders = []


def get_highest_bidder():
  highest_bid = 0
  winner_name = ""

  for bidder in bidders:

    if bidder["bid_amount"] > highest_bid:
      highest_bid = bidder["bid_amount"]
      winner_name = bidder["name"]
  return {
      "winner_name": winner_name,
      "winner_bid": highest_bid,
  }


print(logo)
print("Welcome to the secret auction program")

while (not bid_complete):
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidders.append({"name": name, "bid_amount": bid})
  decision = input("Are there any other bidders? Type 'yes' or 'no': ")
  if (decision == "yes"):
    clear()
  elif decision == "no":
    winner = get_highest_bidder()
    winner_name = winner["winner_name"]
    winner_bid = winner["winner_bid"]
    print(f"The highest bidder is {winner_name} with bid ${winner_bid}")
    bid_complete = True
