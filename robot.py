import datetime
import sys
import requests
# from .DatabaseManager import NewDatabaseManager
from models.robot.site import site
from models.database import database
import time
import re
from os.path import basename
import os
from os.path import basename
import urllib.parse
import shutil
import urllib.request
import pathlib
import traceback
from random import randrange
"""

robot tool to recursively find and add data from website to local storage
"""
site_list = ['https://www.cnet.com/']

dbm =  database("localhost","root","","gooly")
print(dbm.cursor)
random_index = randrange(len(site_list))
url = site_list[random_index]
print(url)
dbm.cursor.execute('SELECT id FROM site WHERE url = %s',(url,))
records = dbm.cursor.fetchall()
print(records)

get = site.get(url)


print("url: "+url)
print("html_tag_title: "+get['html_tag_title'])
print("html_tag_meta_title: "+get['html_tag_meta_title'])
print("html_tag_meta_description: "+get['html_tag_meta_description'])
print("html_tag_meta_image: "+get['html_tag_meta_image'])
print("html_tag_a_href length: "+str(len(get['html_tag_a_href'])))
print("html_tag_img_src length: "+str(len(get['html_tag_img_src'])))

while True:

    try:
        if (len(site_list) == 0):
            break

        random_index = randrange(len(site_list))

        url = site_list[random_index]
        site_list.pop(random_index)

        get = site.get(url)

        if (get == None):
            continue

        print("url: "+url)
        print("html_tag_title: "+get['html_tag_title'])
        print("html_tag_meta_title: "+get['html_tag_meta_title'])
        print("html_tag_meta_description: "+get['html_tag_meta_description'])
        print("html_tag_meta_image: "+get['html_tag_meta_image'])
        print("html_tag_a_href length: "+str(len(get['html_tag_a_href'])))
        print("html_tag_img_src length: "+str(len(get['html_tag_img_src'])))

        print("==============================================")

        site_list = site_list + get['html_tag_a_href']

        dbm.cursor.execute('SELECT id FROM site WHERE url = %s',(url,))
        records = dbm.cursor.fetchall()

        # print("records: ", dbm.cursor._last_executed )

        # if len(records) > 0:
        #     continue
        if( str(get['html_tag_title']) == "" or str(get['html_tag_meta_title']) == "" or str(get['html_tag_meta_description']) == "" or str(get['html_tag_meta_image']) == ""):
            continue

        result = dbm.cursor.execute(
            "INSERT INTO site (url, html_tag_title, html_tag_meta_title, html_tag_meta_description, html_tag_meta_image, server_time_created)  VALUES (%s, %s,%s,%s,%s,%s);",
            (
                url,
                str(get['html_tag_title']),
                str(get['html_tag_meta_title']),
                str(get['html_tag_meta_description']),
                str(get['html_tag_meta_image']),
                time.strftime('%Y-%m-%d %H:%M:%S'),
            )
        )
        dbm.conn.commit()


    except:
        pass