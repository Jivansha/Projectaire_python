import urllib.request

def check():
    quotes = open("E:\programs\python\movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text):
    connection =urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+text)
    output = connection.read()
    print(output)
    connection.close()
    


check()
