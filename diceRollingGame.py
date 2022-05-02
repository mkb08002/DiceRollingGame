####
# Player and Computer each have 3 dice
# They each roll all 3 dice until one player rolls 3 matching dice.
#######

# import random package
import random

# player and computers total score

computer_score = 0
c_dice_one = 0
c_dice_two = 0
c_dice_three = 0

player_score = 0
p_dice_one = 0
p_dice_two = 0
p_dice_three = 0

# define a function below that checks for three matching dice
# function returns True or False
def three_matching_dice(c_dice_one, c_dice_two, c_dice_three, p_dice_one, p_dice_two, p_dice_three):
    global computer_score
    global player_score

# checks for tie
    if c_dice_one == c_dice_two and c_dice_one == c_dice_three and p_dice_one == p_dice_two and p_dice_one == p_dice_three:
        print("You and the computer both rolled 3 matching dice! The game is over.")
        end_game()

# checks if computer wins
    elif c_dice_one == c_dice_two and c_dice_one == c_dice_three:
        computer_score = computer_score + 10
        print("Computer matched 3 dice and earned an extra 10 points.")
        end_game()

# checks if player wins
    elif p_dice_one == p_dice_two and p_dice_one == p_dice_three:
        player_score = player_score + 10
        print("You matched 3 dice and earned an extra 10 points.")
        end_game()
    else:
        roll_the_dice()

# Computer and user roll until one rolls 3 matching dice
# Display the 3 dice with each roll

def roll_the_dice():
    global computer_score
    c_dice_one = random.randint(1,6)
    c_dice_two = random.randint(1,6)
    c_dice_three = random.randint(1,6)
    computer_score = computer_score + c_dice_one + c_dice_two + c_dice_three
    
    print("Computer rolled:")
    print(c_dice_one)
    print(c_dice_two)
    print(c_dice_three)

    global player_score
    p_dice_one = random.randint(1,6)
    p_dice_two = random.randint(1,6)
    p_dice_three = random.randint(1,6)
    player_score = player_score + p_dice_one + p_dice_two + p_dice_three
    
    print("You rolled:")
    print(p_dice_one)
    print(p_dice_two)
    print(p_dice_three)
    
    three_matching_dice(c_dice_one, c_dice_two, c_dice_three, p_dice_one, p_dice_two, p_dice_three)

# Print both the player and computer's final score and report who wins 
def end_game():
    global computer_score
    global player_score
    
    print("Computer's total score: " + str(computer_score))
    print("Your total score: " + str(player_score))
    if player_score > computer_score:
        print("YOU WIN!")
    elif computer_score > player_score:
        print("COMPUTER WINS!")
    else:
        print("IT'S A TIE!")

    play_again = input("Would you like to play again? (y/n) ").lower()
    if play_again == 'y':
        roll_the_dice()
    else:
        print("Goodbye!")


# Let's Begin
print("Let's see if you're lucky enough to beat the computer. The first to roll 3 identical die ends the game. Let's roll!")
start = input("Are you ready? (y/n) ").lower()
if start == "y":
    roll_the_dice()
else:
    print("Goodbye!")
