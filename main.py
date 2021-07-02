from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
def winner(bidders):
  maxBid = 0
  winner = ""

  for key in bidders:
    if bidders[key] > maxBid:
      winner = key
      maxBid = bidders[key]

  print(f"The winner is {winner} with a bid of {maxBid}")

print(logo)
bidders = {}
running = True
while running:
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  bidders[name] = int(bid)
  anyBidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if anyBidders == "no":
    running = False
  clear()

winner(bidders)


  



