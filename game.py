from sink import words
from healthbar import health_phases
import random
import string


def vword(words):
    word=random.choice(words)
    return word.upper()

def ingame():
    word= vword(words)
    choicenWord=set(word)
    alpha= set(string.ascii_uppercase)
    doneLetter=set()
    health=7
    
    while len(choicenWord)>0 and health>0 :
        print("\n===== YOUR NEXT TURN =====\n")
        print("you have",health,"chances and you used these letter:",','.join(doneLetter))
        runing=[letter if letter in doneLetter else '-' for letter in word]
        print(health_phases[health])
        print('The Word:',''.join(runing))
        user=input("guess a letter").upper()
        if user in alpha and len(user) == 1:
            if user in doneLetter:
                print(f"you alrady used {user}")
            else:
                doneLetter.add(user)
                if user in choicenWord:
                    choicenWord.remove(user)
                else:
                    health =health-1
                    print ("yore letter is not in the word")
        else:
            print("invalid character!")
    print("\n========== RESULT ==========\n")
    if health==0:
        print(health_phases[health])
        print("you lost the game The word was:",word)
    else :
        print("Victory is yours! You conquered the challenge with skill and determination—well done!, The word was",word)


ingame()


