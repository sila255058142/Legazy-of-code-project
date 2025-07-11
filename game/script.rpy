# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Elon    = Character("Elon",color="#ffffff")      # MainCharactor
define Rainy   = Character("Rainy",color="#008cff")     # Elon Friend
define M       = Character("")                            # Moderator


# The game starts here.

label start:
    Rainy   "Hey! Elon Hey Elon wake up!!!"
    Rainy   "Why he didn't awake..."
    Elon    "Ugh....."

    scene ruinworld
    


    Rainy "{b}FINALLY{\b}, You awake I start to worry about you now bro..."
    Elon    "H...How much Did i Sleep?"

    hide rainntnormal
    show rainnysurprise
    Rainy   "Did you not know?,After We escape that Ai until we Arrive our base you go to bed and lay dowm on it"
    Rainy   "And it passed 12 hour!! did you know?"


    return
