import random

    
print ("Welcome to Lanz's guessing game!\n")
name = input("Enter your name: ")
print (f"I'll think of a  number and {name} will have to guess the number")
choice = input("Type Game to continue or q to quit: ").lower()
    
if choice == "q":
    print ("Thanks, come again if you have the guts.")
elif choice == "game":
    print ("Great Let's start!\n")
        
    def play_game():
            
        print ("Pick your difficulty:")
        diff = input(
            "Easy (1-10)\n"
            "Normal (1-25)\n"
            "Hard (1-30)\n"
            "Insane (1-50)\n"
            "Intuitive Beast (1-100) (Without hints and only one life)\n\n"
            "Choose: ").lower()
        print()
        if diff == "easy":
            max_num = 10
            lives = 5
            hints = True
        elif diff == "normal":
            max_num = 25
            lives = 5
            hints = True
        elif diff == "hard":
            max_num = 30
            lives = 5
            hints = True
        elif diff == "insane":
            max_num = 50
            lives = 5
            hints = True
        elif diff == "intuitive beast":
            max_num = 100
            lives = 1
            hints = False
        else:
            print("Invalid choice! Redirecting to Normal mode.")
            max_num = 25
            lives = 5
            hints = True
                
        random_number = random.randint(1, max_num)
        print(f"All right {name}, I've picked a number from 1 to {max_num}.")
        print(f"You have {lives} lives before you lose\n")
            
        while lives > 0:
            try:
                guess = int(input("Guess the number! "))
                    
                if guess == random_number:
                    print(f"Congratulations {name}! You guessed the right number!")
                    return
                else:
                    lives -= 1
                    life_word = "life" if lives == 1 else "lives"
                    if hints:
                        if guess > random_number:
                            print(f"Ooops! Too High! {lives} {life_word} left\n")
                        else:
                            print(f"Ooops! Too Low! {lives} {life_word} left\n")
                    else:
                        print(f"Wrong guess! {lives} {life_word} left\n")
                
            except ValueError:
                print("Invalid Guess! Input a valid number.\n")
            
        if lives == 0:
                print(f"Game Over! {name}, The number was {random_number}")
    
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(f"Thanks for playing {name}!")
        break
        
    
    

