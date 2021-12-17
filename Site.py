import urllib.request 
import urllib.parse
from bs4 import BeautifulSoup

class Site:

    class Tag:

        class A:
            
            HREF = []

            def __init__(self):
                pass

        class IMG:
            
            SRC = []

            def __init__(self):
                pass

        A = A()

        IMG = IMG() 

        def __init__(self):
            pass

    URL = ""
    Soup = None
    Title = None
    Tag = Tag()

    def __init__(self, URL):
        self.URL = URL
        
        page = urllib.request.urlopen(URL)

        self.Soup = BeautifulSoup(page, "lxml")
        
        self.Title = self.Soup.title.string

        for a in self.Soup.find_all('a', href=True):
            self.Tag.A.HREF.append(urllib.parse.urljoin(URL,a['href']))


    