from SpeakText import t2s



def curses(MyText):

    if '*' in MyText:

        t2s("That's mean!")

        print("That's mean :(!")

        return 0

    return -1

