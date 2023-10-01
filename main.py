from resources import dictionary



def text_to_morse(text):
    morse = ""
    for character in text:
        #print(character)
        if character in dictionary:
            # The space between letters is three units, therefore 3 spaces
            morse += dictionary[character] + "   "
        elif character == " ":
            # The space between words is seven units, therefore add 4 spaces when space
            morse += "    "

        #print(morse)
    return morse


def main():
    continue_prog = True
    while continue_prog:

        prog_select = input("Type 'quit' for quit, 'morse' for morse to text or 'text' for text to morse: ")

        if prog_select == "quit":
            continue_prog = False
            print("The program is closing now.")
        elif prog_select == "text":
            text_to_convert = input("Enter text to convert to morse code: ").lower()
            converted = text_to_morse(text_to_convert)
            print(converted)
        elif prog_select == "morse":
            print("text")
            morse_to_text = input("Enter morse to convert to text: ")
            morse_to_text = "-   ....   ..   ...       ..   ...       .-       -   .   ...   -"

if __name__ == "__main__":
    main()