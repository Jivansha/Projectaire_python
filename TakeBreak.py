import time
import webbrowser
i=3
while(i>0):
    print("This program started on " + time.ctime())
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=umWABit-wbk")
    i=i-1
