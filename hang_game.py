import random
import stages

word_collection = [ "CodeAlpha","INternship","Apple","Banana",
                   "Cat","Dog","Elephant","Fish","Guitar","Hat",
                   "Jellyfish","Kangaroo","Lion","Moon",
                   "Necklace","Orange","Penguin","Quilt",
                   "Rainbow","Sun","Turtle""Ice cream"
 ]

picked_word = random.choice(word_collection)
lives = 6

print(picked_word)
visible = []

for i in range(len(picked_word)):
    visible += '_'
print(visible)

gameOver = False

while not gameOver:
    guess_letter = input("Guess a letter:")
    for location in range(len(picked_word)):
        letter = picked_word[location]
        if letter == guess_letter:
            visible[location] = guess_letter
    print(visible)
    if guess_letter not in picked_word:
        lives -= 1
        if lives == 0:
            gameOver = True
            print()
            print()
            print("You lost the game!!")
    if '_' not in visible:
        gameOver = True
        print("YOU WIN THE GAME YAYYYYYY!!!!")
    print(stages.stage[lives])