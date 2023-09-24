
import webbrowser
# webbrowser.open('https://us05web.zoom.us/j/85411865375?pwd=aGJ3aElUeW9JUGxvRkdvb1B6UHNSQT09', new=2)
with open('./utilts/meeting_link.txt', 'w') as f:
    link_text = f.read()
webbrowser.open(link_text, new=2)
