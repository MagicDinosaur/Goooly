from models.database import database
import time

dbm = database("localhost", "root", "", "Gooly")
"""
handling visited sites
"""
def visit(id, keyword):
    result = dbm.cursor.execute(
        "INSERT INTO site_visit (id,keyword,time)  VALUES (%s,%s,%s)", (
            id,
            keyword,
            int(time.time()),
        )
    )

    dbm.cursor.commit()
