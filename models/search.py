from models.database import database

dbm =  database("localhost","root","","Gooly")
"""
handling searching result
"""
def suggest(keyword):
    pass

def result(keyword = None,page = 1, limit = 10):

    dic = {}

    dic["results"] = []
    dic["results_count_all"] = 0
    dic["results_count_show_from"] = 0
    dic["results_count_show_to"] = 0
    dic["results_page_count"] = 0
    dic["results_page_current"] = 0
    dic["results_page_list"] = []


    try:
        print("keyword:",keyword)
        keyword = '%'.join(keyword.split()) if keyword else ""

        sql = "SELECT * FROM site b WHERE CONCAT(b.url, b.html_tag_title, b.html_tag_meta_description) LIKE '%{}%' ORDER BY (select count(p.id) from site_visit p where p.id = b.id) DESC ".format(keyword)


        dbm.cursor.execute(sql)
        records = dbm.cursor.fetchall()
        # print(records)
        if len(records) <= 0:
            return dic


        dic["results_count_all"] = len(records)
        
        dic["results_count_show_from"] = ((page-1)*limit)

        dic["results_page_count"] = len(records)/limit
        if (len(records) > limit):
            dic["results_page_count"]= dic["results_page_count"]+1
        
        dic["results_page_count_range"] = range(1,int(len(records)/int(limit)+2))
        dic["results_page_current"] = page

        dic["results_count_show_to"] = ((page-1)*limit)+limit if dic["results_count_all"] >= ((page-1)*limit)+limit else  dic["results_count_all"]

        ###
        dic["results_page_list"] = []

        for x in range(page-1, (page-(2+1)),-1):
            if (x < 1):
                break
            dic["results_page_list"].append(x)
            
        dic["results_page_list"].reverse()

        dic["results_page_list"].append(page)  

        for x in range(page+1, page+(2+1)):
            if (x > dic["results_page_count"]):
                break
            dic["results_page_list"].append(x)
        ###


        recordss = records[dic["results_count_show_from"]:dic["results_count_show_to"]]
        
        for i in range(len(recordss)):
            record = recordss[i]

            # print(record)

            dict_ = {"id": record[0],
                        "url": record[1],
                        "html_tag_meta_description": record[3],
                        "html_tag_title": record[2],
                        "result_breadcrumb_by_url" : result_breadcrumb_by_url(record[1])
                        }

            # print(thisdict)
            
            dic["results"].append(dict_)


        return dic
    except Exception as ex:
        import  traceback
        print(traceback.format_exc())
        return dic

def result_breadcrumb_by_url(rs):
    arr = []
    rs = rs.split("/")

    try:
        rs.remove("https:")
    except:
        pass

    rs.remove("")

    for x in rs:
        try:
            xs = x.split(".")
            arr.append(xs[0])
        except:
            arr.append(x)

    return arr






