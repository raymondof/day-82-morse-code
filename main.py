from resources import dictionary

continue_prog = True
while continue_prog:

    text_to_convert = input("Enter text to convert to morse code: ").lower()

    if text_to_convert == "quit":
        continue_prog = False
        print("The program is closing now.")
    else:
        morse = ""
        for character in text_to_convert:
            #print(character)
            if character in dictionary:
                # The space between letters is three units, therefore 3 spaces
                morse += dictionary[character] + "   "
            elif character == " ":
                # The space between words is seven units, therefore add 4 spaces when space
                morse += "    "

        print(morse)
