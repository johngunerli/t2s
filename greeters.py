from SpeakText import t2s



def greeters(MyText):

    greeters = ['hello', 'hi', 'hey', 'hola', 'howdy',

                'greetings', 'good morning', 'good afternoon', 'good evening']

    if MyText in greeters:
        t2s("Hello there!")
        print("Hello there!")

    return -1

