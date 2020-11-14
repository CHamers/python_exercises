#Given a sentence, return a sentence with the words reversed.

def masterYoda(text):
    wordList = text.split()
    reversedWordList = wordList[::-1]
    reversedText = " ".join(reversedWordList)
    return reversedText
        

print(masterYoda("pretty Pig"))