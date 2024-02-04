import cv2
import numpy as np


word = "kuşburnu"
word = word.lower()
blank = ""
previousletters = set()
attempt = 0
left = 4
chances = 4
text = ""


def draw_hangman(image, attempt, text):
    # Draw pole figure
        cv2.putText(image, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.line(image, (50, 400), (150, 400), (255, 255, 255), 2)  # Base
        cv2.line(image, (100, 400), (100, 100), (255, 255, 255), 2)  # Vertical pole
        cv2.line(image, (100, 100), (200, 100), (255, 255, 255), 2)  # Top horizontal pole
        cv2.line(image, (100, 160), (150, 100), (255, 255, 255), 2)  # Diagonal pole
        cv2.line(image, (200, 100), (200, 150), (255, 255, 255),2)

        if attempt >= 1:
            cv2.circle(image, (200, 170), 20, (255, 255, 255), 2)  # Head
        if attempt >= 2:
            cv2.line(image, (200, 190), (200, 260), (255, 255, 255), 2)  # Body
        if attempt >= 3:
            cv2.line(image, (200, 260), (220, 290), (255, 255, 255), 2)  # Right leg
            cv2.line(image, (200, 260), (180, 290), (255, 255, 255), 2)  # Left leg
        if attempt >= 4:
            cv2.line(image, (200, 210), (230, 230), (255, 255, 255), 2)  # Right arm
            cv2.line(image, (200, 210), (170, 230), (255, 255, 255), 2)  # Left arm

def img_show(attempt, text):

    image_size = (300, 400, 3)  # I recreate and draw the image each time, if I don't the changes may overlap.
    blank_image = np.zeros(image_size, dtype=np.uint8)

    draw_hangman(blank_image, attempt, text)
    cv2.imshow('Hangman', blank_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    text = ""
    draw_hangman(blank_image, attempt, text)  # Cleaning text


for j in range(len(word)):
    blank += "_"

print(blank)
while True:

    if attempt == chances:  # When attempts finished, means game over
        print("game over You Lost")
        text = "Game over You Lost"

        img_show(attempt, text)
        break

    letter = input("Enter the letter: ").lower()

    if letter in previousletters:  # if You use the same word before its calculating as an attempt
        attempt += 1
        left -= 1
        print("Entered same letter, attempts left:"+str(left))

        if attempt == chances:  # If the game is over, send directly to the game over window
            continue

        text = "Entered same letter, attempts left: "+str(left)
        img_show(attempt, text)
        continue

    oldblank = blank  # Taking old blank before changes at for loop.

    for i in range(len(word)):
        if word[i:i+1] == letter:
            blank = blank[0:i] + letter + blank[i+1:]
            previousletters.add(letter)

    print(blank)

    if oldblank == blank: # if you can't find another letter it means the blank didn't changed so you entered wrong letter.
        attempt += 1
        left -= 1
        print("Entered Wrong letter, attempts left:"+str(left))

        if attempt == chances:  # If the game is over, send directly to the game over window
            continue

        text = "Entered wrong letter, attempts left: "+str(left)
        img_show(attempt, text)

    if blank == word:
        print("You Won")

        text = "You Won with "+str(attempt)+" mistakes"
        img_show(attempt, text)
        break

