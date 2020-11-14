#takes a two-word string and returns True if boths words begin with the same letter

def animalCrackers(text):
    wordList = text.lower().split()
    return wordList[0][1] == wordList[0][1]
        

print(animalCrackers("pretty Pig"))