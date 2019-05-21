#Creat a scrpt that let thr user type in a search term and opens and search on the browser for that on the google

import webbrowser
word = input("Provide the word to be searched on google:")
url = 'http://www.google.com/search?btnG=1&q=%s' % word
webbrowser.open_new(url)
