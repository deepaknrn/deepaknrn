from replit import clear
#import art
#HINT: You can call clear() to clear the output in the console.

#print(art.logo)
print("\n Welcome to the secret auction program")
condition=True
dictionary={} #create an empty dictionary

while condition:
  name=input("\n What is your name?:")
  bid=input("\n What's your bid: $")
  dictionary[name]=bid
  choice=input("\n Are there any other bidders? Type 'yes' or 'no': ")
  if choice=="yes":
    clear()
    condition=True
  else:
    condition=False

current_highest_name=""
current_highest_bid=0

for namee in dictionary:
  if int(dictionary[namee])>current_highest_bid:
    current_highest_bid=int(dictionary[namee])
    current_highest_name=namee

print(f"\n The current highest bidder is: {current_highest_name} and the bid is {current_highest_bid}")
