from multiprocessing.pool import ThreadPool
import os, time
from threading import Thread
from Site import Site

URLs = ['https://www.w3schools.com/','https://stackoverflow.com/','https://kenh14.vn/']

URLs_Done = []

ThreadCount = 0

def myfunc(URL,ThreadName):
    global ThreadCount
    global URLs

    ThreadCount+=1
    try:

        Site_ = Site(URL)

        print(str(ThreadName) +' - '+Site_.Title)

        URLs = URLs + Site_.Tag.A.HREF
        
        print(URLs[0])
    except Exception as e:
        print(e)
    finally:
        ThreadCount-=1

while True:
    if len(URLs) <= 0:
        continue 
    if ThreadCount < 10:
        try:
            x = URLs_Done.index(URLs[0])
            URLs.remove(URLs[0])
        except:
            t = Thread(target=myfunc, args=(URLs[0],ThreadCount+1,))
            URLs_Done.append(URLs[0])
            URLs.remove(URLs[0])
            t.start()

print("Exit")

# for i in range(10):
#     t = Thread(target=myfunc, args=(i,))
#     t.start()