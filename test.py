import random

rps = ["scissor", "paper", "rock"]

print("ROCK PAPER SC==SORS")
c = input("\n Your Play: ")

computer = random.choice(rps)

if (c == 'scissor' and computer == 'paper'):
    print("Computer PLAY: " + computer + "\nYou WIN!")
elif (c == 'paper' and computer == 'rock'):
    print("Computer PLAY: " + computer + "\nYou WIN!")
elif (c == 'rock' and computer == 'scissor'):
    print("Computer PLAY: " + computer + "\nYou WIN!")
elif (c == 'paper' and computer == 'scissor'):
    print("Computer PLAY: " + computer + "\nYou LOSE!")
elif (c == 'rock' and computer == 'paper'):
    print("Computer PLAY: " + computer + "\nYou LOSE!")
elif (c == 'scissor' and computer == 'rock'):
    print("Computer PLAY: " + computer + "\nYou LOSE!")