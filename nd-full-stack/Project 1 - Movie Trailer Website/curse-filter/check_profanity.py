import urllib

def read_text():
    quotes = open(r"C:\Users\Jason\OneDrive\_udacity\nd-full-stack\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity alert!")
    else:
        print("No profanity!")
    
    

read_text()    
