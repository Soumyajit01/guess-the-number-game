import random


def play():
    num = random.randint(0,50)
    print(num)
    print("Enter your guess between 0-50")
    chances =0
    name = input("Enter your name: ")
    while (True):
        guess = int(input("Enter guess:"))
        chances+=1
        if guess>num:
            print("enter a smaller one!")
        elif guess<num:
            print("Enter a greater one!")
        elif guess==num:
            print("you guessed it correctly!")
            print(f"You guessed it in {chances} number of guesses")
            with open("scores.txt", 'a') as f:
                f.write(f"{name}: {chances}\n")

            f = open("highscore.txt", 'r+')
            highscore = f.read()
            f.close()
            if chances<int(highscore):
                with open('highscore.txt','w') as f:
                    f.write(str(chances))
                print('You just broke the highscore!')
            break

while True:
    print("Press 'p' to play again and 'q' to quit")
    replay = input().lower()
    if replay=='p':
        play()
    elif replay=='q':
        break 
    