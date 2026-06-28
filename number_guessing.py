import random 

number = random.randint(0,101)


guesses = 0
over = False

def check_number(guess, number, over):
    if guess > number:
        print("Too High")
        
    elif guess < number:
        print("Too Low ")
        
    else:
        print("You guessed the number!")
        over = True
    
    return over

def choose_mode(mode, num):

    if mode == "hard":
        num = 5
    else:
        num = 10

    return num

print("Let's PLay Number Guesser! ")       
print("I am thinking over a number 1-100")
mode = input("Choose mode: 'hard', 'easy' ")

guesses = choose_mode(mode, guesses)

while guesses >= 1:
    
    guess = int(input("Enter guess: "))
    
    if check_number(guess, number, over) == True: 
        
        break
    else: 
        guesses -= 1
        if guesses == 0:
            print("You Lose!")










