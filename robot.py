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
from random import randrange

site_list = ['https://kenh14.vn/','https://vnexpress.net/']

dbm =  database ("localhost","root","","Gooly")

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
        if len(records) > 0:
            continue

        result =  dbm.cursor.execute(
            "INSERT INTO site (url, html_tag_title, html_tag_meta_title, html_tag_meta_description, html_tag_meta_image, server_time_created)  VALUES (%s, %s,%s,%s,%s,%s);",(
                url,
                get['html_tag_title'],
                get['html_tag_meta_title'],
                get['html_tag_meta_description'],
                get['html_tag_meta_image'],
                int(time.time()),
            )
        )

        # dbm.cursor.execute("SELECT @@IDENTITY AS ID;")
        # site_id = dbm.cursor.fetchone()[0]

        # if (get['html_tag_meta_image'] != ""):
        #     try:
        #         fname = getFileName(get['html_tag_meta_image'],urllib.request.urlopen(urllib.request.Request(get['html_tag_meta_image'])))
        #
        #         result =  dbm.cursor.execute(
        #             "INSERT INTO site_image (site_id, url, name, type, server_time_created)  VALUES (?,?,?,?,?);",
        #             site_id,
        #             url,
        #             pathlib.Path(fname).stem,
        #             pathlib.Path(fname).suffix.replace(".",""),
        #             int(time.time())
        #         )
        #
        #         dbm.cursor.execute("SELECT @@IDENTITY AS ID;")
        #         site_img_id = dbm.cursor.fetchone()[0]
        #
        #         download(get['html_tag_meta_image'],str(site_img_id)+"."+pathlib.Path(fname).suffix.replace(".",""))
        #     except:
        #         pass
        #
        # if (len(get['html_tag_img_src']) > 0):
        #     for x in get['html_tag_img_src']:
        #         try:
        #             fname = getFileName(x,urllib.request.urlopen(urllib.request.Request(x)))
        #
        #             result =  dbm.cursor.execute(
        #                 "INSERT INTO site_image (site_id, url, name, type, server_time_created)  VALUES (?,?,?,?,?);",
        #                 site_id,
        #                 url,
        #                 pathlib.Path(fname).stem,
        #                 pathlib.Path(fname).suffix.replace(".",""),
        #                 int(time.time())
        #             )
        #
        #             dbm.cursor.execute("SELECT @@IDENTITY AS ID;")
        #             site_img_id = dbm.cursor.fetchone()[0]
        #
        #             download(x,str(site_img_id)+"."+pathlib.Path(fname).suffix.replace(".",""))
        #         except:
        #             pass

        dbm.conn.commit()
    except:
        pass