from resources import dictionary

def text_to_morse(text):
    morse = ""
    for character in text:
        if character in dictionary:
            # The space between letters is three units, therefore 3 spaces
            morse += dictionary[character] + "   "
        elif character == " ":
            # The space between words is seven units, therefore add 4 spaces when space
            morse += "    "
    return morse


def morse_to_text(morse):
    text = ""
    # Create a list where each morse code unit is string in a list
    morse_list = morse.split("   ")
    # Remove unnecessary spaces from the units
    # space is empty string in the list
    for count, morse_unit in enumerate(morse_list):
        morse_list[count] = morse_unit.lstrip()

    for morse_unit in morse_list:
        if morse_unit != "":
            text += list(dictionary.keys())[list(dictionary.values()).index(morse_unit)]
        else:
            text += " "
    return text


def main():
    continue_prog = True
    while continue_prog:

        prog_select = input("Type 'q' for quit, 'm' for morse to text or 't' for text to morse: ")

        if prog_select == "q":
            continue_prog = False
            print("The program is closing now.")
        elif prog_select == "t":
            text_to_convert = input("Enter text to convert to morse code: ").lower()
            converted = text_to_morse(text_to_convert)
            print(converted)
        elif prog_select == "m":
            morse = input("Enter morse to convert to text: ")
            morse = "-   ....   ..   ...       ..   ...       .-       -   .   ...   -"
            text = morse_to_text(morse)
            print(text)
        else:
            print("Input not available, please try again.")

if __name__ == "__main__":
    main()