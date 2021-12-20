import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import traceback

class site:

    @staticmethod
    def get(url):
        try:
            webpage = urlopen(url)
            if webpage.getcode() != 200:
                return None

            html_tag_title, html_tag_meta_title, html_tag_meta_description, html_tag_meta_image = "","","",""

            soup = BeautifulSoup(webpage.read(), "lxml")

            try:
                html_tag_title = soup.title.string
            except:
                pass
            #
            try:
                html_tag_meta_title = soup.find("meta",property="og:title")['content']
            except:
                try:
                    html_tag_meta_title = soup.find("meta",name="twitter:title")['content']
                except:
                    try:
                        html_tag_meta_title = soup.find("meta",itemprop="name")['content']
                    except:
                        pass
            #
            try:
                html_tag_meta_description = soup.find("meta",property="og:description")['content']
            except:
                try:
                    html_tag_meta_description = soup.find("meta",name="twitter:description")['content']
                except:
                    try:
                        html_tag_meta_description = soup.find("meta",itemprop="description")['content']
                    except:
                        try:
                            html_tag_meta_description = soup.find("meta",name="description")['content']
                        except:
                            pass

            try:
                html_tag_meta_image = soup.find("meta",  property="og:image")['content']
            except:
                pass
            #

            cars = []
            for a in soup.find_all('a', href=True):
                cars.append(urllib.parse.urljoin(url,a['href']))

            cars1 = []
            images = soup.findAll('img')
            for image in images:
                cars1.append(urllib.parse.urljoin(url,image['src']))

            mydict = {"html_tag_title": html_tag_title, "html_tag_meta_title": html_tag_meta_title, "html_tag_meta_description": html_tag_meta_description, "html_tag_meta_image" : html_tag_meta_image, "html_tag_a_href" : cars, "html_tag_img_src" : cars1}

            return mydict
        except:
            # traceback.print_exc()
            return None
