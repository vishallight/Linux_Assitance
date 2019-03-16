import wikipedia
import webbrowser


def wiki(str):
    try:
        result = wikipedia.summary(str, sentences=2)
        url = "http://en.wikipedia.org/w/index.php?title="
        #webbrowser.open_new_tab(url+str)
        return result
    
    except wikipedia.exceptions.PageError:
        gsearch = "https://www.google.com/search?q="
        webbrowser.open_new_tab(gsearch+str)
    	return "match didn't find any information to that, here the search results found in google"
