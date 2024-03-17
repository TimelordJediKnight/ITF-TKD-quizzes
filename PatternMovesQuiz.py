import random
    

def moveCountQuiz(rank):
    moves = []
    patterns = []
    incorrectGuesses = 0
    correctGuesses = 0
    
    ranks = ["ninth gup", "eigth gup", "seventh gup", "sixth gup", "fifth gup", "fourth gup", 
             "third gup", "second gup", "first gup", "first dan", "second dan", "third dan", "fourth dan",
             "fifth dan", "sixth dan"]
    
    movesInPatterns = {"Chon-Ji":19, "Dan-Gun":21, "Do-San":24, "Won-Hyo":28, "Yul-Guk":38, 
                   "Joon-Gun":32, "Toi-Gye":37, "Hwa-Rang":29, "Choong-Mu":30, "Kwon-Gae":39, 
                   "Poe-Eun":32, "Ge-Baek":44, "Eui-Am":45, "Choong-Jang":52, "Ko-Dang":45,
                   "Sam-Il":33, "Yoo-Sin":68, "Choi-Yong":46, "Yong-Gae":49, "Ul-Ji":42, "Moon-Moo":61,
                   "So-San":72, "Se-Jong":24, "Tong-Il":56}

    for i in movesInPatterns.values():
        moves.append(i)
    
    for i in movesInPatterns.keys():
        patterns.append(i)

    if rank in ranks[:9]:
        moves = moves[:ranks.index(rank)+1]
        patterns = patterns[:ranks.index(rank)+1]
        
    elif rank in ranks[9:13]:
        moves = moves[:15+(3*(ranks.index(rank)-10))]
        patterns = patterns[:15+(3*(ranks.index(rank)-10))]
        
    elif rank == ranks[13]:
        moves = moves[:23]
        patterns = patterns[:23]
    
    while len(patterns) > 0:
        
        i = random.randint(0, len(patterns)-1)
        guess = (input(f"How many moves are in {patterns[i]}?\n"))
        
        while moves[i] != int(guess):
            print("Wrong! Try again.")
            guess = (input(f"How many moves are in {patterns[i]}?\n"))
            incorrectGuesses += 1
            
        if moves[i] == int(guess):
            print("Correct!")
            patterns.pop(i)
            moves.pop(i)
            correctGuesses += 1
            
    print(f"You had {correctGuesses} right guesses and {incorrectGuesses} wrong guesses.")
    
    restart = input("Study again? \n(y)es \n(n)o\n").lower()
    
    return restart

def main():
    rank = input("What rank are you? ")
    restart = moveCountQuiz(rank)
    if restart == "y":
        moveCountQuiz(rank)     

main()