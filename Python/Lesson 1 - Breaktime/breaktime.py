import webbrowser
import time

print("This program started on "+time.ctime())
breaks = 0
while (breaks < 3):
    time.sleep(10)
    webbrowser.open("http://www.youtube.co/watch?v=dQw4w9WgXcQ")
    breaks = breaks + 1
