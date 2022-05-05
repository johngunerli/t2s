import webbrowser

def open_site(MyText):
    if 'open' in MyText:
        # whatever is after the word open 
        text = MyText.split('open')[1]
        # remove the space
        text = text.strip()
        url = 'https://www.'+text+'.com'
        webbrowser.open(url)
        return 0
    else:
        return -1


def search_site(MyText):
        # whatever is after the word search 
        text = MyText.split('search')[1]
        # remove the space
        text = text.strip()
        url = 'https://www.google.com/search?q='+text
        webbrowser.open(url)
        return 0
        