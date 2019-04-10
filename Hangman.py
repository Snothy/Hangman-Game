import turtle

sonic = turtle.Turtle()
sonic.hideturtle()
lives = 6 #Head, body, 2arms, 2legs.
counter = 0
secret_word = input("Insert word: ").lower()
#Hiding the word from the guesser.
for i in range(1000):
    print(" ")
#Drawing the hanging board.
sonic.penup()
sonic.right(90)
sonic.forward(50)
sonic.right(90)
sonic.forward(50)
sonic.pendown()
sonic.forward(50)
sonic.backward(25)
sonic.right(90)
sonic.forward(250)
sonic.right(90)
sonic.forward(100)
sonic.right(90)
sonic.forward(20)
xrope = sonic.xcor()
yrope = sonic.ycor()
sonic.penup()
sonic.forward(290)
sonic.right(90)
sonic.forward(190)
sonic.right(180)
sonic.pendown()
xword = sonic.xcor()
yword = sonic.ycor()
#Drawing placeholders for the letters.
for letter in secret_word:
    if letter == " ":
        sonic.penup()
        sonic.forward(30)
        sonic.pendown()
        continue
    sonic.forward(20)
    sonic.penup()
    sonic.forward(10)
    sonic.pendown()
lives_lost = 0
attempts_list = []
#Making a copy of the original word, but with spaces.
new_word = []
for letter in secret_word:
    new_word.append(" ")

while lives > lives_lost and ''.join(new_word) != secret_word: #Loop ends when all lives are lost or the word is guessed.
    letters_counter = 0
    guess = input("Enter a guess: ")
    #Minimizing invalid inputs so no unnecessary lives are lost.
    if len(guess) == 1 and guess not in "0123456789":
        pass
    else:
        print("Only one letter, try again.")
        continue
    if guess in attempts_list:
        print("You've already tried that letter, baka.")
        continue
    if guess in secret_word:
        attempts_list.append(guess)
        for index in range(len(secret_word)):
            if guess == secret_word[index]:
                new_word[index] = secret_word[index] #Same length = same index = same letter. Replacing the spaces in the copy by the letters if guessed correctly. 
                sonic.setheading(0)
                sonic.up()
                #Setting the header coordinates to the beginning of the first placeholder letter.
                sonic.setx(xword)
                sonic.sety(yword)
                sonic.down()
                #The length of each letter placeholder is 20, and the space between them is 10, so I skip by 30 until I get to the one I need. If index is 0 it's the first letter so I dont skip.
                for num in range(index):
                    if index == 0:
                        break
                    sonic.up()
                    sonic.forward(30)
                    sonic.down()
                #Setting the header to the middle of the placeholder and moving it up slightly to write the letter.
                sonic.up()
                sonic.forward(10)
                sonic.left(90)
                sonic.forward(2)
                sonic.down()
                sonic.write(guess)
        for letter in secret_word: #Counting how many times the letter appears in the word.
            if guess == letter:
                letters_counter = letters_counter + 1
        print("Correct! There are " + str(letters_counter) + " " + guess + "'s in the word.")
    else:
        attempts_list.append(guess)
        lives_lost = lives_lost + 1
        print("Incorrect! You have " + str(lives - lives_lost) + " lives left.")
        #Positioning header at the end of the rope facing right.
        sonic.setheading(0)
        sonic.up()
        sonic.setx(xrope)
        sonic.sety(yrope)
        sonic.right(90)
        sonic.forward(30)
        if lives_lost == 1: # Draws the head
            sonic.left(90)
            sonic.down()
            sonic.circle(15)
        elif lives_lost == 2: # Draws the body
            sonic.down()
            sonic.forward(70)
        elif lives_lost == 3: # Left foot
            sonic.forward(70)
            sonic.down()
            sonic.left(45)
            sonic.forward(30)
        elif lives_lost == 4: # Right foot
            sonic.forward(70)
            sonic.down()
            sonic.right(45)
            sonic.forward(30)
        elif lives_lost == 5: # Left hand
            sonic.forward(25)
            sonic.down()
            sonic.left(45)
            sonic.forward(20)
        elif lives_lost == 6: # Right hand
            sonic.forward(25)
            sonic.down()
            sonic.right(45)
            sonic.forward(20)
    #Showing the already used letters.
    sonic.setheading(0)
    sonic.up()
    sonic.setx(xrope)
    sonic.sety(yrope)
    sonic.left(180)
    sonic.forward(300)
    sonic.right(90)
    sonic.forward(100)
    sonic.right(90)
    sonic.down()
    if counter == 0:
        sonic.write("Letters attempted: ")
    sonic.up()
    sonic.forward(88)
    sonic.down()
    for n in range(counter):
        sonic.up()
        sonic.forward(10)
        sonic.down()
    sonic.write(guess)
    counter = counter + 1



#Once loop ends one of these is printed.
if lives_lost >= lives:
    print("You lose! Relaunch to try again!")
else:
    print("You win. " + secret_word + " was easy anyway. Relaunch to try again.")

turtle.mainloop()